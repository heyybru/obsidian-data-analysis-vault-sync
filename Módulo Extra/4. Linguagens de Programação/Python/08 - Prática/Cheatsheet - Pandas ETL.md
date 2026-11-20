---
tipo: cheatsheet
status: concluído
tags:
  - python
  - cheatsheet
  - pandas
atualizado: 2026-11-19
---
## Cheatsheet — Pandas ETL

Ordem do pipeline: **E**xtrair → **T**ransformar → **L**oad.

```python
import pandas as pd
import numpy as np
```

**1. E — Extrair**

```python
df = pd.read_csv("dados.csv", sep=";", encoding="latin-1", low_memory=False)
df = pd.read_excel("dados.xlsx", sheet_name="Vendas")
df = pd.read_json("dados.json")
df = pd.read_sql("SELECT * FROM vendas", conexao)
df = pd.read_html("https://site.com/tabela")[0]
```

Parâmetros que resolvem 90% dos problemas de leitura:

| Parâmetro   | Use quando                     | Valor típico                |
| ----------- | ------------------------------ | --------------------------- |
| sep         | colunas vieram grudadas        | ";" para Excel em português |
| encoding    | erro com acento ou ç           | "latin-1" ou "utf-8"        |
| low_memory  | aviso DtypeWarning             | False                       |
| usecols     | base enorme, só quer parte     | ["Loja", "Valor"]           |
| dtype       | CEP ou matrícula virou número  | {"CEP": str}                |
| parse_dates | coluna de data veio como texto | ["Data"]                    |
| skiprows    | cabeçalho começa na linha 3    | skiprows=2                  |
**2. T — Inspecionar antes de mexer**

```python 
df.shape                  # (linhas, colunas) — sem parênteses
df.columns                # nomes das colunas
df.info()                 # tipos, nulos, memória
df.describe()             # estatística das numéricas
df.head(10); df.tail(10)  # pontas
df.sample(10)             # amostra aleatória
df.isna().sum()           # nulos por coluna
df.nunique()              # valores distintos por coluna
```
## Essencial

## Pegadinhas

## Ver também
- [[0. MOC Trilha Geral]]
