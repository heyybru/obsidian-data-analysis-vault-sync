-- Aula 3: 
-- ALIAS: Renomeando colunas e tabelas com o AS

/*
O `AS` cria um **apelido (alias)** para uma coluna ou tabela no resultado da consulta. 
Traduzindo: você diz ao banco _"pega essa coluna, mas **mostra** ela com esse outro nome"_.

Pseudocódigo:
PEGUE a coluna product_name
MOSTRE no resultado como "nome_do_produto"
DE dentro da tabela products
*/

SELECT
	PRODUCT_NAME AS NOME_DO_PRODUTO -- - Define o **apelido** que será exibido no resultado: `nome_do_produto`.
FROM
	PRODUCTS;

/*
Não é só coluna que ganha apelido — **tabela também**. Isso é essencial para juntar tabelas (Módulo 5, Joins!):

Pseudocódigo:
PEGUE product_name DA tabela products
MOSTRE com o nome "p" para a tabela
USE p. na frente de cada coluna
*/

SELECT 
-- `SELECT p.product_name` → usa `p.` + nome da coluna, deixando explícito _"a coluna product_name da tabela products"_.
    p.product_id AS ID_Produto, 
    p.product_name AS Nome_Produto, 
    p.unit_price AS Preco_Unitario
-- `FROM products AS p` → a tabela `products` ganha o apelido **curto** `p`.
FROM products AS p;