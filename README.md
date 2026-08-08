# Can LLMs Detect and Refactor Test Smells in Performance Tests?

Replication package and artifacts for the empirical study evaluating whether
three widely used Large Language Models (LLMs) — **Claude**, **GPT**, and
**Gemini** — can detect and refactor four performance test smells in real-world
[k6](https://grafana.com/docs/k6/latest/) load testing scripts, and whether
adding illustrative code examples to the prompt changes their performance.

The study targets SAST 2026 (Brazilian Symposium on Software Testing).

---

## Table of contents

- [Overview](#overview)
- [Performance test smells studied](#performance-test-smells-studied)
- [Research questions](#research-questions)
- [Study design](#study-design)
- [Main findings](#main-findings)
- [Repository structure](#repository-structure)
- [Requirements](#requirements)
- [How to reproduce](#how-to-reproduce)
- [Dataset](#dataset)
- [Version control hygiene](#version-control-hygiene)
- [Citation](#citation)
- [Acknowledgements](#acknowledgements)

---

## Overview

Performance testing verifies whether a system meets its responsiveness,
scalability, and resource-usage requirements under load. Frameworks such as k6
let developers write performance tests as scripts that are versioned, reviewed,
and integrated into CI/CD pipelines. Like any code, these scripts are exposed to
recurring bad practices, known as **performance test smells**, that can produce
misleading results or waste resources.

While LLMs have shown promise in detecting and refactoring conventional
(functional) test smells, their effectiveness on performance test smells was
largely unexplored. This study fills that gap through a controlled empirical
evaluation.

In numbers:

- **228** real-world k6 scripts, drawn from **58** open-source GitHub repositories.
- Ground truth produced by the **k6-performance** static linter (Barbosa, 2025).
- **3** LLMs evaluated through their official APIs.
- **2** prompt variants (definitions only vs. definitions plus code examples).
- **1,368** detection-and-refactoring queries (228 x 3 models x 2 prompts).
- **120** refactoring suggestions manually reviewed by a domain expert.

### Models evaluated

| Provider          | LLM    | Model version          |
|-------------------|--------|------------------------|
| Anthropic         | Claude | claude-sonnet-4-6      |
| OpenAI            | GPT    | gpt-5.5-2026-04-23     |
| Google DeepMind   | Gemini | gemini-2.5-pro         |

---

## Performance test smells studied

The four smells (S1–S4) are formalized from Barbosa (2025).

| ID  | Smell                                  | Short description |
|-----|----------------------------------------|-------------------|
| S1  | Costly operations in the init context  | Expensive work (file reads, JSON parsing, heavy computation) in the per-virtual-user init context. Fix: move one-time logic to `setup()` and shared data into a `SharedArray`. |
| S2  | Do not use thresholds                  | Missing `thresholds`, so a test may pass even when the system is underperforming. Fix: add a `thresholds` block defining pass/fail conditions. |
| S3  | Not checking requests                  | No `check()` on responses, so 4xx/5xx errors do not fail the test. Fix: add `check()` calls plus a threshold on the `checks` metric. |
| S4  | Not using tags                         | Requests/metrics not tagged, making it hard to filter and group results. Fix: attach key-value tags to requests, checks, and metrics. |

A key distinction discussed in the paper:

- **Declarative fixes** (S2, S3, S4): insert configuration, a validation call, or
  metadata. Self-contained and well-documented.
- **Architectural fixes** (S1): require reasoning about k6's execution lifecycle
  (execution order, scope, data lifetime across VUs).

---

## Research questions

- **RQ1:** Can LLMs detect and refactor performance smells in k6 scripts when
  prompted only with the smell definitions?
- **RQ2:** Can LLMs detect and refactor performance smells when prompted with the
  smell definitions accompanied by illustrative code examples?
- **RQ3:** How much do illustrative code examples improve performance compared to
  definitions alone?
- **RQ4:** Among the three LLMs, which achieves the highest detection accuracy?

---

## Study design

Two prompt variants were evaluated:

- **Prompt 1 (P1) — Description-only:** textual definition of each smell, followed
  by the k6 script and an instruction to identify smells, point out their exact
  location, and suggest a refactored version.
- **Prompt 2 (P2) — Description + Example:** P1 plus a concrete illustrative code
  snippet for each smell.

Each of the 228 scripts was submitted to each of the 3 LLMs under both prompts
(228 x 3 x 2 = 1,368 queries). Each query was a single, non-repeated API call with
default generation parameters (no resampling).

Detection was evaluated automatically against the linter ground truth using
Precision, Recall, F1 (micro and macro), Accuracy, and per-smell F1. Refactoring
quality was assessed manually on a stratified sample of up to 120 cases (restricted
to correctly detected smells), each rated as **Correct**, **Partial**,
**Incorrect**, or **Breaking**.

---

## Main findings

1. **Detection is moderate and comparable across models.** Under P1, F1 micro
   ranged from 0.5273 (Claude) to 0.5427 (Gemini). All three models struggled with
   the absence-based smells S2 and S3, and did better on the structural smells S1
   and S4.

2. **Adding code examples does not consistently help.** Under P2, F1 micro dropped
   for Claude and GPT and stayed roughly stable for Gemini. The paper attributes
   this to an attentional anchoring effect, where a salient example (S1) draws
   attention away from the other smells.

3. **Detection and refactoring are decoupled.** The hardest smells to detect
   (S2, S3) were refactored almost flawlessly once found, while one of the
   best-detected smells (S1) concentrated nearly all incorrect and breaking
   refactorings. The reliability of an LLM fix depends on whether it is
   declarative or architectural, not on the detection F1 of the smell.

### Overall detection metrics

| Prompt | LLM    | Prec.  | Recall | F1 (micro) | F1 (macro) | Acc.   |
|--------|--------|--------|--------|------------|------------|--------|
| P1     | Gemini | 0.4428 | 0.7007 | 0.5427     | 0.5544     | 0.6064 |
| P1     | Claude | 0.4430 | 0.6513 | 0.5273     | 0.5222     | 0.6107 |
| P1     | GPT    | 0.4584 | 0.6349 | 0.5324     | 0.5218     | 0.6283 |
| P2     | Gemini | 0.4417 | 0.6480 | 0.5253     | 0.5628     | 0.6096 |
| P2     | Claude | 0.4344 | 0.5559 | 0.4877     | 0.5007     | 0.6107 |
| P2     | GPT    | 0.4571 | 0.5954 | 0.5171     | 0.4904     | 0.6294 |

### Refactoring quality (120 reviewed suggestions)

| Category  | Count | %      |
|-----------|-------|--------|
| Correct   | 94    | 78.3%  |
| Partial   | 18    | 15.0%  |
| Incorrect | 5     | 4.2%   |
| Breaking  | 3     | 2.5%   |
| **Total** | 120   | 100%   |

Full per-smell and per-model breakdowns are reported in the paper (Tables 3, 5,
and 6) and reproduced in `05 - Analysis`.

---

## Repository structure

```
.
├── 01 - Prompts/                      Prompt templates used in the experiment (P1 and P2)
├── 02 - Dataset/
│   └── Database_suites/               The 228 k6 scripts used as input, with linter labels (S1-S4)
├── 03 - Scripts/
│   ├── k6-smell-detector-py/          Python tool that queries the LLM APIs and collects responses
│   │   ├── k6_scripts/                k6 scripts consumed by the tool
│   │   └── results/                   Raw run outputs
│   │       └── old/                   Earlier / superseded run outputs
│   └── k6-smell-detector-py - 2/      Second run or variant of the detector tool
│       ├── k6_scripts/
│       └── results/
│           └── old/
├── 04 - Results/
│   ├── Results 01/                    Raw LLM outputs for the first prompt variant
│   ├── Results 02/                    Raw LLM outputs for the second prompt variant
│   └── Results_Smells_k6/             Consolidated detection results
└── 05 - Analysis/
    ├── Qualitative Analysis/          Manual refactoring review (Correct/Partial/Incorrect/Breaking)
    └── Quantitative Analysis/
        ├── Binária/                   Binary presence/absence comparison vs. ground truth
        │   └── Comparação Binária P1 e P2/
        └── F1/                        F1-score computation and P1 vs. P2 comparison
            ├── Comparação P1 e P2/
            ├── Prompt_01/
            └── Prompt_02/
```

---

## Requirements

- Python 3.10+ (the bundled environment was built with the official API client
  libraries for the three providers).
- API access and keys for the three providers:
  - Anthropic (Claude)
  - OpenAI (GPT)
  - Google Generative AI (Gemini)

Core Python dependencies (inferred from the environment shipped in `03 - Scripts`):

```
anthropic
openai
google-generativeai
```

---

## How to reproduce

1. Clone the repository and enter the tool directory:

   ```bash
   git clone <REPO_URL>
   cd "<REPO_NAME>/03 - Scripts/k6-smell-detector-py"
   ```

2. Create and activate a fresh virtual environment, then install dependencies:

   ```bash
   python -m venv venv
   # Linux / macOS
   source venv/bin/activate
   # Windows
   venv\Scripts\activate

   pip install -r requirements.txt
   ```

3. Provide the API keys as environment variables:

   ```bash
   export ANTHROPIC_API_KEY="..."
   export OPENAI_API_KEY="..."
   export GOOGLE_API_KEY="..."
   ```

4. Run the detector over the dataset for a given prompt variant and model:

   ```bash
   python <detector_script>.py --prompt P1 --model claude-sonnet-4-6
   ```

5. The raw responses are written to `results/`. The quantitative comparison
   against the ground truth and the F1 computation are in `05 - Analysis`.

> **Cost warning:** Reproducing the full experiment issues 1,368 paid API calls
> across three providers. The original study deliberately sampled 228 scripts (down
> from 2,105) to keep API costs tractable. Re-running everything will incur real
> cost on your accounts.

---

## Dataset

The dataset comprises **228** real-world k6 scripts extracted from open-source
GitHub repositories, collected and annotated by the **k6-performance** linter.
For each script, the linter records the presence and exact location (line and
column) of each smell type (S1–S4), which serves as the ground truth.

Construction (two cleaning phases):

1. From **428** candidate repositories (**3,073** scripts), keep only those that
   are publicly accessible and contain at least one k6 script with a linter-annotated
   smell, yielding **212** repositories (**2,105** scripts).
2. Apply simple random sampling over the 212 repositories, yielding the final
   **58** repositories and **228** scripts, while preserving the distribution of
   smell types in the full corpus.

The dataset and the linter are derived from work made publicly available by
Barbosa (2025): https://github.com/samurollie/TCC

---

## Version control hygiene

When you recreate a virtual environment to run the detector tool, do **not**
commit it. Environments are large, platform-specific, and not reproducible across
machines. A `.gitignore` at the repository root keeps the repo clean:

```gitignore
# Python
__pycache__/
*.py[cod]
*.egg-info/
.venv/
venv/
env/

# Environment files
.env
*.key

# OS noise
.DS_Store
Thumbs.db
```

If a `venv/` was ever tracked, untrack it without deleting the local files:

```bash
git rm -r --cached "03 - Scripts/k6-smell-detector-py/venv"
```

---

## Citation

This study builds directly on the k6-performance linter and dataset:

```bibtex
@mastersthesis{barbosa2025k6,
  title  = {Detec{\c{c}}{\~a}o de Test Smells em Testes de Carga Implementados no Framework K6},
  author = {Barbosa, Samuel},
  school = {Universidade Federal de Alagoas},
  year   = {2025},
  note   = {Bachelor's Thesis. Artifacts: https://github.com/samurollie/TCC}
}
```

---

## Acknowledgements

We thank the reviewers for their feedback. This work was financed in part by the FAPEAL (Fundação de Amparo à Pesquisa do Estado de Alagoas)
Process: [E:60030.0000000591/2026], The work was also partially supported by INES.IA (National Institute of Science and Technology for Software Engineering Based on and for Artificial Intelligence) www.ines.org.br, CNPq grant 408817/2024-0. The work was also partially supported by CNPq, grants 312195/2021-4, 404825/2023-0, and 443393/2023-0.
