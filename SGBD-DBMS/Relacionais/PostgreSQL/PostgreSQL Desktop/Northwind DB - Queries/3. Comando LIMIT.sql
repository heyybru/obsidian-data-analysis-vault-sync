-- Aula 4:
-- LIMIT:Limitando a quantidade de linhas da query

/*

O `LIMIT` é uma cláusula do SQL que **limita a quantidade de linhas** que uma consulta retorna. 
Em vez de trazer a tabela inteira, você diz ao banco: _"me traz só as primeiras N linhas"_.

Pseudocódigo:
PEGUE customer_id, company_name e country
DA tabela customers
MAS RETORNE apenas as 5 primeiras linhas

*/

-- 1. Selecione a tabela orders
-- 2. Selecione apenas as 100 primeiras linhas da tabela orders

SELECT * FROM orders LIMIT 100;
SELECT * FROM orders LIMIT 10;
SELECT * FROM orders LIMIT 15;

-- 1. `SELECT customer_id, company_name, country` → escolhe as 3 colunas que queremos ver.
SELECT customer_id, company_name, country
-- 2. `FROM customers` → de onde vêm os dados (tabela de clientes).
FROM customers
-- 3. `LIMIT 5` → **retorna no máximo 5 linhas**, mesmo que a tabela tenha 91 clientes.
-- `;` → fim da instrução.
LIMIT 5;