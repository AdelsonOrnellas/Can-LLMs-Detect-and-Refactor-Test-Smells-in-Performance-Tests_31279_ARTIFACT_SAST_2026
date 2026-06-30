"""
F-Measure para avaliação de Code Smell Detection por LLMs
==========================================================
Compara os resultados de 3 LLMs (claude, chatgpt, gemini) com o Oracle (gabarito)
para os 228 arquivos e os 4 smells (S1, S2, S3, S4).

Lógica de classificação (por arquivo × smell):
  - Oracle = 'x' e LLM = 'x'  → True Positive  (TP)
  - Oracle = NaN e LLM = 'x'  → False Positive (FP)
  - Oracle = 'x' e LLM = NaN  → False Negative (FN)
  - Oracle = NaN e LLM = NaN  → True Negative  (TN)

Métricas calculadas:
  Precision = TP / (TP + FP)
  Recall    = TP / (TP + FN)
  F1        = 2 * P * R / (P + R)
  Accuracy  = (TP + TN) / (TP + FP + FN + TN)

Saídas:
  - metricas_por_smell.csv  → por LLM × smell
  - metricas_gerais.csv     → por LLM (micro e macro média)
  - metricas_por_arquivo.csv → por LLM × arquivo
  - confusion_matrix.csv    → TP/FP/FN/TN por LLM × smell
  - relatorio_fmeasure.txt  → resumo legível
"""

import pandas as pd
import numpy as np
import os
from pathlib import Path

# ── Configuração ──────────────────────────────────────────────────────────────
ORACLE_PATH = "Oracle.csv"
PROMPTS = {
    "Prompt_01": "Tabela_Prompt_01.csv",
    # Adicione outros prompts/tabelas aqui se necessário:
    # "Prompt_02": "Tabela_Prompt_02.csv",
}
SMELLS = ["S1", "S2", "S3", "S4"]
OUTPUT_DIR = Path("resultados_fmeasure")
OUTPUT_DIR.mkdir(exist_ok=True)

# ── Funções auxiliares ────────────────────────────────────────────────────────

def is_positive(val) -> bool:
    """Retorna True se o valor indica detecção (célula == 'x')."""
    if pd.isna(val):
        return False
    return str(val).strip().lower() == "x"


def confusion_counts(oracle_col: pd.Series, llm_col: pd.Series) -> dict:
    """Calcula TP, FP, FN, TN para um par de colunas."""
    o = oracle_col.map(is_positive)
    p = llm_col.map(is_positive)

    tp = int(( o &  p).sum())
    fp = int((~o &  p).sum())
    fn = int(( o & ~p).sum())
    tn = int((~o & ~p).sum())
    return {"TP": tp, "FP": fp, "FN": fn, "TN": tn}


def metrics_from_counts(tp: int, fp: int, fn: int, tn: int) -> dict:
    """Calcula Precision, Recall, F1 e Accuracy a partir dos contadores."""
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall    = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1        = (2 * precision * recall / (precision + recall)
                 if (precision + recall) > 0 else 0.0)
    total     = tp + fp + fn + tn
    accuracy  = (tp + tn) / total if total > 0 else 0.0
    return {
        "Precision": round(precision, 4),
        "Recall":    round(recall,    4),
        "F1":        round(f1,        4),
        "Accuracy":  round(accuracy,  4),
    }


# ── Carregamento de dados ─────────────────────────────────────────────────────

def load_data(oracle_path: str, prompt_path: str):
    oracle = pd.read_csv(oracle_path)
    prompt = pd.read_csv(prompt_path)

    # Normaliza nomes de colunas
    oracle.columns = oracle.columns.str.strip()
    prompt.columns = prompt.columns.str.strip()

    # Garante que 'File' seja a chave de junção
    oracle["File"] = oracle["File"].str.strip()
    prompt["File"] = prompt["File"].str.strip()
    prompt["LLM"]  = prompt["LLM"].str.strip().str.lower()

    return oracle, prompt


# ── Cálculo de métricas ───────────────────────────────────────────────────────

def compute_metrics(oracle: pd.DataFrame, prompt: pd.DataFrame, prompt_name: str):
    llms = sorted(prompt["LLM"].unique())

    rows_smell   = []   # por LLM × smell
    rows_arquivo = []   # por LLM × arquivo
    rows_conf    = []   # confusion matrix
    rows_geral   = []   # micro/macro por LLM

    for llm in llms:
        llm_df = prompt[prompt["LLM"] == llm].set_index("File")

        # ── por arquivo ──────────────────────────────────────────────────────
        for _, oracle_row in oracle.iterrows():
            file = oracle_row["File"]
            if file not in llm_df.index:
                continue
            llm_row = llm_df.loc[file]

            file_tp = file_fp = file_fn = file_tn = 0
            for smell in SMELLS:
                c = confusion_counts(
                    pd.Series([oracle_row[smell]]),
                    pd.Series([llm_row[smell]])
                )
                file_tp += c["TP"]; file_fp += c["FP"]
                file_fn += c["FN"]; file_tn += c["TN"]

            m = metrics_from_counts(file_tp, file_fp, file_fn, file_tn)
            rows_arquivo.append({
                "Prompt": prompt_name,
                "LLM": llm,
                "File": file,
                "TP": file_tp, "FP": file_fp, "FN": file_fn, "TN": file_tn,
                **m
            })

        # ── por smell ────────────────────────────────────────────────────────
        macro_p = macro_r = macro_f1 = macro_acc = 0.0
        micro_tp = micro_fp = micro_fn = micro_tn = 0

        for smell in SMELLS:
            merged = oracle[["File", smell]].merge(
                llm_df[[smell]].reset_index(),
                on="File", suffixes=("_oracle", "_llm")
            )
            c = confusion_counts(
                merged[f"{smell}_oracle"],
                merged[f"{smell}_llm"]
            )
            m = metrics_from_counts(c["TP"], c["FP"], c["FN"], c["TN"])

            rows_smell.append({
                "Prompt": prompt_name,
                "LLM":   llm,
                "Smell": smell,
                **c, **m
            })
            rows_conf.append({
                "Prompt": prompt_name,
                "LLM": llm, "Smell": smell, **c
            })

            macro_p   += m["Precision"]
            macro_r   += m["Recall"]
            macro_f1  += m["F1"]
            macro_acc += m["Accuracy"]

            micro_tp += c["TP"]; micro_fp += c["FP"]
            micro_fn += c["FN"]; micro_tn += c["TN"]

        n = len(SMELLS)
        macro = {
            "Precision_macro": round(macro_p  / n, 4),
            "Recall_macro":    round(macro_r  / n, 4),
            "F1_macro":        round(macro_f1 / n, 4),
            "Accuracy_macro":  round(macro_acc / n, 4),
        }
        micro_m = metrics_from_counts(micro_tp, micro_fp, micro_fn, micro_tn)
        micro = {f"{k}_micro": v for k, v in micro_m.items()}

        rows_geral.append({
            "Prompt": prompt_name,
            "LLM": llm,
            "TP_total": micro_tp, "FP_total": micro_fp,
            "FN_total": micro_fn, "TN_total": micro_tn,
            **micro, **macro
        })

    return (
        pd.DataFrame(rows_smell),
        pd.DataFrame(rows_arquivo),
        pd.DataFrame(rows_conf),
        pd.DataFrame(rows_geral),
    )


# ── Relatório textual ─────────────────────────────────────────────────────────

def gerar_relatorio(df_geral: pd.DataFrame, df_smell: pd.DataFrame,
                    df_conf: pd.DataFrame, output_path: Path):
    lines = []
    sep = "=" * 70

    lines.append(sep)
    lines.append("  RELATÓRIO DE F-MEASURE — AVALIAÇÃO DE LLMs vs. ORACLE")
    lines.append(sep)
    lines.append("")

    for prompt in df_geral["Prompt"].unique():
        lines.append(f"  PROMPT: {prompt}")
        lines.append("-" * 70)

        g = df_geral[df_geral["Prompt"] == prompt]
        for _, row in g.iterrows():
            llm = row["LLM"].upper()
            lines.append(f"\n  [{llm}]")
            lines.append(f"  {'Métrica':<20} {'Micro':>8}  {'Macro':>8}")
            lines.append(f"  {'-'*40}")
            for metric in ["Precision", "Recall", "F1", "Accuracy"]:
                micro_val = row[f"{metric}_micro"]
                macro_val = row[f"{metric}_macro"]
                lines.append(f"  {metric:<20} {micro_val:>8.4f}  {macro_val:>8.4f}")

            lines.append(f"\n  Por smell:")
            lines.append(f"  {'Smell':<6} {'P':>8} {'R':>8} {'F1':>8} {'Acc':>8} "
                         f"{'TP':>5} {'FP':>5} {'FN':>5} {'TN':>5}")
            lines.append(f"  {'-'*66}")
            s = df_smell[(df_smell["Prompt"] == prompt) & (df_smell["LLM"] == row["LLM"])]
            for _, sr in s.iterrows():
                lines.append(
                    f"  {sr['Smell']:<6} {sr['Precision']:>8.4f} {sr['Recall']:>8.4f} "
                    f"{sr['F1']:>8.4f} {sr['Accuracy']:>8.4f} "
                    f"{sr['TP']:>5} {sr['FP']:>5} {sr['FN']:>5} {sr['TN']:>5}"
                )

        lines.append("\n" + sep + "\n")

    report = "\n".join(lines)
    output_path.write_text(report, encoding="utf-8")
    print(report)


# ── Pipeline principal ────────────────────────────────────────────────────────

def main():
    all_smell   = []
    all_arquivo = []
    all_conf    = []
    all_geral   = []

    for prompt_name, prompt_path in PROMPTS.items():
        if not os.path.exists(oracle_path := ORACLE_PATH):
            raise FileNotFoundError(f"Oracle não encontrado: {oracle_path}")
        if not os.path.exists(prompt_path):
            raise FileNotFoundError(f"Tabela de prompt não encontrada: {prompt_path}")

        print(f"\n>>> Processando: {prompt_name} ({prompt_path})")
        oracle, prompt = load_data(oracle_path, prompt_path)

        df_smell, df_arq, df_conf, df_geral = compute_metrics(
            oracle, prompt, prompt_name
        )
        all_smell.append(df_smell)
        all_arquivo.append(df_arq)
        all_conf.append(df_conf)
        all_geral.append(df_geral)

    # Consolida
    df_smell_all   = pd.concat(all_smell,   ignore_index=True)
    df_arquivo_all = pd.concat(all_arquivo, ignore_index=True)
    df_conf_all    = pd.concat(all_conf,    ignore_index=True)
    df_geral_all   = pd.concat(all_geral,   ignore_index=True)

    # Salva CSVs
    df_smell_all.to_csv(   OUTPUT_DIR / "metricas_por_smell.csv",   index=False)
    df_arquivo_all.to_csv( OUTPUT_DIR / "metricas_por_arquivo.csv", index=False)
    df_conf_all.to_csv(    OUTPUT_DIR / "confusion_matrix.csv",     index=False)
    df_geral_all.to_csv(   OUTPUT_DIR / "metricas_gerais.csv",      index=False)

    # Relatório
    gerar_relatorio(
        df_geral_all, df_smell_all, df_conf_all,
        OUTPUT_DIR / "relatorio_fmeasure.txt"
    )

    print(f"\n✔ Resultados salvos em: {OUTPUT_DIR.resolve()}/")
    print("  • metricas_gerais.csv       — Micro/macro por LLM")
    print("  • metricas_por_smell.csv    — Métricas por LLM × Smell")
    print("  • metricas_por_arquivo.csv  — Métricas por LLM × Arquivo")
    print("  • confusion_matrix.csv      — TP/FP/FN/TN por LLM × Smell")
    print("  • relatorio_fmeasure.txt    — Resumo legível")


if __name__ == "__main__":
    main()
