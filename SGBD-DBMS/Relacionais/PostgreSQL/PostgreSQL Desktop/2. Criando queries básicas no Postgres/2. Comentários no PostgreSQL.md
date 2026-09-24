## 💬 O que são comentários no PostgreSQL?

Comentários são **anotações que você escreve dentro do código SQL, mas que o banco de dados ignora completamente**. Eles não são executados — servem só para quem está lendo o código.

Pense assim: é como um **bilhete colado no código**. O banco passa direto por ele, mas a pessoa que lê depois entende o que estava acontecendo ali.

```sql
-- Esta consulta retorna todos os clientes cadastrados
SELECT *
FROM customers;
```

A linha com `--` não faz nada no banco. Ela só explica. ✅

## 🎯 Para que servem e quando usar?

Os comentários servem para:

- **Explicar** o que uma consulta faz (ex.: "retorna os pedidos de 2025").
- **Documentar** decisões (ex.: "usamos LEFT JOIN porque queremos clientes sem pedidos também").
- **Organizar** o código em blocos, facilitando a leitura.
- **Ajudar outras pessoas** — e você mesmo no futuro — a entender rapidinho o que foi feito.

A regra prática: **comente quando o código não for óbvio**. Em consultas simples, um comentário curto já resolve. Em consultas complexas (joins, subqueries), comentar é quase obrigatório.

## 📝 Comentário de linha: `--`

O comentário de linha começa com **duas barras** `--` e vale **até o fim da linha**.

```sql
-- Lista os produtos da categoria 1
SELECT product_name
FROM products
WHERE category_id = 1;
```

Ele também pode aparecer **no final de uma linha de código**:

```sql
SELECT product_name
FROM products
WHERE unit_price > 20;  -- só produtos caros
```

> 👉 O `--` funciona como um "post-it": anota aquele trecho e não interfere em nada.

## 📦 Comentário de bloco: `/* */`

O comentário de bloco começa com `/*` e termina com `*/`. Ele pode ocupar **várias linhas**.

```sql
/*
Esta consulta retorna os produtos
e o preço de cada um.
Criada em setembro de 2026.
*/
SELECT product_name, unit_price
FROM products;
```

Quando usar o de bloco?

- Para **explicações longas** (várias linhas de contexto).
- Para **"desligar" temporariamente** um trecho de código sem apagá-lo — basta envolvê-lo em `/* */` e ele deixa de executar. Útil para testes!

## 🧠 Exemplo prático completo

```sql
-- Consulta: clientes do Brasil
/*
Objetivo: listar os clientes brasileiros
para a análise de vendas da região.
*/
SELECT company_name, city
FROM customers
WHERE country = 'Brazil';  -- filtro por país
```

Nesse exemplo, o `--` explica o objetivo, o bloco `/* */` traz o contexto, e o comentário no final da linha detalha o filtro. O banco executa **apenas** a linha `SELECT ... WHERE ...`.

## Resumo prático

- Comentários são **anotações ignoradas pelo banco** — servem para quem lê o código.
- `--` comenta **uma linha**; `/* */` comenta **várias linhas**.
- Use para **explicar, documentar e organizar** suas consultas.
- Comentários não mudam o resultado — só deixam o código mais claro. 🎯