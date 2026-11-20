---
tipo: moc
area: python
fase: 3
tags: [moc, python]
atualizado: 2026-11-19
---

# MOC — Intermediário

A pasta principal do vault: dados, automação e visualização.

## Notas do nível raiz

```dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  status AS "Status"
FROM "03 - Intermediário"
WHERE file.folder = "03 - Intermediário"
SORT file.name ASC
```

## Feature Engineering

```dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  status AS "Status"
FROM "03 - Intermediário/Feature Engineering"
SORT file.name ASC
```

## Pendentes no nível

```dataview
LIST WITHOUT ID file.link
FROM "03 - Intermediário"
WHERE status != "concluído"
SORT file.name ASC
```

Links: [[MOC Trilha Geral]]
