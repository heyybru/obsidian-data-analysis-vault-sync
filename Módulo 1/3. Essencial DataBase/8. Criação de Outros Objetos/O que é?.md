Além de **tabelas**, um SGBD permite criar **outros objetos** que ajudam na organização, desempenho, segurança e automação do banco.

Os principais são:

- **VIEW (Visão)**
    
- **SEQUENCE (Sequência)**
    
- **INDEX (Índice)**
    
- **SYNONYM (Sinônimo)**
    
- **TRIGGER (Gatilho)** _(visão introdutória)_

---

## 🔹 VIEW (Visão)

### 📌 O que é?

Uma **view** é uma **tabela virtual**, criada a partir de uma consulta `SELECT`.

- Não armazena dados
    
- Mostra dados das tabelas reais
    
- Facilita consultas
    
- Ajuda na segurança (mostra só o que precisa)

### 🧠 Exemplo

```sql
CREATE VIEW vw_colaboradores AS
SELECT id_colaborador, nome, cargo
FROM colaborador;
```

📌 Uso:

```sql
SELECT * FROM vw_colaboradores;
```

---

## 🔹 SEQUENCE (Sequência)

### 📌 O que é?

Objeto usado para **gerar números automáticos**, muito comum para **PK**.

### 🧠 Exemplo

```sql
CREATE SEQUENCE seq_colaborador
START WITH 1
INCREMENT BY 1;
```

📌 Uso:

```sql
seq_colaborador.NEXTVAL
```

---

## 🔹 INDEX (Índice)

### 📌 O que é?

Melhora o **desempenho das consultas**.

- Acelera `SELECT`
    
- Muito usado em PK e FK
    
- Pode deixar `INSERT` um pouco mais lento

### 🧠 Exemplo

```sql
CREATE INDEX idx_colab_nome
ON colaborador(nome);
```

---

## 🔹 SYNONYM (Sinônimo)

### 📌 O que é?

Um **apelido** para um objeto do banco.

- Facilita o acesso
    
- Muito usado quando a tabela está em outro schema

### 🧠 Exemplo

```sql
CREATE SYNONYM colab FOR colaborador;
```

📌 Uso:

```sql
SELECT * FROM colab;
```

---

## 🔹 TRIGGER (Introdução)

### 📌 O que é?

Código que executa **automaticamente** quando ocorre um evento:

- `INSERT`
    
- `UPDATE`
    
- `DELETE`

### 🧠 Exemplo simples

```sql
CREATE TRIGGER trg_log
BEFORE INSERT ON colaborador
FOR EACH ROW
BEGIN
  -- ação automática
END;
```

📌 Muito usado para:

- Auditoria
    
- Validações
    
- Regras automáticas

---

## 🧠 Resumo

|Objeto|Para que serve|
|---|---|
|VIEW|Consulta salva|
|SEQUENCE|Gerar números|
|INDEX|Melhorar performance|
|SYNONYM|Criar apelidos|
|TRIGGER|Executar ações automáticas|
