-- Módulo PostgreSQL
-- DISTINCT: Selecionar os valores distintos de uma coluna
/*
1. Selecione a tabela 'customers'
2. Faça uma consulta que retorne as profissøes (contact_title) distintas/unicas da tabela customers
*/
SELECT
	DISTINCT CONTACT_TITLE 
FROM
	CUSTOMERS;