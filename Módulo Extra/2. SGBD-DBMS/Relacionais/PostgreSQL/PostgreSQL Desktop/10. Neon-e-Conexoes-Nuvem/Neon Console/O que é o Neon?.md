[neon-console](https://console.neon.tech/app/projects/orange-moon-89252708/branches/br-purple-paper-b6t6wc9k)

## 1. O que é o Neon? (explicação simples)

O que é: um serviço que hospeda bancos PostgreSQL na nuvem, com plano gratuito e sem cartão de crédito.

Para que serve: deixa seu banco acessível pela internet — algo que o `localhost` (sua máquina) não consegue. É isso que permite o Google Sheets conversar com o Northwind.

Quando usar:

- Quando precisar conectar ferramentas de nuvem (Sheets, BI, apps) ao banco
- Para praticar SQL de qualquer lugar, sem depender do seu computador
- Quando não quiser gerenciar servidor (o Neon escala e "dorme" sozinho)

Quando não usar: para estudos só locais — aí o PostgreSQL local + plugin do Obsidian resolve sem nuvem.

---

## 2. Bloco pronto para planilha ou documento

### 📋 Dados de conexão (Neon)

|Parâmetro|Valor|Onde encontrar|
|---|---|---|
|Host|`ep-xxxx.us-east-2.aws.neon.tech`|Connection string do projeto|
|Port|`5432`|Padrão PostgreSQL|
|Database|`northwind`|Definido na criação do projeto|
|User|`neondb_owner`|Connection string do projeto|
|Password|(a senha gerada)|Connection string do projeto|
|SSL|`True`|Obrigatório no Neon|

Connection string (formato):

postgresql://neondb_owner:SENHA@ep-xxxx.us-east-2.aws.neon.tech/northwind

### 🚀 Passos para criar o banco na nuvem

|Passo|Ação|Detalhe|
|---|---|---|
|1|Criar conta no [neon.com](https://neon.com/)|Cadastro com e-mail, GitHub ou Google|
|2|Criar projeto|Nome: `curso-postgres` · Database: `northwind`|
|3|Copiar a connection string|Ela só aparece uma vez — guarde!|
|4|Exportar o Northwind local|`pg_dump -U postgres -h localhost -d northwind --no-owner -f northwind.sql`|
|5|Importar no Neon|`psql "CONNECTION_STRING" -f northwind.sql`|
|6|Verificar|`\dt` e `SELECT COUNT(*) FROM customers;` (esperado: 91)|

### 🔌 Conexão no Google Sheets (SyncWith)

|Campo|Valor|
|---|---|
|Host|`ep-xxxx.us-east-2.aws.neon.tech`|
|Port|`5432`|
|Database|`northwind`|
|Username|`neondb_owner`|
|Password|(senha da connection string)|
|SSL Enabled|`True`|

### ⚠️ Erros comuns e soluções

|Erro|Causa|Solução|
|---|---|---|
|`No DNS records found for host: localhost`|Conector na nuvem não enxerga sua máquina|Usar banco na nuvem (Neon) ou túnel ngrok|
|Conexão recusada|Senha/SSL errados|Conferir connection string e ativar SSL|
|Tabelas não aparecem|Importação falhou|Rodar de novo com `--no-owner` e conferir o banco certo|
|Banco "dormindo"|Neon escala a zero após inatividade|Esperar alguns segundos; ele acorda sozinho|
