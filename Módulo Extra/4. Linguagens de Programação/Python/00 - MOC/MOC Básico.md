---
tipo: moc
area: python
fase: 2
tags: [moc, python]
atualizado: 2026-11-19
---

# MOC — Básico

## Notas da pasta

```dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  status AS "Status",
  file.mtime AS "Editada"
FROM "02 - Básico"
SORT file.name ASC
```

## Pendentes

```dataview
LIST WITHOUT ID file.link
FROM "02 - Básico"
WHERE status != "concluído"
SORT file.name ASC
```

## Situação da fase

```dataview
TABLE WITHOUT ID
  status AS "Status",
  length(rows) AS "Notas"
FROM "02 - Básico"
GROUP BY status
SORT status ASC
```

Links: [[MOC Trilha Geral]]
