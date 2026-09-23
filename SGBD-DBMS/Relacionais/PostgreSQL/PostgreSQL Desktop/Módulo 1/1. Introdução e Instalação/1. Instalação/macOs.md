[download](https://www.postgresql.org/download/macosx/)
## 🖥️ 1. Verificação prévia de compatibilidade

**Contexto de 2026:** o macOS atual é o **26 "Tahoe"** (26.6.x em set/2026). O PostgreSQL 18 suporta macOS 13 ou superior (Apple Silicon e Intel). Ou seja: **seu Mac roda sem problema**.

**Versão do PostgreSQL:** a estável atual é a **18** (18.6, de ago/2026). A versão **19 está em beta** — não instale beta para aprender.

👉 **Como confirmar antes de continuar** (abre o Terminal com `Cmd + Espaço` → digite "Terminal"):

```bash
sw_vers          # mostra a versão do macOS
uname -m         # deve retornar: arm64 (Apple Silicon)
psql --version   # mostra se já existe algo instalado
```

✅ Se `uname -m` retornar `arm64` e o macOS for 13 ou superior, pode seguir tranquilo.

---

## ⚖️ 2. Opções de instalação disponíveis em 2026

O comparativo abaixo resume as quatro formas mais usadas. Depois dele, o passo a passo dos **dois caminhos que valem a pena**:

- **Mais simples** → EDB Interactive Installer (interface gráfica)
- **Mais recomendada (profissional)** → Homebrew (terminal)

---

## 📦 3. Passo a passo da instalação

### 🟢 Caminho A — EDB Installer (o mais simples para iniciantes)

1. Acesse o site oficial: [postgresql.org/download/macosx](https://www.postgresql.org/download/macosx)
2. Baixe o **Interactive Installer** do **PostgreSQL 18** (o site detecta Apple Silicon automaticamente).
3. Abra o arquivo `.dmg` baixado e execute o instalador.
4. No assistente, marque os componentes: **PostgreSQL Server** e **pgAdmin 4** (interface gráfica).
5. Defina a **senha do superusuário `postgres`** — **anote e guarde**.
6. Mantenha a **porta padrão 5432**.
7. No `Locale`, **mantenha o padrão** sugerido.
8. Conclua a instalação. O serviço **inicia sozinho**.

### 🔵 Caminho B — Homebrew (o mais recomendado e profissional)

1. Abra o **Terminal**.
2. Verifique se o Homebrew já está instalado:
    
    ```bash
    brew --version
    ```
    
    Se **não** aparecer versão, instale o Homebrew com o comando oficial (copie e cole, siga as instruções na tela):
    
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    
3. Atualize o Homebrew:
    
    ```bash
    brew update
    ```
    
4. Instale o PostgreSQL 18:
    
    ```bash
    brew install postgresql@18
    ```
    
    > 💡 Se o comando disser que a fórmula não existe, use `brew install postgresql` (instala a versão estável atual). O Homebrew já cria o banco padrão automaticamente.
    
5. Adicione o PostgreSQL ao PATH (Apple Silicon usa a pasta `/opt/homebrew`):
    
    ```bash
    echo 'export PATH="/opt/homebrew/opt/postgresql@18/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```
    
6. Inicie o serviço:
    
    ```bash
    brew services start postgresql@18
    ```
    
7. Confirme que instalou:
    
    ```bash
    psql --version
    pg_isready
    ```
    

✅ Se `pg_isready` responder `accepting connections`, está tudo certo.

---

## ▶️ 4. Iniciar, parar e verificar se está funcionando

**Se você usou o Homebrew:**

```bash
brew services start postgresql@18     # iniciar
       # parar
brew services restart postgresql@18   # reiniciar
brew services list                    # ver se está "started"
```

**Se você usou o EDB:** o serviço sobe automaticamente com o Mac. Para parar, o mais fácil é usar o **pgAdmin** (botão Stop) — ou, no Terminal, o `pg_ctl` apontando para a pasta de dados `.../PostgreSQL/18/data`.

**Verificação universal (os dois casos):**

```bash
pg_isready        # "accepting connections" = servidor no ar
psql --version    # confirma a versão instalada
```

---

## 💻 5. Como acessar o banco pelo terminal

**Homebrew** (você entra como seu próprio usuário do Mac, sem senha):

```bash
psql postgres
```

**EDB** (você entra como o usuário `postgres`, com a senha que definiu):

```bash
psql -U postgres -h localhost
```

**Dentro do `psql`, os comandos essenciais:**

|Comando|O que faz|
|---|---|
|`\l`|lista os bancos de dados|
|`\du`|lista os usuários (roles)|
|`\c nome_do_banco`|conecta a um banco|
|`\q`|sai do psql|

---

## 🔐 6. Configurar usuário, senha e criar banco

Já conectado ao `psql`, rode um comando por vez (exemplo com tema de RH, a sua praia 😉):

```sql
-- 1) criar um usuário com senha
CREATE USER bruno WITH PASSWORD 'uma_senha_forte_aqui';

-- 2) criar um banco de dados e dar a posse ao usuário
CREATE DATABASE rh_analytics OWNER bruno;
```

**Boas práticas já aqui:** use o **superusuário apenas para administração**. Para o dia a dia, crie um usuário dedicado (como o `bruno` acima) e conecte com ele:

```bash
psql -U bruno -d rh_analytics -h localhost
```

**Trocar a senha depois:**

```sql
ALTER USER bruno WITH PASSWORD 'nova_senha_aqui';
```

---

## 🛠️ 7. Problemas comuns e como resolver

1. **`psql: command not found`** → o PATH não foi configurado. Rode de novo a linha do `export ... >> ~/.zshrc` e depois `source ~/.zshrc` (passo 5 do Caminho B).
2. **`could not connect to server: Connection refused`** → o serviço está parado. Suba com `brew services start postgresql@18`.
3. **`role "bruno" does not exist`** → o usuário ainda não foi criado. Execute o `CREATE USER` da seção 6.
4. **`password authentication failed`** → senha incorreta. Conectado como seu usuário do Mac, redefina: `ALTER USER postgres WITH PASSWORD 'nova_senha';`
5. **Porta 5432 ocupada** → descubra quem está usando com `lsof -i :5432`; pare o outro serviço ou escolha outra porta.
6. **`brew services list` mostra "error"** → veja os detalhes com `brew services info postgresql@18` (geralmente é permissão na pasta de dados).
7. **Depois de atualizar o macOS, parou de funcionar** → rode `brew services restart postgresql@18`.

⚠️ **Dica de diagnóstico:** na dúvida, comece sempre por `pg_isready`. Se ele diz "accepting connections", o problema é de **acesso/autenticação** — não do servidor.

---

## ✅ 8. Boas práticas básicas após a instalação

1. **Senha forte** para o superusuário e **um usuário por projeto** (princípio do menor privilégio).
2. **Não use o superusuário `postgres` em aplicações** — só para administrar.
3. **Backup regular:** `pg_dump rh_analytics > backup.sql` (restaurar: `psql rh_analytics < backup.sql`).
4. **Mantenha atualizado:** `brew upgrade postgresql@18` corrige falhas de segurança.
5. **Por padrão, o PostgreSQL só escuta em `localhost`** — mantenha assim para estudos (mais seguro).
6. **Anote a pasta de dados** (Homebrew: `/opt/homebrew/var/postgresql@18`) — ela guarda seus bancos.
7. **Prefere interface gráfica?** Use o **pgAdmin 4** (vem no EDB) ou o **DBeaver** (funciona com Homebrew também).