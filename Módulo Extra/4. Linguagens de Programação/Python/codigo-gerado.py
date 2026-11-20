from pathlib import Path

VAULT = Path("Python-Vault")
HOJE = "2026-11-19"
F = chr(96) * 3          # três crases, evita conflito de bloco
NAO_SOBRESCREVER = True

# ---------- estrutura ----------
ESTRUTURA = {
    "01 - Fundamentos": [
        "01.01 Instalação e ambiente (Python + VS Code + Colab)",
        "01.02 Variáveis, tipos e tipagem dinâmica",
        "01.03 input, print e casting",
        "01.04 Operadores aritméticos, relacionais e lógicos",
        "01.05 Ordem de execução e primeiros erros",
        "01.06 if, elif e else com indentação",
        "01.07 Condicionais encadeadas, ternário e match-case",
        "01.08 Strings - índice, slice e métodos",
        "01.09 Listas - métodos, pilha e fila",
        "01.10 For, for-each e enumerate",
        "01.11 While e loop infinito",
        "01.12 Tuplas e unpacking",
        "01.13 Dicionários",
        "01.14 Sets e iterables",
        "01.15 Lista de listas e matrizes",
        "01.16 Projeto 1 — RPA + pandas",
    ],
    "02 - Básico": [
        "02.01 Funções - def, return e parâmetros",
        "02.02 Argumentos - posição, keyword, args e kwargs",
        "02.03 Funções recursivas",
        "02.04 Docstrings, annotations e built-ins",
        "02.05 try, except e raise",
        "02.06 List comprehension",
        "02.07 Bibliotecas, módulos e variações de import",
        "02.08 time - EPOCH, sleep e medição de tempo",
        "02.09 time - strftime, strptime e locale",
        "02.10 datetime - construtor e timedelta",
        "02.11 datetime - naive, aware e ZoneInfo",
        "02.12 Arquivos - open, modos e close",
        "02.13 Tudo é objeto (intro a OO)",
        "02.14 Classes, atributos e métodos",
        "02.15 __init__ e instanciação",
        "02.16 Encapsulamento - getters e setters",
        "02.17 Herança e classes abstratas",
        "02.18 time, matplotlib e numpy (primeiro contato)",
    ],
    "03 - Intermediário": [
        "03.01 map, filter e lambda",
        "03.02 NumPy - ndarray, shape e reshape",
        "03.03 NumPy - operações, álgebra e aleatórios",
        "03.04 Series e DataFrame",
        "03.05 Pandas ETL - read_csv, encoding, sep e low_memory",
        "03.06 Pandas - inspeção (head, tail, sample, info, describe)",
        "03.07 Pandas - limpeza (drop, dropna, fillna, to_datetime)",
        "03.08 Pandas - texto e padronização (str, strip, title)",
        "03.09 Pandas - duplicatas (subset e keep)",
        "03.10 Pandas - engenharia de colunas (np.where, map, unique)",
        "03.11 Pandas - índices (loc, iloc, set_index, inplace)",
        "03.12 Pandas - seleção e filtros (filter, condicional, e-ou)",
        "03.13 Pandas - ordenação e reset_index",
        "03.14 Pandas - groupby e agg",
        "03.15 Pandas - merge e tipos de join",
        "03.16 Pandas - apply, lambda, nlargest e assign",
        "03.17 Pandas - série temporal (to_period e plot)",
        "03.18 Dados faltantes - qual técnica usar",
        "03.19 Análise Exploratória (EDA) e yfinance",
        "03.20 Excel - pandas versus openpyxl",
        "03.21 Regex no Pandas (str.contains e str.replace)",
        "03.22 Como ler documentações e APIs",
        "03.23 Matplotlib (pyplot e POO)",
        "03.24 Seaborn",
        "03.25 Arquivos txt e PDF (avançado)",
        "03.26 pathlib e shutil",
        "03.27 E-mail - smtplib, Outlook e SendGrid",
        "03.28 SQL - pyodbc, sqlite3 e SQLAlchemy",
        "03.29 Selenium - fundamentos e seleção",
        "03.30 Selenium - formulários, alertas, abas e iframes",
        "03.31 Projeto 2 — Automação Web de preços",
        "03.32 BeautifulSoup",
    ],
    "03 - Intermediário/Feature Engineering": [
        "03.33 Normalização (MinMaxScaler)",
        "03.34 Transformação logarítmica",
        "03.35 Outliers e z-score",
        "03.36 Encoding - get_dummies e drop_first",
    ],
    "04 - Avançado": [
        "04.01 RPA com pyautogui",
        "04.02 Regex",
        "04.03 APIs e JSON",
        "04.04 Finanças - DataReader e rolling",
        "04.05 Ambientes virtuais (conda e venv)",
        "04.06 Integração Power BI",
        "04.07 Gerar executável e agendar tarefas",
    ],
    "05 - Aprofundamento": [
        "05.01 Pytest",
        "05.02 HTML e PyScript",
        "05.03 SpeechRecognition",
        "05.04 OpenCV e MediaPipe",
        "05.05 ArcGIS",
        "05.06 Panorama Python e lógica",
    ],
    "06 - RH e Dados": [
        "06.01 Headcount por área",
        "06.02 Turnover (churn de colaboradores)",
        "06.03 Funil de recrutamento",
        "06.04 Limpeza de base de candidatos",
        "06.05 Relatório semanal automatizado",
        "06.06 Folha e custo por colaborador",
        "06.07 Pipeline ETL de RH",
        "06.08 Coleta automatizada de dados de mercado",
        "06.09 Pipeline de RH orientado a objetos",
        "06.10 Dashboard de headcount",
    ],
    "08 - Prática": [
        "Cheatsheet - Sintaxe",
        "Cheatsheet - Datas e fusos",
        "Cheatsheet - Pandas ETL",
        "Cheatsheet - POO",
        "Erros comuns",
        "Exercícios resolvidos",
    ],
    "09 - Big Data": [
        "09.01 O que é Big Data Analytics",
        "09.02 MapReduce - o paradigma",
        "09.03 reduce com functools",
        "09.04 Do MapReduce ao Pandas",
    ],
    "99 - Fontes": [
        "Apostilas Hashtag - índice por módulo",
        "Descomplica - notas de aula",
        "docs.python.org - links",
    ],
}

NIVEL = {
    "01 - Fundamentos": "fundamentos",
    "02 - Básico": "basico",
    "03 - Intermediário": "intermediario",
    "03 - Intermediário/Feature Engineering": "intermediario",
    "04 - Avançado": "avancado",
    "05 - Aprofundamento": "avancado",
    "06 - RH e Dados": "intermediario",
    "08 - Prática": "pratica",
    "09 - Big Data": "avancado",
    "99 - Fontes": "fonte",
}

# ---------- corpos ----------
def corpo_conceito(titulo, nivel, tag_extra=""):
    tags = f"python, nivel/{nivel}"
    if tag_extra:
        tags += ", " + tag_extra
    return f"""---
tema: {titulo}
nivel: {nivel}
fonte: 
modulo: 
status: não iniciado
tags: [{tags}]
atualizado: {HOJE}
---

# {titulo}

- [ ] Li o conceito
- [ ] Rodei o código
- [ ] Fiz o exemplo de RH
- [ ] Apliquei em dados

## 1. O que é (em uma frase)

## 2. Sintaxe
{F}python
# menor exemplo que roda
{F}

## 3. Pseudo-código
{F}
PASSO 1
PASSO 2
{F}

## 4. Linha a linha
| Linha | O que faz | Por quê |
|---|---|---|
|  |  |  |

## 5. Quando usar

## 6. Quando não usar

## 7. Exemplo RH

## 8. Aplicação em análise de dados

## 9. Erros comuns

## 10. Links
- https://docs.python.org/3/
- https://www.w3schools.com/python/
"""

def corpo_cheatsheet(titulo):
    return f"""---
tipo: cheatsheet
status: não iniciado
tags: [python, cheatsheet]
atualizado: {HOJE}
---

# {titulo}

## Essencial

## Pegadinhas

## Ver também
- [[MOC Trilha Geral]]
"""

def corpo_fonte(titulo):
    return f"""---
tipo: fonte
status: concluído
tags: [fonte]
atualizado: {HOJE}
---

# {titulo}

## O que cobre

## Arquivos relacionados

## Observações
"""

# ---------- MOCs ----------
def moc_padrao(nome, pasta, fase):
    return f"""---
tipo: moc
area: python
fase: {fase}
tags: [moc, python]
atualizado: {HOJE}
---

# MOC — {nome}

## Notas da pasta

{F}dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  status AS "Status",
  file.mtime AS "Editada"
FROM "{pasta}"
SORT file.name ASC
{F}

## Pendentes

{F}dataview
LIST WITHOUT ID file.link
FROM "{pasta}"
WHERE status != "concluído"
SORT file.name ASC
{F}

## Situação da fase

{F}dataview
TABLE WITHOUT ID
  status AS "Status",
  length(rows) AS "Notas"
FROM "{pasta}"
GROUP BY status
SORT status ASC
{F}

Links: [[MOC Trilha Geral]]
"""

MOC_INTERMEDIARIO = f"""---
tipo: moc
area: python
fase: 3
tags: [moc, python]
atualizado: {HOJE}
---

# MOC — Intermediário

A pasta principal do vault: dados, automação e visualização.

## Notas do nível raiz

{F}dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  status AS "Status"
FROM "03 - Intermediário"
WHERE file.folder = "03 - Intermediário"
SORT file.name ASC
{F}

## Feature Engineering

{F}dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  status AS "Status"
FROM "03 - Intermediário/Feature Engineering"
SORT file.name ASC
{F}

## Pendentes no nível

{F}dataview
LIST WITHOUT ID file.link
FROM "03 - Intermediário"
WHERE status != "concluído"
SORT file.name ASC
{F}

Links: [[MOC Trilha Geral]]
"""

MOC_PROJETOS = f"""---
tipo: moc
area: python
fase: pratica
tags: [moc, python, rh]
atualizado: {HOJE}
---

# MOC — Projetos e RH

## Projetos do curso

{F}dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  status AS "Status"
FROM ""
WHERE contains(file.name, "Projeto")
SORT file.name ASC
{F}

## Aplicações de RH por área

{F}dataview
TABLE WITHOUT ID
  key AS "Área de RH",
  length(rows) AS "Notas",
  length(filter(rows.status, (s) => s = "concluído")) AS "Feitas"
FROM "06 - RH e Dados"
GROUP BY area_rh
SORT key ASC
{F}

## Aplicações por tipo de vaga

{F}dataview
TABLE WITHOUT ID
  key AS "Tipo de vaga",
  length(rows) AS "Notas"
FROM "06 - RH e Dados"
WHERE tipo_vaga
GROUP BY tipo_vaga
SORT length(rows) DESC
{F}

## Todas as aplicações de RH

{F}dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  area_rh AS "Área",
  tipo_vaga AS "Vaga",
  status AS "Status"
FROM "06 - RH e Dados"
SORT area_rh ASC, file.name ASC
{F}

## Pendentes de RH

{F}dataview
LIST WITHOUT ID file.link
FROM "06 - RH e Dados"
WHERE status != "concluído"
SORT file.name ASC
{F}

Links: [[MOC Trilha Geral]]
"""

MOC_TRILHA = f"""---
tipo: moc
area: python
tags: [moc, python]
atualizado: {HOJE}
---

# MOC — Trilha Geral

Painel de entrada do vault. Progresso, pendências e atalhos.

## Progresso por pasta

{F}dataview
TABLE WITHOUT ID
  key AS "Pasta",
  length(rows) AS "Notas",
  length(filter(rows.file.tasks, (t) => t.completed)) AS "Feitas",
  length(filter(rows.file.tasks, (t) => !t.completed)) AS "Abertas"
FROM "01 - Fundamentos" OR "02 - Básico" OR "03 - Intermediário" OR "04 - Avançado" OR "05 - Aprofundamento" OR "06 - RH e Dados" OR "09 - Big Data"
GROUP BY file.folder
SORT key ASC
{F}

## Notas por status

{F}dataview
TABLE WITHOUT ID
  status AS "Status",
  length(rows) AS "Quantidade"
FROM "01 - Fundamentos" OR "02 - Básico" OR "03 - Intermediário"
GROUP BY status
SORT status ASC
{F}

## Precisam de atenção

{F}dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  nivel AS "Nível",
  status AS "Status"
FROM "01 - Fundamentos" OR "02 - Básico" OR "03 - Intermediário"
WHERE status != "concluído"
SORT nivel ASC, file.name ASC
LIMIT 25
{F}

## Marcadas para revisar

{F}dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  file.mtime AS "Editada"
FROM #revisar
SORT file.mtime DESC
{F}

## Editadas nos últimos 7 dias

{F}dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  file.mtime AS "Quando"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 15
{F}

## Fases de estudo

- **Fase 1 — Sintaxe** · 01.01 a 01.16 · semanas 1 a 3
- **Fase 2 — Funções, datas e POO** · 02.01 a 02.18 · semanas 4 a 6
- **Fase 3 — Pandas ETL** · 03.04 a 03.18 · semanas 7 a 11
- **Fase 4 — Visualização** · 03.23 e 03.24 · semanas 12 e 13
- **Fase 5 — Integrações** · 03.27 a 03.32 (escolha 2) · semanas 14 a 17
- **Fase 6 — Feature Engineering** · 03.33 a 03.36 · semana 18
- **Fase 7 — Big Data** (opcional) · 09.01 a 09.04

## MOCs das fases

- [[MOC Fundamentos]]
- [[MOC Básico]]
- [[MOC Intermediário]]
- [[MOC Avançado]]
- [[MOC Aprofundamento]]
- [[MOC Projetos]]

## Regras que não podem quebrar

- 03.04 a 03.18 é **um projeto único** de ETL. Não leia como notas soltas.
- 02.13 a 02.17 (POO) só faz sentido nesta ordem.
- **03.35 Outliers vem antes de 03.33 Normalização.** Normalizar com outlier distorce a escala.
"""

# ---------- templates ----------
TPL_CONCEITO = f"""---
tema: 
nivel: fundamentos
fonte: 
modulo: 
status: não iniciado
tags: [python, nivel/fundamentos]
atualizado: {HOJE}
---

# {{{{title}}}}

- [ ] Li o conceito
- [ ] Rodei o código
- [ ] Fiz o exemplo de RH
- [ ] Apliquei em dados

## 1. O que é (em uma frase)

## 2. Sintaxe
{F}python
# menor exemplo que roda
{F}

## 3. Pseudo-código
{F}
PASSO 1
PASSO 2
{F}

## 4. Linha a linha
| Linha | O que faz | Por quê |
|---|---|---|
|  |  |  |

## 5. Quando usar

## 6. Quando não usar

## 7. Exemplo RH

## 8. Aplicação em análise de dados

## 9. Erros comuns

## 10. Links
- https://docs.python.org/3/
- https://www.w3schools.com/python/
"""

TPL_BIBLIOTECA = f"""---
tipo: biblioteca
nome: 
versao: 
instalacao: 
import_padrao: 
status: não iniciado
tags: [python, biblioteca]
atualizado: {HOJE}
---

# {{{{title}}}}

## O que resolve

## Instalação e import

## Métodos que uso com frequência
| Método | Para que serve | Exemplo |
|---|---|---|
|  |  |  |

## Pegadinhas

## Projetos onde usei

## Links oficiais
"""

TPL_LOG = f"""---
tipo: log
semana: 
tags: [log, python]
atualizado: {HOJE}
---

# Log da semana {{{{date:YYYY-[W]ww}}}}

## O que estudei

## O que travou

## Como resolvi

## Próxima semana
"""

# ---------- execução ----------
def escrever(caminho, conteudo):
    caminho.parent.mkdir(parents=True, exist_ok=True)
    if NAO_SOBRESCREVER and caminho.exists():
        return False
    caminho.write_text(conteudo, encoding="utf-8")
    return True

criados = 0
pulados = 0

# notas de estudo
for pasta, notas in ESTRUTURA.items():
    for nome in notas:
        alvo = VAULT / pasta / f"{nome}.md"
        if not alvo.parent.exists():
            alvo.parent.mkdir(parents=True, exist_ok=True)

        if pasta == "08 - Prática":
            corpo = corpo_cheatsheet(nome)
        elif pasta == "99 - Fontes":
            corpo = corpo_fonte(nome)
        else:
            tag = "rh" if pasta == "06 - RH e Dados" else ""
            corpo = corpo_conceito(nome, NIVEL[pasta], tag)

        # frontmatter extra para as notas de RH
        if pasta == "06 - RH e Dados":
            corpo = corpo.replace(
                "status: não iniciado",
                "tipo: aplicacao-rh\narea_rh: \ntipo_vaga: \nstatus: não iniciado",
                1,
            )

        if escrever(alvo, corpo):
            criados += 1
        else:
            pulados += 1

# MOCs
mocs = {
    "MOC Trilha Geral": MOC_TRILHA,
    "MOC Fundamentos": moc_padrao("Fundamentos", "01 - Fundamentos", 1),
    "MOC Básico": moc_padrao("Básico", "02 - Básico", 2),
    "MOC Intermediário": MOC_INTERMEDIARIO,
    "MOC Avançado": moc_padrao("Avançado", "04 - Avançado", 5),
    "MOC Aprofundamento": moc_padrao("Aprofundamento", "05 - Aprofundamento", 6),
    "MOC Projetos": MOC_PROJETOS,
}
for nome, corpo in mocs.items():
    alvo = VAULT / "00 - MOC" / f"{nome}.md"
    if escrever(alvo, corpo):
        criados += 1
    else:
        pulados += 1

# templates
templates = {
    "TPL Conceito": TPL_CONCEITO,
    "TPL Biblioteca": TPL_BIBLIOTECA,
    "TPL Log Semanal": TPL_LOG,
}
for nome, corpo in templates.items():
    alvo = VAULT / "07 - Templates" / f"{nome}.md"
    if escrever(alvo, corpo):
        criados += 1
    else:
        pulados += 1

print(f"Criados: {criados} arquivos")
print(f"Pulados (já existiam): {pulados}")
print(f"Vault em: {VAULT.resolve()}")