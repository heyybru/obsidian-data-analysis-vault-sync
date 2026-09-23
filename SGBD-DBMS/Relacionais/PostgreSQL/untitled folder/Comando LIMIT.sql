-- Módulo PostgreSQL
-- LIMIT: Limitando a quantidade de linhas das query

/*
1. Selecione a tabela orders
2. Selecione apenas as 100 primeiras linhas da tabela orders
*/
SELECT *
FROM
	ORDERS
LIMIT
	100;

SELECT *
FROM
	ORDERS
LIMIT
	10;