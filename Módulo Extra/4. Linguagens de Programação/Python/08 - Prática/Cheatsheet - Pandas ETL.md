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

### **1. E — Extrair**

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
### **2. T — Inspecionar antes de mexer**

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

### **3. T — Limpar colunas e nulos**

```python
df = df.drop(columns=["coluna_inutil"])
df = df.dropna(subset=["Loja"])
df = df.drop_duplicates(subset=["ID_Pedido"], keep="first")
df["Loja"] = df["Loja"].fillna("Online")
```

As quatro técnicas de imputação, e quando cada uma vale:

| Técnica   | Use quando                          | Código                        |
| --------- | ----------------------------------- | ----------------------------- |
| Média     | distribuição simétrica, sem outlier | df[c].fillna(df[c].mean())    |
| Mediana   | há outlier (salário, valor)         | df[c].fillna(df[c].median())  |
| Moda      | variável categórica                 | df[c].fillna(df[c].mode()[0]) |
| Descartar | mais de 30% vazio                   | df.dropna(subset=[c])         |
### **4. T — Tipos e texto**

```python 
df["Data"] = pd.to_datetime(df["Data"], format="%Y-%m-%d")
df["CEP"] = df["CEP"].astype(str)
df["Loja"] = df["Loja"].str.strip().str.title()
df["Email"] = df["Email"].str.lower()
```

format mais usados: %Y-%m-%d (2026-11-19), %d/%m/%Y (19/11/2026), %m-%d-%Y (padrão americano).

Cuidado: %m é mês e %M é minuto. Trocar os dois quebra a conversão silenciosamente.

### **5. T — Criar e transformar colunas**

```python 
df["Faturamento"] = df["Qtd"] * df["Preco_Unitario"]
df["Forma"] = np.where(df["Loja"] == "Online", "Online", "Presencial")
df["Regiao"] = df["Loja"].map({"São Paulo": "Sudeste", "Curitiba": "Sul"})
df["Receita"] = df["Receita"].apply(lambda x: x * 1.1)
df = df.assign(Margem=lambda d: d["Lucro"] / d["Faturamento"])
```

### **6. T — Filtrar e selecionar**

```python 
df["Loja"]                          # Series
df[["Loja", "Cliente"]]             # DataFrame
df.filter(items=["Loja", "Qtd"])    # por nome de coluna
df.filter(like="Vend")              # por parte do nome

df.loc[3, "Loja"]                   # por rótulo
df.iloc[3, 1]                       # por posição
df.set_index("Loja", inplace=True)  # vira índice

cond = df["Faturamento"] > 1000
df[cond]                            # filtro condicional
df[(df["Regiao"] == "Sul") & (df["Qtd"] > 5)]
df[(df["Loja"] == "Online") | (df["Loja"] == "Recife")]
df[df["Data"].dt.year == 2026]
df[df["Data"] >= "2026-01-01"]
```

### **7. T — Ordenar e agrupar**

```python 
df = df.sort_values(by="Data").reset_index(drop=True)
df = df.sort_values(by=["Data", "Faturamento"], ascending=[True, False])

df.groupby("Loja")["Faturamento"].sum()
df.groupby(["Loja", "Produto"])["Faturamento"].sum().reset_index()
df.groupby("Loja").agg(Total=("Faturamento", "sum"), Ticket=("Faturamento", "mean"))
df.nlargest(5, "Faturamento")
```

### **8. T — Juntar bases**

```python 
df_meta = df_meta.merge(df_gerentes, on="Loja", how="left")
df_meta = df_meta.merge(outra, left_on="Loja", right_on="Cidade", how="inner")
```

| how   | Traz o quê              | Quando usar                   |
| ----- | ----------------------- | ----------------------------- |
| inner | só quem existe nos dois | padrão, mas esconde faltantes |
| left  | tudo da esquerda        | **mais seguro para conferir** |
| right | tudo da direita         | raro                          |
| outer | tudo dos dois           | diagnóstico de diferença      |

### **9. T — Série temporal**

```python 
df["Mes"] = df["Data"].dt.to_period("M")
serie = df.groupby("Mes")["Faturamento"].sum()
serie.plot(figsize=(12, 4))

df["Mes"].dt.year
df["Mes"].dt.month
df["Mes"].dt.day
df["Mes"].dt.dayofweek
```

### **10. L — Carregar e exportar**

```python 
df.to_csv("saida.csv", sep=";", index=False, encoding="utf-8-sig")
df.to_excel("saida.xlsx", index=False)
df.to_parquet("saida.parquet")
df.to_sql("tabela", conexao, if_exists="replace", index=False)
```

encoding="utf-8-sig" é o que evita o Excel abrir com acento quebrado.

## Essencial

**Sequência que funciona**

```python 
# 1. carregar
df = pd.read_csv("vendas.csv", sep=";", encoding="latin-1", low_memory=False)

# 2. copiar antes de tratar
df_analise = df.copy()

# 3. inspecionar
df_analise.info()
df_analise.isna().sum()

# 4. limpar
df_analise = df_analise.drop(columns=["Data_Base"])
df_analise["Loja"] = df_analise["Loja"].fillna("Online").str.strip().str.title()
df_analise["Data"] = pd.to_datetime(df_analise["Data"], format="%Y-%m-%d")
df_analise = df_analise.drop_duplicates()

# 5. enriquecer
df_analise["Faturamento"] = df_analise["Qtd"] * df_analise["Preco_Unitario"]

# 6. analisar
ranking = (
    df_analise.groupby("Loja")["Faturamento"]
    .sum()
    .reset_index()
    .sort_values("Faturamento", ascending=False)
)

# 7. exportar
ranking.to_csv("ranking_lojas.csv", index=False)
```

## Pegadinhas

| Erro                           | Causa                | Correção                          |
| ------------------------------ | -------------------- | --------------------------------- |
| Colunas todas grudadas em uma  | separador errado     | sep=";"                           |
| Acento virou símbolo           | encoding errado      | encoding="latin-1"                |
| CEP perdeu o zero inicial      | leu como número      | dtype={"CEP": str}                |
| Data não ordena                | ainda é texto        | pd.to_datetime                    |
| SettingWithCopyWarning         | filtro sem .copy()   | df_filtrado = df[cond].copy()     |
| groupby deu erro               | tentou somar texto   | selecione só as colunas numéricas |
| Duplicata com datas diferentes | linha não é idêntica | drop_duplicates(subset=["ID"])    |
| reset_index() sem efeito       | retornou cópia       | inplace=True ou reatribua         |
| merge perdeu lojas             | inner escondeu       | how="left" para investigar        |
| describe() não mostrou coluna  | dtype é object       | converter antes                   |

## Ver também
- [[0. MOC Trilha Geral]]
