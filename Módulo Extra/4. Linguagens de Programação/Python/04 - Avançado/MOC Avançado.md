---
tipo: moc
area: python
fase: "5"
tags:
  - moc
  - python
---

# MOC — Integrações

## Todas as notas da pasta

​```dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  status AS "Status",
  file.mtime AS "Editada"
FROM "01 - Fundamentos"
SORT file.name ASC
​```

## Pendentes

​```dataview
LIST WITHOUT ID file.link
FROM "01 - Fundamentos"
WHERE status != "concluído"
SORT file.name ASC
​```

## Situação geral

​```dataview
TABLE WITHOUT ID
  status AS "Status",
  length(rows) AS "Notas"
FROM "01 - Fundamentos"
GROUP BY status
SORT status ASC
​```

Links: [[MOC Trilha Geral]]
