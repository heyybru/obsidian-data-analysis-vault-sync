-- Aula 5: 
-- DISTINCT: Selecionar os valores distintos de uma coluna

/*

O `DISTINCT` **remove valores repetidos** da coluna que você seleciona. 
Em vez de trazer a lista inteira (com milhares de linhas repetidas), 
ele traz **cada valor diferente uma única vez**.

Pseudocódigo:
PEGUE a coluna country
DA tabela customers
REMOVA os valores repetidos
MOSTRE cada país apenas uma vez

*/

-- 1. Selecione a tabela customers
-- 2. Faça uma consulta que retorne as profissões (contact_title) distintas da tabela customers

 SELECT DISTINCT
    contact_title
 FROM customers;

SELECT DISTINCT 
	country -- `SELECT DISTINCT country` → pega a coluna `country` (país) e **elimina os repetidos**.
FROM customers; -- `FROM customers` → de onde vêm os dados (tabela de clientes).

SELECT DISTINCT country, city
FROM customers;