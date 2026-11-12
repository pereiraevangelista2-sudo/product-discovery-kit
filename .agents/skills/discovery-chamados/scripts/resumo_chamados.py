#!/usr/bin/env python3
"""Resumo quantitativo de chamados de suporte para a Etapa 4 do discovery.

Lê uma exportação (.xlsx, .xls ou .csv), aplica filtros de escopo e gera um
resumo em Markdown com contagens, tempos de resolução e SLA. Não reproduz
descrições nem dados pessoais: só contagens e estatísticas.

Exemplo:
  python resumo_chamados.py chamados.xlsx \
    --col-data "Aberto em" --col-fechamento "Resolvido em" \
    --col-tipo "Tipo" --col-categoria "Serviço" --col-cliente "Cliente" \
    --col-sla "Dentro do SLA" --col-tema "Tema" \
    --filtro "Serviço=Módulo X" --excluir-tipo "Melhoria" --saida resumo.md

--filtro pode ser repetido (todas as condições valem). Use "Coluna~texto"
para "contém" (sem diferenciar maiúsculas) e "Coluna=valor" para igualdade.
"""
import argparse
import sys

import pandas as pd


def ler(caminho, aba):
    if caminho.lower().endswith(".csv"):
        for enc in ("utf-8", "utf-8-sig", "latin-1"):
            try:
                return pd.read_csv(caminho, sep=None, engine="python", encoding=enc)
            except UnicodeDecodeError:
                continue
        raise SystemExit("Não foi possível ler o CSV (codificação).")
    return pd.read_excel(caminho, sheet_name=aba or 0)


def aplicar_filtros(df, filtros):
    for f in filtros or []:
        if "~" in f:
            col, val = f.split("~", 1)
            df = df[df[col].astype(str).str.contains(val, case=False, na=False, regex=False)]
        elif "=" in f:
            col, val = f.split("=", 1)
            df = df[df[col].astype(str).str.strip() == val.strip()]
        else:
            raise SystemExit(f"Filtro inválido: {f}")
    return df


def tabela(serie, titulo, total):
    cont = serie.fillna("(vazio)").astype(str).value_counts()
    linhas = [f"### {titulo}", "", "| Valor | Chamados | % |", "|---|---|---|"]
    for k, v in cont.items():
        linhas.append(f"| {k} | {v} | {v / total:.0%} |")
    return "\n".join(linhas) + "\n"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("arquivo")
    p.add_argument("--aba", help="Nome da aba (Excel)")
    p.add_argument("--col-data", required=True, help="Coluna de data de abertura")
    p.add_argument("--col-fechamento", help="Coluna de data de resolução")
    p.add_argument("--col-tipo")
    p.add_argument("--col-categoria")
    p.add_argument("--col-situacao")
    p.add_argument("--col-urgencia")
    p.add_argument("--col-cliente", help="Empresa-cliente (só aparece no top 10; não use em material externo)")
    p.add_argument("--col-sla", help="Coluna com indicação de SLA cumprido (sim/não, true/false)")
    p.add_argument("--col-tema", help="Coluna de tema já classificado")
    p.add_argument("--filtro", action="append", help="Coluna=valor ou Coluna~texto (repetível)")
    p.add_argument("--excluir-tipo", action="append", help="Tipos excluídos do cálculo de tempo (ex.: Melhoria)")
    p.add_argument("--saida", help="Arquivo .md de saída (padrão: tela)")
    a = p.parse_args()

    bruto = ler(a.arquivo, a.aba)
    total_bruto = len(bruto)
    df = aplicar_filtros(bruto.copy(), a.filtro)
    n = len(df)
    if n == 0:
        raise SystemExit("Nenhum chamado depois dos filtros. Confira nomes de colunas e valores.")

    df["_abertura"] = pd.to_datetime(df[a.col_data], errors="coerce", dayfirst=True)
    datas_invalidas = int(df["_abertura"].isna().sum())
    df["_ano"] = df["_abertura"].dt.year
    df["_mes"] = df["_abertura"].dt.to_period("M")

    out = ["# Resumo de chamados (gerado por script)", ""]
    out.append(f"- Arquivo: {a.arquivo}")
    out.append(f"- Linhas na base: {total_bruto}")
    out.append(f"- Filtros: {a.filtro or 'nenhum'}")
    out.append(f"- Chamados no escopo: {n}")
    out.append(f"- Período: {df['_abertura'].min():%d/%m/%Y} a {df['_abertura'].max():%d/%m/%Y}")
    if datas_invalidas:
        out.append(f"- Atenção: {datas_invalidas} chamados sem data de abertura válida")
    out.append("")

    out.append(tabela(df["_ano"].astype("Int64"), "Por ano de abertura", n))
    por_mes = df.groupby("_mes").size()
    out.append("### Por mês (verifique meses vazios ou cortes de exportação)\n")
    out.append("| Mês | Chamados |\n|---|---|")
    out.extend(f"| {m} | {v} |" for m, v in por_mes.items())
    out.append("")

    for col, titulo in [(a.col_tipo, "Por tipo"), (a.col_categoria, "Por serviço ou categoria"),
                        (a.col_situacao, "Por situação"), (a.col_urgencia, "Por urgência"),
                        (a.col_tema, "Por tema")]:
        if col:
            out.append(tabela(df[col], titulo, n))

    if a.col_fechamento:
        base = df
        if a.excluir_tipo and a.col_tipo:
            base = df[~df[a.col_tipo].astype(str).isin(a.excluir_tipo)]
        fim = pd.to_datetime(base[a.col_fechamento], errors="coerce", dayfirst=True)
        dias = (fim - base["_abertura"]).dt.total_seconds() / 86400
        dias = dias.dropna()
        dias = dias[dias >= 0]
        out.append("### Tempo até resolução (dias corridos)\n")
        out.append(f"Base: {len(dias)} chamados resolvidos" + (f", sem {a.excluir_tipo}" if a.excluir_tipo else "") + ".\n")
        if len(dias):
            out.append("| Recorte | Mediana | P75 | P90 |\n|---|---|---|---|")
            out.append(f"| Geral | {dias.median():.1f} | {dias.quantile(.75):.1f} | {dias.quantile(.9):.1f} |")
            anos = base.loc[dias.index, "_ano"]
            for ano, grupo in dias.groupby(anos):
                out.append(f"| {int(ano)} | {grupo.median():.1f} | {grupo.quantile(.75):.1f} | {grupo.quantile(.9):.1f} |")
            out.append("")

    if a.col_sla:
        s = df[a.col_sla].astype(str).str.strip().str.lower()
        dentro = s.isin(["sim", "s", "true", "1", "yes", "dentro"])
        fora = s.isin(["não", "nao", "n", "false", "0", "no", "fora"])
        out.append("### SLA\n")
        out.append("| Ano | Dentro | Fora | % fora |\n|---|---|---|---|")
        for ano in sorted(df["_ano"].dropna().unique()):
            m = df["_ano"] == ano
            d, f = int((dentro & m).sum()), int((fora & m).sum())
            pct = f / (d + f) if d + f else 0
            out.append(f"| {int(ano)} | {d} | {f} | {pct:.0%} |")
        out.append("")

    if a.col_cliente:
        out.append("### Top 10 empresas por volume (uso interno; não citar em material externo)\n")
        top = df[a.col_cliente].fillna("(vazio)").astype(str).value_counts().head(10)
        out.append("| Empresa | Chamados | % |\n|---|---|---|")
        out.extend(f"| {k} | {v} | {v / n:.0%} |" for k, v in top.items())
        out.append("")

    texto = "\n".join(out)
    if a.saida:
        with open(a.saida, "w", encoding="utf-8") as fh:
            fh.write(texto)
        print(f"Resumo salvo em {a.saida}")
    else:
        sys.stdout.write(texto)


if __name__ == "__main__":
    main()
