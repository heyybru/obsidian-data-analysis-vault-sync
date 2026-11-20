---
tipo: moc
area: python
fase: 1
tags: [moc, python]
atualizado: 2026-11-19
---

# MOC — Fundamentos

## Notas da pasta

```dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  status AS "Status",
  file.mtime AS "Editada"
FROM "01 - Fundamentos"
SORT file.name ASC
```

## Pendentes

```dataview
LIST WITHOUT ID file.link
FROM "01 - Fundamentos"
WHERE status != "concluído"
SORT file.name ASC
```

## Situação da fase

```dataview
TABLE WITHOUT ID
  status AS "Status",
  length(rows) AS "Notas"
FROM "01 - Fundamentos"
GROUP BY status
SORT status ASC
```

Links: [[MOC Trilha Geral]]
