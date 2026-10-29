---
titulo: Tipos de Comandos SQL
modulo: Revisão Geral
data: 2026-10-28
tags:
  - sql
  - postgresql
  - revisao
  - obsidian
---

# Tipos de Comandos SQL

> [!info] Visão geral
> Os comandos SQL se dividem em **5 famílias** (DQL, DML, DDL, DCL, TCL).
> Cada uma tem um papel: ler, manipular, definir, controlar acesso e gerenciar transações.

## 🧩 Analogia da casa

- **DDL** constrói a casa (estrutura)
- **DML** coloca os móveis (dados)
- **DQL** pergunta o que tem (leitura)
- **TCL** é o salvar/desfazer (transações)
- **DCL** decide quem tem a chave (permissões)

---

## 1. DQL — Consultas (ler)

> [!note] O que é
> Linguagem de Consulta de Dados. Serve para **fazer perguntas** ao banco e ver as respostas.

### 1.1 SELECT — comando principal

- **Sintaxe:**
    SELECT colunas FROM tabela;
- **Pseudocódigo:**
    ESCOLHA as colunas DE dentro da tabela
- **Exemplo:**
    SELECT company_name FROM customers;
- **Ver no curso:** [[01-DQL-Consultas/SELECT e FROM|SELECT e FROM]]

### 1.2 Cláusulas do SELECT

- **WHERE** — filtra linhas (ex.: `WHERE country = 'Brazil'`)
- **GROUP BY** — agrupa por coluna (ex.: `GROUP BY country`)
- **HAVING** — filtra grupos (ex.: `HAVING COUNT(*) > 5`)
- **ORDER BY** — ordena (ASC/DESC)
- **LIMIT** — limita a quantidade de linhas
- **DISTINCT** — mostra valores únicos

### 1.3 JOIN — combinar tabelas

- **INNER JOIN** — só o que existe nas duas
- **LEFT JOIN** — tudo da esquerda + o que casar
- **RIGHT JOIN** — tudo da direita + o que casar
- **FULL JOIN** — tudo das duas

### 1.4 Subqueries

- Consulta dentro de consulta (ex.: `SELECT ... WHERE id IN (SELECT ...)`)

---

## 2. DML — Manipulação de dados

> [!warning] Atenção
> **UPDATE e DELETE sem WHERE** afetam a tabela inteira. Sempre confira o filtro antes de executar!

### 2.1 INSERT — adicionar

- **Sintaxe:**
    INSERT INTO tabela (coluna) VALUES (valor);
- **Pseudocódigo:**
    ADICIONE uma linha com estes valores
- **Exemplo:**
    INSERT INTO categories (name) VALUES ('Bebidas');

### 2.2 UPDATE — alterar

- **Sintaxe:**
    UPDATE tabela SET coluna = valor WHERE condição;
- **Pseudocódigo:**
    ALTERE os valores ONDE a condição for verdadeira
- **Exemplo:**
    UPDATE products SET unit_price = 25 WHERE product_id = 1;

### 2.3 DELETE — remover

- **Sintaxe:**
    DELETE FROM tabela WHERE condição;
- **Pseudocódigo:**
    REMOVA as linhas ONDE a condição for verdadeira
- **Exemplo:**
    DELETE FROM products WHERE product_id = 99;

---

## 3. DDL — Definição de estrutura

> [!note] O que é
> Linguagem de Definição de Dados. Cria e destrói a **estrutura** do banco.

### 3.1 CREATE — criar

- **CREATE TABLE** — cria tabela
- **CREATE DATABASE** — cria banco
- **CREATE VIEW** — cria visão
- **CREATE INDEX** — cria índice

### 3.2 ALTER — modificar

- **ADD COLUMN** — adiciona coluna
- **DROP COLUMN** — remove coluna
- **RENAME** — renomeia

### 3.3 DROP — remover estrutura

- **DROP TABLE** — apaga tabela e dados
- **DROP DATABASE** — apaga banco
- **DROP VIEW** — apaga visão

### 3.4 TRUNCATE — esvaziar

- Apaga todas as linhas, **mantém a estrutura**
- Mais rápido que `DELETE` sem `WHERE`

---

## 4. DCL — Controle de acesso

### 4.1 GRANT — dar permissão

- **Sintaxe:**
    GRANT permissão ON objeto TO usuário;
- **Exemplo:**
    GRANT SELECT ON products TO analista;

### 4.2 REVOKE — remover permissão

- **Sintaxe:**
    REVOKE permissão ON objeto FROM usuário;
- **Exemplo:**
    REVOKE DELETE ON products FROM analista;

---

## 5. TCL — Controle de transações

> [!tip] Lembrete
> Transação = conjunto de operações que **ou acontece inteira, ou não acontece**.

- **BEGIN** — inicia a transação
- **COMMIT** — confirma e torna as mudanças permanentes
- **ROLLBACK** — desfaz tudo até o último BEGIN
- **SAVEPOINT** — cria ponto de restauração para desfazer só parte

---

## 📚 Resumo rápido

| Família | O que faz | Comandos |
|---------|-----------|----------|
| DQL | Ler dados | SELECT |
| DML | Mexer no conteúdo | INSERT, UPDATE, DELETE |
| DDL | Criar/destruir estrutura | CREATE, ALTER, DROP, TRUNCATE |
| DCL | Controlar permissões | GRANT, REVOKE |
| TCL | Gerenciar transações | BEGIN, COMMIT, ROLLBACK, SAVEPOINT |
