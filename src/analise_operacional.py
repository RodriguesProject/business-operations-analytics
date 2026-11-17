from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "demandas_sinteticas.csv"
OUTPUT_DIR = ROOT / "outputs"
DATA_REFERENCIA = pd.Timestamp("2026-10-31")


def carregar_dados() -> pd.DataFrame:
    """Carrega a base e converte os campos de data e valor."""
    df = pd.read_csv(DATA_FILE)
    df["data_recebimento"] = pd.to_datetime(df["data_recebimento"], errors="coerce")
    df["data_conclusao"] = pd.to_datetime(df["data_conclusao"], errors="coerce")
    df["data_alvo"] = pd.to_datetime(df["data_alvo"], errors="coerce")
    df["valor_referencial"] = pd.to_numeric(df["valor_referencial"], errors="coerce")
    return df


def validar_dados(df: pd.DataFrame) -> None:
    """Aplica verificações básicas de integridade antes da análise."""
    obrigatorias = {
        "id_demanda", "area", "data_recebimento", "data_conclusao",
        "status", "etapa", "prioridade", "equipe", "data_alvo",
        "valor_referencial",
    }
    faltantes = obrigatorias.difference(df.columns)
    if faltantes:
        raise ValueError(f"Colunas obrigatórias ausentes: {sorted(faltantes)}")
    if df["id_demanda"].isna().any():
        raise ValueError("Há identificadores de demanda vazios.")
    if df["id_demanda"].duplicated().any():
        raise ValueError("Há identificadores de demanda duplicados.")
    if df["data_recebimento"].isna().any() or df["data_alvo"].isna().any():
        raise ValueError("Há datas inválidas nos campos obrigatórios.")
    if (df["data_conclusao"].notna() & (df["data_conclusao"] < df["data_recebimento"])).any():
        raise ValueError("Há conclusão anterior à data de recebimento.")


def calcular_indicadores(df: pd.DataFrame) -> tuple[dict, pd.DataFrame, pd.DataFrame]:
    total = int(df["id_demanda"].nunique())
    concluidas = df[df["status"].eq("concluida")].copy()
    abertas = df[~df["status"].eq("concluida")].copy()

    concluidas["dias_para_conclusao"] = (
        concluidas["data_conclusao"] - concluidas["data_recebimento"]
    ).dt.days
    abertas["em_atraso"] = abertas["data_alvo"] < DATA_REFERENCIA

    indicadores = {
        "data_referencia": DATA_REFERENCIA.strftime("%Y-%m-%d"),
        "total_demandas": total,
        "demandas_concluidas": int(len(concluidas)),
        "demandas_em_aberto": int(len(abertas)),
        "taxa_conclusao_percentual": round(len(concluidas) / total * 100, 1) if total else 0,
        "tempo_medio_conclusao_dias": round(float(concluidas["dias_para_conclusao"].mean()), 1)
        if not concluidas.empty else None,
        "demandas_em_atraso": int(abertas["em_atraso"].sum()),
        "observacao": "Indicadores calculados exclusivamente sobre dados sintéticos."
    }

    por_area = (
        df.groupby("area", as_index=False)
        .agg(total_demandas=("id_demanda", "nunique"))
        .sort_values("total_demandas", ascending=False)
    )
    por_mes = df.assign(mes=df["data_recebimento"].dt.to_period("M").astype(str))
    entradas = por_mes.groupby("mes").size().rename("demandas_recebidas")
    saidas = (
        concluidas.assign(mes=concluidas["data_conclusao"].dt.to_period("M").astype(str))
        .groupby("mes").size().rename("demandas_concluidas")
    )
    fluxo_mensal = pd.concat([entradas, saidas], axis=1).fillna(0).astype(int).reset_index()
    return indicadores, por_area, fluxo_mensal


def gerar_visualizacoes(por_area: pd.DataFrame, fluxo: pd.DataFrame) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    ax = por_area.sort_values("total_demandas").plot(
        kind="barh", x="area", y="total_demandas", legend=False,
        title="Demandas registradas por área"
    )
    ax.set_xlabel("Quantidade de demandas")
    ax.set_ylabel("Área")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "demandas_por_area.png", dpi=160)
    plt.close()

    ax = fluxo.set_index("mes")[["demandas_recebidas", "demandas_concluidas"]].plot(
        marker="o", title="Entradas e conclusões por mês"
    )
    ax.set_xlabel("Mês")
    ax.set_ylabel("Quantidade")
    ax.legend(["Recebidas", "Concluídas"])
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "entrada_vs_conclusao_mensal.png", dpi=160)
    plt.close()


def main() -> None:
    df = carregar_dados()
    validar_dados(df)
    indicadores, por_area, fluxo = calcular_indicadores(df)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "resumo_indicadores.json").write_text(
        json.dumps(indicadores, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    por_area.to_csv(OUTPUT_DIR / "demandas_por_area.csv", index=False)
    fluxo.to_csv(OUTPUT_DIR / "entrada_vs_conclusao_mensal.csv", index=False)
    gerar_visualizacoes(por_area, fluxo)

    print("\nINDICADORES OPERACIONAIS — BASE SINTÉTICA")
    for chave, valor in indicadores.items():
        print(f"{chave}: {valor}")
    print(f"\nArquivos gerados em: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
