````dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  file.folder AS "Pasta real"
WHERE contains(file.name, "01.01")
````
````dataview
TABLE WITHOUT ID file.link AS "Nota", status AS "Status"
FROM "Python/01 - Fundamentos"
SORT file.name ASC
```` 


