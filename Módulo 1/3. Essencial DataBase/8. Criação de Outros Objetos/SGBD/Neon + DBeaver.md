
## 🔷 Passo a passo: criar banco no Neon + conectar no DBeaver (Mac)

### ✅ 1. Criar conta e banco no Neon

1. Acesse [neon.tech](https://neon.tech/) → "Sign up" (grátis)
2. Crie um projeto → escolha região (ex.: São Paulo se tiver)
3. Clique em "Create database" (nome: `estudos_rh_qa`)
4. Anote:
    - **Hostname** (ex.: `ep-cool-name-123456.us-east-2.aws.neon.tech`)
    - **Database name** (ex.: `estudos_rh_qa`)
    - **User** (ex.: `bruno`)
    - **Password** (gerado automaticamente)

### ✅ 2. Instalar DBeaver no Mac

1. Baixe em [dbeaver.io](https://dbeaver.io/download/)
2. Instale (arraste para Applications)
3. Abra o DBeaver

### ✅ 3. Conectar no Neon pelo DBeaver

1. Clique em "New Database Connection" (ícone de plug)
2. Escolha **PostgreSQL**
3. Preencha:
    - Host: `ep-cool-name-123456.us-east-2.aws.neon.tech`
    - Database: `estudos_rh_qa`
    - Username: `bruno`
    - Password: (cole a senha do Neon)
4. Teste conexão → "Finish"

Pronto. Agora você tem um **banco PostgreSQL na nuvem** conectado no seu Mac.

---
## 🔷 Onde encontrar seu HOST no Neon

### ✅ **PASSO 1: Acesse seu projeto no Neon**

1. Entre em [neon.tech](https://neon.tech/)
2. Faça login
3. Clique no seu **projeto** (geralmente tem um nome tipo "My Project")

---

### ✅ **PASSO 2: Vá para "Connection Details"**

Na página do projeto, procure por:

**Opção A** (mais comum):

- Procure um botão ou seção chamada **"Connection Details"**
- Ou **"Connect"** → depois **"Connection Details"**

**Opção B** (se não achar):

- No menu lateral esquerdo, clique em **"Dashboard"**
- Procure por **"Connection string"** ou **"Connect to your database"**

---

### ✅ **PASSO 3: Identifique o HOST**

Você vai ver algo assim:

```
postgresql://bruno:password@ep-cool-name-123456.us-east-2.aws.neon.tech/estudos_rh_qa
```

Ou em formato de lista:

```
Host: ep-cool-name-123456.us-east-2.aws.neon.tech
Database: estudos_rh_qa
User: bruno
Password: ********
```

**Seu HOST é a parte que começa com `ep-`**:

```
ep-cool-name-123456.us-east-2.aws.neon.tech
```

---

### ✅ **PASSO 4: Se não encontrar "Connection Details"**

Às vezes o Neon muda a interface. Tente:

1. **Clique no nome do seu banco** (na lista de databases)
2. Procure por **"Connect"** ou **"Connection string"**
3. Ou vá em **"Settings"** → **"Connection"**

---

### 🔷 **DICA RÁPIDA: Como o HOST se parece**

O HOST do Neon **sempre** tem este formato:

```
ep-XXXXXXXX-YYYYYY.regiao.aws.neon.tech
```

Exemplos reais:

- `ep-winter-sound-123456.us-east-2.aws.neon.tech`
- `ep-silent-brook-789012.eu-central-1.aws.neon.tech`

**É ESSA STRING COMPLETA que você coloca no campo "Host" do DBeaver.**

---

### 🔷 **Se ainda não encontrar:**

Me diga **o que você está vendo** na tela do Neon:

1. Você está na página do projeto?
2. Vê alguma lista de "databases"?
3. Tem algum botão "Connect", "Connection Details" ou "Connection string"?

Ou **me envie uma captura de tela** (se quiser) que eu te mostro exatamente onde clicar.

---
### 🔷 **Extraindo os dados da sua string**

Sua string:

```
postgresql://neondb_owner:npg_pgkE2VJIrez8@ep-fancy-king-acrbfht9-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
```

Vamos decodificar:

|Parte|Valor|
|---|---|
|**Protocolo**|`postgresql://`|
|**Usuário**|`neondb_owner`|
|**Senha**|`npg_pgkE2VJIrez8`|
|**HOST**|`ep-fancy-king-acrbfht9-pooler.sa-east-1.aws.neon.tech`|
|**Database**|`neondb`|
|**Parâmetros extras**|`sslmode=require&channel_binding=require`|

---

## 🔷 **Agora configure no DBeaver**

No DBeaver, na tela de configuração do PostgreSQL:

|Campo|O que colocar|
|---|---|
|**Host**|`ep-fancy-king-acrbfht9-pooler.sa-east-1.aws.neon.tech`|
|**Port**|`5432` (deixe assim)|
|**Database**|`neondb`|
|**Username**|`neondb_owner`|
|**Password**|`npg_pgkE2VJIrez8`|

---

## 🔷 **IMPORTANTE: Configuração extra (SSL)**

Como sua string tem `sslmode=require`, você **precisa** configurar o SSL no DBeaver:

1. Na mesma tela de configuração, vá na aba **"SSL"**
2. Marque **"Use SSL"**
3. Em **"SSL Mode"**, selecione **"require"**
4. Deixe os outros campos em branco (o DBeaver usa certificados padrão)

---

## 🔷 **Passo a passo completo**

1. **Abra DBeaver** → clique no **ícone de plug** (New Database Connection)
2. Escolha **PostgreSQL** → Next
3. Preencha:
    - Host: `ep-fancy-king-acrbfht9-pooler.sa-east-1.aws.neon.tech`
    - Database: `neondb`
    - Username: `neondb_owner`
    - Password: `npg_pgkE2VJIrez8`
4. **Vá na aba SSL**:
    - Marque **"Use SSL"**
    - SSL Mode: **"require"**
5. **Clique em "Test Connection"**
6. Se der **"Connected"**, clique em **"Finish"**

---

## 🔷 **Se der erro no teste**

Os erros mais comuns:

### ❌ **"SSL error"**

- Verifique se marcou **"Use SSL"** e selecionou **"require"**
- Tente também **"verify-full"** (às vezes funciona melhor)

### ❌ **"Authentication failed"**

- Confira se a senha está **exatamente** `npg_pgkE2VJIrez8` (sem espaços)
- Às vezes a senha expira no Neon → gere uma nova no site

### ❌ **"Connection refused"**

- Confira se o HOST está **exatamente** como acima
- Tente sem o `-pooler` (às vezes funciona):
    
    ```
    ep-fancy-king-acrbfht9.sa-east-1.aws.neon.tech
    ```

---

## 🔷 **Pronto para usar**

Depois de conectar, no painel esquerdo do DBeaver você verá:

- **PostgreSQL - neondb** (sua conexão)
- Dentro: **Schemas** → **public** → **Tables** (quando criar)

---
## 🔷 Mini schema de RH + QA para treinar (views, índices, queries)

### ✅ Tabelas (crie no DBeaver, na conexão do Neon)

```sql
-- 1) Candidatos
CREATE TABLE candidatos (
  candidato_id BIGSERIAL PRIMARY KEY,
  nome TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  criado_em TIMESTAMP NOT NULL DEFAULT now()
);

-- 2) Vagas
CREATE TABLE vagas (
  vaga_id BIGSERIAL PRIMARY KEY,
  titulo TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'aberta'
);

-- 3) Entrevistas
CREATE TABLE entrevistas (
  entrevista_id BIGSERIAL PRIMARY KEY,
  candidato_id BIGINT REFERENCES candidatos(candidato_id),
  vaga_id BIGINT REFERENCES vagas(vaga_id),
  etapa TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'agendada',
  data_entrevista TIMESTAMP NOT NULL,
  criado_em TIMESTAMP NOT NULL DEFAULT now()
);

-- 4) Bugs (QA)
CREATE TABLE bugs (
  bug_id BIGSERIAL PRIMARY KEY,
  titulo TEXT NOT NULL,
  severidade TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'aberto',
  build_id TEXT NOT NULL,
  criado_em TIMESTAMP NOT NULL DEFAULT now()
);

-- 5) Execuções de teste (QA)
CREATE TABLE execucoes_teste (
  execucao_id BIGSERIAL PRIMARY KEY,
  build_id TEXT NOT NULL,
  status TEXT NOT NULL,
  duracao_segundos INT,
  criado_em TIMESTAMP NOT NULL DEFAULT now()
);
```

### ✅ Índices (exemplos práticos)

```sql
-- Índice único para email (já criado pelo UNIQUE, mas é bom lembrar)
CREATE UNIQUE INDEX idx_candidatos_email ON candidatos(email);

-- Índice composto para entrevistas (busca por vaga + status)
CREATE INDEX idx_entrevistas_vaga_status ON entrevistas(vaga_id, status);

-- Índice para bugs abertos (parcial)
CREATE INDEX idx_bugs_abertos ON bugs(status) WHERE status = 'aberto';

-- Índice para execuções por build (muito comum em QA)
CREATE INDEX idx_execucoes_build ON execucoes_teste(build_id);
```

### ✅ Views complexas (para treinar)

**View 1: Funil de recrutamento por vaga**

```sql
CREATE OR REPLACE VIEW vw_funil_vaga AS
WITH etapas AS (
  SELECT
    v.vaga_id,
    v.titulo,
    COUNT(DISTINCT c.candidato_id) AS total_candidatos,
    COUNT(DISTINCT CASE WHEN e.etapa = 'entrevista_tecnica' THEN e.candidato_id END) AS entrevistas_tecnicas,
    COUNT(DISTINCT CASE WHEN e.etapa = 'proposta' THEN e.candidato_id END) AS propostas
  FROM vagas v
  LEFT JOIN entrevistas e ON e.vaga_id = v.vaga_id
  LEFT JOIN candidatos c ON c.candidato_id = e.candidato_id
  GROUP BY v.vaga_id, v.titulo
)
SELECT
  *,
  ROUND((entrevistas_tecnicas::DECIMAL / NULLIF(total_candidatos, 0)) * 100, 2) AS taxa_entrevista_tecnica,
  ROUND((propostas::DECIMAL / NULLIF(entrevistas_tecnicas, 0)) * 100, 2) AS taxa_conversao_proposta
FROM etapas;
```

**View 2: Saúde do build (QA)**

```sql
CREATE OR REPLACE VIEW vw_saude_build AS
WITH build_stats AS (
  SELECT
    build_id,
    COUNT(*) AS total_execucoes,
    SUM(CASE WHEN status = 'sucesso' THEN 1 ELSE 0 END) AS sucessos,
    SUM(CASE WHEN status = 'falha' THEN 1 ELSE 0 END) AS falhas,
    AVG(duracao_segundos) AS duracao_media
  FROM execucoes_teste
  GROUP BY build_id
),
bug_stats AS (
  SELECT
    build_id,
    COUNT(*) AS total_bugs,
    SUM(CASE WHEN severidade = 'critico' THEN 1 ELSE 0 END) AS bugs_criticos
  FROM bugs
  GROUP BY build_id
)
SELECT
  b.build_id,
  b.total_execucoes,
  b.sucessos,
  b.falhas,
  b.duracao_media,
  COALESCE(bg.total_bugs, 0) AS total_bugs,
  COALESCE(bg.bugs_criticos, 0) AS bugs_criticos,
  ROUND((b.falhas::DECIMAL / NULLIF(b.total_execucoes, 0)) * 100, 2) AS taxa_falha_percentual
FROM build_stats b
LEFT JOIN bug_stats bg ON bg.build_id = b.build_id;
```

---

## 🔷 Próximos passos (estudo + trabalho)

### ✅ Semana 1–2: Domine o básico no Postgres

- SELECT, WHERE, JOIN, GROUP BY, HAVING
- Crie as tabelas acima e insira dados de exemplo
- Teste as views

### ✅ Semana 3–4: Avançado

- CTEs (WITH)
- Window functions (ROW_NUMBER, RANK, LAG)
- Índices (teste com EXPLAIN ANALYZE)

### ✅ Semana 5–6: Projeto

- Monte um dashboard mental (ou use Metabase/Redash se quiser)
- Replique as views em outro dialeto (MySQL via Docker)