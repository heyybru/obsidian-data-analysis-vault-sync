-- Módulo PostgreSQL
-- ALIAS: Renomeando colunas e tabelas com o 'AS'

SELECT 
	product_id AS ID_Product, -- mantém o texto em letra miniscula sem formatação desejada
	product_name,
	unit_price
FROM products;	

SELECT 
	product_id AS "ID_Produto", -- "" considera a formatação original do texto - popula em letra maiscula
	product_name AS "Nome_Produto",
	unit_price AS "Preco_Unidade"
FROM products AS p; -- pode renomear nome da tabela de 'products' para 'p' para referenciar de forma melhor

/*
Uma vez que o nome da tabela foi referenciado como 'p', agora permite que ele chame diretamente as colunas.
*/
SELECT 
	p.product_id AS ID_Produto,
	p.product_name AS Nome_Produto,
	p.unit_price AS Preco_Unidade
FROM products AS p;
