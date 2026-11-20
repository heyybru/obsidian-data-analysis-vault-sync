---
tipo: moc
area: python
fase: "3"
tags:
  - moc
  - python
---

# MOC — Pandas ETL

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
FROM "03 - Intermediário"
WHERE status != "concluído"
SORT file.name ASC
​```

## Situação geral

​```dataview
TABLE WITHOUT ID
  status AS "Status",
  length(rows) AS "Notas"
FROM "03 - Intermediário"
GROUP BY status
SORT status ASC
​```

## Feature Engineering

​```dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  status AS "Status"
FROM "03 - Intermediário/Feature Engineering"
SORT file.name ASC
​```

Links: [[MOC Trilha Geral]]
