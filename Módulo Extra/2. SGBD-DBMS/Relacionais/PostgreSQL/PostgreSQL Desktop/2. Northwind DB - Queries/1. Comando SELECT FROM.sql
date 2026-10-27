-- Aula 1: SELECT FROM - Selecionando dados das tabelas

/*
1. O `SELECT` é o comando que diz ao banco: "quero ver os dados". 
Ele é a forma de ler informações guardadas nas tabelas.

2. O `FROM` é o comando que diz **de onde** você quer os dados — ou seja, 
**qual gaveta** (tabela) você vai abrir.

Pseudocódigo:
ESCOLHA as colunas que você quer ver   →  SELECT
DE dentro da tabela onde elas moram    →  FROM
*/

-- Use o `*` (asterisco) para ver todas as colunas de uma tabela. Ele significa "tudo".
FROM CATEGORIES;
SELECT* 

SELECT* -- `SELECT company_name` → "quero ver a coluna **company_name**" (nome da empresa do cliente).
FROM CUSTOMERS; -- `FROM customers` → "de onde? Da tabela **customers**" (clientes).

SELECT first_name FROM employees; -- Para ver uma unica coluna, basta selecionar o nome dela. Sintaxe: SELECT [nome_coluna].

SELECT product_name FROM products;

SELECT product_id, product_name, unit_price FROM products;

SELECT 
    product_id, 
    product_name, 
    unit_price 
FROM products;

-- Aula 2:
-- Comentários no PostgreSQL

-- Este é um comentário de 1 linha
SELECT * FROM orders;

/*

Este

é um comentário

...

de múltiplas linhas

SELECT * FROM products

*/