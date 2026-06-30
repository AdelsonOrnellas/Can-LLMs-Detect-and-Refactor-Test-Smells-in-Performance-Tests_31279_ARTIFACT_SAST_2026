import os
import json
import asyncio
import re
from pathlib import Path
from datetime import datetime

import anthropic
from openai import AsyncOpenAI
import google.generativeai as genai

K6_SCRIPTS_DIR = Path("./k6_scripts")
RESULTS_DIR    = Path("./results")

CLAUDE_MODEL  = "claude-sonnet-4-6"           
CHATGPT_MODEL = "gpt-5.5-2026-04-23"
GEMINI_MODEL  = "gemini-2.5-pro"             

SMELL_NAMES = {
    1: "Costly ops in init context",
    2: "No thresholds",
    3: "Not checking requests",
    4: "Not using tags",
}

PROMPT_TEMPLATE = """You are an expert in performance engineering, load testing, and k6 scripting.
Review the following k6 code and identify whether it contains any of the four performance smells described below. For each smell, a number (1–4), a name, a definition, and a concrete example are provided.

SMELL 1 — Costly operations in the init context
Definition:
The init context runs once per virtual user before the test starts. Performing expensive operations in this phase — such as reading large files, parsing JSON, or executing heavy computations — can degrade performance and increase resource usage unnecessarily.
Example:
import {{ open }} from "k6";
const largeDataFile = open("./large-data.json");
const testData = JSON.parse(largeDataFile);       // heavy parsing in init
for (let i = 0; i < 100; i++) {{
  console.log(i);                                  // unnecessary loop in init
}}

SMELL 2 — Do not use thresholds
Definition:
Thresholds define success or failure conditions based on test metrics. Without them, a test may always be reported as successful even when the system is underperforming, creating false confidence — especially in CI/CD pipelines.
Example:
import http from 'k6/http';
export const options = {{
  vus: 50,
  duration: '1m',
  // no thresholds defined
}};
export default function () {{
  http.get('https://api.minha-aplicacao.com');
}}

SMELL 3 — Not checking requests
Definition:
k6 does not automatically fail a test when HTTP requests return 4xx or 5xx responses; it only updates failure-related metrics and continues execution. Without explicit checks validating response correctness, the script may produce false positives and incorrectly report successful results.
Example:
import http from 'k6/http';
import {{ sleep }} from 'k6';
export const options = {{
  thresholds: {{
    http_req_duration: ['p(95)<500'],
  }},
}};
export default function () {{
  http.get('https://api.minha-aplicacao.com/dados-criticos');  // no check()
  sleep(1);
}}

SMELL 4 — Not using tags
Definition:
Tags are key-value metadata that can be attached to requests, metrics, and checks in k6. Without tags, it becomes difficult to filter and group metrics by endpoint or user flow, making it harder to pinpoint the source of performance issues.
Example:
import http from 'k6/http';
import {{ check }} from 'k6';
export const options = {{
  thresholds: {{
    'http_req_duration{{name:Login}}': ['p(95)<300'],
    'http_req_duration{{name:Products}}': ['p(95)<1000'],
    'http_req_duration{{name:Cart}}': ['p(95)<500'],
  }},
}};
export default function () {{
  http.get('https://api.minha-aplicacao.com/login');     // no tags attached
  http.get('https://api.minha-aplicacao.com/products');  // no tags attached
  http.get('https://api.minha-aplicacao.com/cart');      // no tags attached
}}

TASK:
Analyze the k6 code provided below and determine whether it contains one or more of the smells above (1, 2, 3, or 4).
For each smell detected:
- Identify which smell it is (number and name).
- Point out exactly where in the code it occurs.
- Suggest a refactored version for code with a code smell.
If no smell is found, state that the code does not exhibit any of the four performance smells described.

Return ONLY a valid JSON object, no markdown, no explanation, no backticks.
Schema:
{{
  "smells": [
    {{
      "smell_id": <1|2|3|4>,
      "smell_name": "<name of the smell>",
      "lines": [<line numbers as integers>],
      "snippet": "<short code excerpt showing the problem>",
      "refactored": "<suggested refactored version of the problematic code>"
    }}
  ],
  "summary": "<if no smells found, state that the code does not exhibit any of the four performance smells described, otherwise leave as empty string>"
}}

If no smells are found, return:
{{"smells": [], "summary": "The code does not exhibit any of the four performance smells described."}}

k6 code to analyze (with line numbers):
{numbered_code}
"""


def add_line_numbers(code: str) -> str:
    return "\n".join(f"{i+1:3}: {line}" for i, line in enumerate(code.splitlines()))


def parse_llm_json(raw: str) -> dict:
    clean = re.sub(r"```(?:json)?|```", "", raw).strip()
    return json.loads(clean)


async def call_claude(prompt: str) -> dict:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(
        None,
        lambda: client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}],
        ),
    )
    return parse_llm_json(response.content[0].text)


async def call_chatgpt(prompt: str) -> dict:
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = await client.chat.completions.create(
        model=CHATGPT_MODEL,
        max_completion_tokens=2000,           # corrigido
        messages=[{"role": "user", "content": prompt}],
    )
    return parse_llm_json(response.choices[0].message.content)


async def call_gemini(prompt: str) -> dict:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel(GEMINI_MODEL)
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, lambda: model.generate_content(prompt))
    return parse_llm_json(response.text)


async def analyze_file(file_path: Path) -> dict:
    code = file_path.read_text(encoding="utf-8")
    numbered = add_line_numbers(code)
    prompt = PROMPT_TEMPLATE.format(numbered_code=numbered)

    print(f"  analyzing {file_path.name}...")

    results = await asyncio.gather(
        call_claude(prompt),
        call_chatgpt(prompt),
        call_gemini(prompt),
        return_exceptions=True,
    )

    labels = ["claude", "chatgpt", "gemini"]
    parsed = {}
    for label, result in zip(labels, results):
        if isinstance(result, Exception):
            print(f"  {label} failed: {result}")
            parsed[label] = {"smells": [], "summary": "", "error": str(result)}
        else:
            parsed[label] = result

    return {"file": file_path.name, "timestamp": datetime.now().isoformat(), **parsed}


RESET  = "\033[0m"
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
DIM    = "\033[2m"


def print_summary_table(all_results: list[dict]):
    COL_FILE  = 28
    COL_LLM   = 10
    COL_S     = 6
    COL_LINES = 24

    PRESENT = f"{RED}  x  {RESET}"
    ABSENT  = "     "

    sep = (
        "+" + "-" * (COL_FILE + 2)
        + "+" + "-" * (COL_LLM + 2)
        + "+" + "-" * (COL_S + 2)
        + "+" + "-" * (COL_S + 2)
        + "+" + "-" * (COL_S + 2)
        + "+" + "-" * (COL_S + 2)
        + "+" + "-" * (COL_LINES + 2)
        + "+"
    )

    def row(file, llm, s1, s2, s3, s4, lines):
        return (
            f"| {file:<{COL_FILE}} "
            f"| {llm:<{COL_LLM}} "
            f"| {s1:^{COL_S}} "
            f"| {s2:^{COL_S}} "
            f"| {s3:^{COL_S}} "
            f"| {s4:^{COL_S}} "
            f"| {lines:<{COL_LINES}} |"
        )

    print()
    print(f"  {DIM}S1 = Costly init   S2 = No thresholds   S3 = No checks   S4 = No tags{RESET}")
    print(f"  {DIM}x = smell detected{RESET}")
    print()
    print(sep)
    print(row("File", "LLM", "S1", "S2", "S3", "S4", "Lines with smells"))
    print(sep)

    for res in all_results:
        fname = res["file"]
        first = True

        for llm in ["claude", "chatgpt", "gemini"]:
            data   = res.get(llm, {})
            smells = data.get("smells", [])
            found  = {s["smell_id"] for s in smells}

            all_lines = []
            for s in smells:
                for ln in s.get("lines", []):
                    all_lines.append(f"S{s['smell_id']}:L{ln}")
            lines_str = ", ".join(all_lines) if all_lines else "none"
            if len(lines_str) > COL_LINES:
                lines_str = lines_str[: COL_LINES - 1] + "..."

            display_file = fname if first else ""
            if len(display_file) > COL_FILE:
                display_file = display_file[: COL_FILE - 1] + "..."

            print(row(
                display_file,
                llm,
                PRESENT if 1 in found else ABSENT,
                PRESENT if 2 in found else ABSENT,
                PRESENT if 3 in found else ABSENT,
                PRESENT if 4 in found else ABSENT,
                lines_str,
            ))
            first = False

        print(sep)

    print(f"\n{YELLOW}=== Refactoring Suggestions ==={RESET}\n")
    for res in all_results:
        fname = res["file"]
        for llm in ["claude", "chatgpt", "gemini"]:
            data   = res.get(llm, {})
            smells = data.get("smells", [])
            if smells:
                print(f"{CYAN}[{fname}] — {llm.upper()}{RESET}")
                for s in smells:
                    print(f"  {RED}Smell {s['smell_id']}: {s.get('smell_name', SMELL_NAMES.get(s['smell_id'], ''))}{RESET}")
                    print(f"  Lines: {s.get('lines', [])}")
                    print(f"  Snippet:    {DIM}{s.get('snippet', '')}{RESET}")
                    print(f"  Refactored: {GREEN}{s.get('refactored', 'N/A')}{RESET}")
                    print()


def save_results(all_results: list[dict]):
    RESULTS_DIR.mkdir(exist_ok=True)

    json_path = RESULTS_DIR / "results.json"
    json_path.write_text(json.dumps(all_results, indent=2, ensure_ascii=False), encoding="utf-8")

    md_lines = [
        "# k6 Performance Smell Analysis",
        f"Generated: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n",
        "S1 = Costly init | S2 = No thresholds | S3 = No checks | S4 = No tags\n",
        "| File | LLM | S1 | S2 | S3 | S4 | Lines with smells |",
        "|------|-----|:--:|:--:|:--:|:--:|-------------------|",
    ]

    for res in all_results:
        fname = res["file"]
        first = True
        for llm in ["claude", "chatgpt", "gemini"]:
            data   = res.get(llm, {})
            smells = data.get("smells", [])
            found  = {s["smell_id"] for s in smells}

            all_lines = []
            for s in smells:
                for ln in s.get("lines", []):
                    all_lines.append(f"S{s['smell_id']}:L{ln}")
            lines_str = ", ".join(all_lines) if all_lines else "-"

            md_lines.append(
                f"| {'`' + fname + '`' if first else ''} "
                f"| {llm} "
                f"| {'x' if 1 in found else ''} "
                f"| {'x' if 2 in found else ''} "
                f"| {'x' if 3 in found else ''} "
                f"| {'x' if 4 in found else ''} "
                f"| {lines_str} |"
            )
            first = False

    md_lines.append("\n## Refactoring Suggestions\n")
    for res in all_results:
        fname = res["file"]
        for llm in ["claude", "chatgpt", "gemini"]:
            data   = res.get(llm, {})
            smells = data.get("smells", [])
            if smells:
                md_lines.append(f"### `{fname}` — {llm.upper()}\n")
                for s in smells:
                    name = s.get("smell_name", SMELL_NAMES.get(s["smell_id"], ""))
                    md_lines.append(f"**Smell {s['smell_id']}: {name}**\n")
                    md_lines.append(f"- **Lines:** {s.get('lines', [])}")
                    md_lines.append(f"- **Snippet:**\n```js\n{s.get('snippet', '')}\n```")
                    md_lines.append(f"- **Refactored:**\n```js\n{s.get('refactored', 'N/A')}\n```\n")

    md_path = RESULTS_DIR / "report.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"\n{GREEN}results saved to {RESULTS_DIR}/{RESET}")


async def main():
    print(f"\n{YELLOW}k6 smell detector{RESET}\n")

    if not K6_SCRIPTS_DIR.exists():
        print(f"folder not found: {K6_SCRIPTS_DIR}")
        return

    files = sorted(K6_SCRIPTS_DIR.glob("*.js"))
    if not files:
        print(f"no .js files found in {K6_SCRIPTS_DIR}")
        return

    print(f"{len(files)} file(s) found\n")

    all_results = []
    for file in files:
        result = await analyze_file(file)
        all_results.append(result)

    print_summary_table(all_results)
    save_results(all_results)
    print(f"\n{GREEN}done{RESET}")


if __name__ == "__main__":
    asyncio.run(main())