---
tipo: moc
area: python
tags: [moc, python]
atualizado: 2026-11-19
---
# MOC — Trilha Geral

Painel de entrada do vault. Progresso, pendências e atalhos para cada fase.

## Progresso por pasta

​```dataview
TABLE WITHOUT ID
  key AS "Pasta",
  length(rows) AS "Notas",
  length(filter(rows.file.tasks, (t) => t.completed)) AS "Feitas",
  length(filter(rows.file.tasks, (t) => !t.completed)) AS "Abertas"
FROM "01 - Fundamentos" OR "02 - Básico" OR "03 - Intermediário"
  OR "04 - Avançado" OR "05 - Aprofundamento"
  OR "06 - RH e Dados" OR "09 - Big Data"
GROUP BY file.folder
SORT key ASC
​```
## Notas por status

​```dataview
TABLE WITHOUT ID
  status AS "Status",
  length(rows) AS "Quantidade"
FROM "01 - Fundamentos" OR "02 - Básico" OR "03 - Intermediário"
GROUP BY status
SORT status ASC
​```

## Precisam de atenção

​```dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  nivel AS "Nível",
  status AS "Status"
FROM "01 - Fundamentos" OR "02 - Básico" OR "03 - Intermediário"
WHERE status != "concluído"
SORT nivel ASC, file.name ASC
LIMIT 25
​```

## Marcadas para revisar

​```dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  file.mtime AS "Editada"
FROM #revisar
SORT file.mtime DESC
​```

## Editadas nos últimos 7 dias

​```dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  file.mtime AS "Quando"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 15
​```

## Fases de estudo

▸ **Fase 1 — Sintaxe** · 01.01 até 01.16 · semanas 1–3
▸ **Fase 2 — Funções, datas e POO** · 02.01 até 02.18 · semanas 4–6
▸ **Fase 3 — Pandas ETL** · 03.04 até 03.18 · semanas 7–11
▸ **Fase 4 — Visualização** · 03.23 e 03.24 · semanas 12–13
▸ **Fase 5 — Integrações** · 03.27 a 03.32 (escolha 2) · semanas 14–17
▸ **Fase 6 — Feature Engineering** · 03.33 até 03.36 · semana 18
▸ **Fase 7 — Big Data** (opcional) · 09.01 até 09.04

## MOCs das fases

- [[MOC Fundamentos]]
- [[MOC Básico]]
- [[MOC Intermediário]]
- [[MOC Avançado]]
- [[MOC Aprofundamento]]
- [[MOC Projetos]]

## Regras que não podem quebrar

▸ 03.04 → 03.18 é **um projeto único** de ETL. Não leia como notas soltas.
▸ 02.13 → 02.17 (POO) só faz sentido nesta ordem.
▸ **03.35 Outliers vem ANTES de 03.33 Normalização.** Normalizar com outlier distorce a escala.