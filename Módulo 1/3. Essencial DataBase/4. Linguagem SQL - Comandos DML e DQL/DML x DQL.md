### 🔹 O que é DML?

**DML (Data Manipulation Language)**  
São comandos usados para **manipular dados em tabelas**.

👉 Inserir, alterar ,e excluir registros.

### 🔹 O que é DQL?

**DQL (Data Query Language)**  
É usado para **consultar os dados** armazenados no banco.

👉 Recuperar informações.

---

## 🧩 Comandos DML

### 🔹 INSERT – Inserir dados

Usado para adicionar registros em uma tabela.

```sql
INSERT INTO COLABORADOR (id_colaborador, nome, cargo)
VALUES (1, 'Bruno', 'Assistente');
```

---

### 🔹 UPDATE – Alterar dados

Usado para modificar registros existentes.

```sql
UPDATE COLABORADOR
SET cargo = 'Analista'
WHERE id_colaborador = 1;
```

⚠️ **Atenção de prova**:  
Sem `WHERE`, **todos os registros** são alterados.

---

### 🔹 DELETE – Excluir dados

Usado para remover registros.

```sql
DELETE FROM COLABORADOR
WHERE id_colaborador = 1;
```

⚠️ Sem `WHERE`, **todos os registros são apagados** (mas a tabela continua existindo).

---

## 🔎 Comando DQL

### 🔹 SELECT – Consultar dados

Usado para recuperar informações do banco.

```sql
SELECT nome, cargo
FROM COLABORADOR;
```

---

### 🔹 SELECT com WHERE (filtro)

```sql
SELECT *
FROM COLABORADOR
WHERE cargo = 'Analista';
```

---

### 🔹 Operadores comuns no WHERE

- `=` igual
    
- `<>` diferente
    
- `>` maior
    
- `<` menor
    
- `BETWEEN` intervalo
    
- `LIKE` padrão
    
- `IN` lista
    

Exemplo:

```sql
SELECT *
FROM INVENTORY
WHERE price BETWEEN 25 AND 50;
```

---

## 📊 SELECT com funções agregadas

Usadas para **resumos estatísticos**:

- `COUNT()` → contar
    
- `SUM()` → somar
    
- `AVG()` → média
    
- `MIN()` → menor valor
    
- `MAX()` → maior valor
    

```sql
SELECT AVG(price)
FROM INVENTORY;
```

---

## 🧠 Diferença

|Tipo|Para que serve|Exemplos|
|---|---|---|
|DML|Manipular dados|INSERT, UPDATE, DELETE|
|DQL|Consultar dados|SELECT|

---

📌 **Resumo final**

- DML = muda dados
    
- DQL = consulta dados
    
- `SELECT` é o comando mais usado
    
- `WHERE` evita desastre 😅