[download](https://www.postgresql.org/download/)
### 1. Pré-requisitos

Antes de instalar, confira estes pontos:

- **Sistema operacional**: Windows 10/11 (64 bits), macOS 11 ou superior, ou Linux (Ubuntu/Debian, Fedora/RHEL, etc.).
- **Acesso de administrador**: necessário para instalar software. No Linux, isso significa ter permissão de `sudo`.
- **Espaço em disco**: cerca de 1 GB livres (a instalação básica é leve; os dados crescem com o uso).
- **Memória**: 2 GB de RAM são suficientes para estudo e uso comum.
- **Porta 5432 livre**: é a porta padrão do PostgreSQL. Se estiver ocupada, o instalador permite trocar.
- **Acesso à internet**: para baixar o instalador ou os pacotes.
- **Decisão de versão**: use a mais recente estável (18.x). Em ambientes de trabalho, mantenha a mesma versão entre desenvolvimento e produção.

### 2. Métodos de instalação

| Método                                      | Sistema          | Complexidade | Quando usar                                                       |
| ------------------------------------------- | ---------------- | ------------ | ----------------------------------------------------------------- |
| Instalador oficial (EDB)                    | Windows e macOS  | Baixa        | Recomendado para iniciantes; inclui pgAdmin 4 e interface gráfica |
| Gerenciador de pacotes (apt, dnf, Homebrew) | Linux e macOS    | Média        | Quem prefere linha de comando e integração nativa com o sistema   |
| Docker                                      | Qualquer sistema | Média        | Ambientes isolados, testes e reprodução de configuração           |
| Compilação do código-fonte                  | Qualquer sistema | Alta         | Customização avançada; raramente necessária                       |

A tabela acima resume os quatro caminhos possíveis. Para quem está começando (como no nosso curso), o **instalador oficial (EDB)** é o mais indicado no Windows e macOS. No Linux, o caminho natural é o **gerenciador de pacotes**, pois a EDB não fornece mais instaladores Linux para versões 11+ — a recomendação oficial é usar os pacotes nativos do sistema.

### 3. Instalação no Windows (instalador oficial)

1. Acesse a página oficial de downloads: [postgresql.org/download](https://www.postgresql.org/download/).
2. Escolha a versão **18.x** e o instalador para **Windows x86-64**.
3. Execute o arquivo `.exe` baixado e clique em **Next** até aceitar os termos de licença.
4. **Selecione os componentes**: mantenha marcados _PostgreSQL Server_, _pgAdmin 4_ e _Command Line Tools_. O _Stack Builder_ é opcional (instala drivers e extensões extras).
5. **Defina os diretórios**: o local de instalação (ex.: `C:\Program Files\PostgreSQL\18`) e o diretório de dados (ex.: `C:\Program Files\PostgreSQL\18\data`).
6. **Crie a senha do superusuário `postgres`**: anote e guarde essa senha com segurança — ela será usada em todas as conexões.
7. **Mantenha a porta 5432** (padrão) e escolha o _locale_ (ex.: _Portuguese, Brazil_).
8. Revise o resumo e clique em **Next** para concluir a instalação.
9. Abra o **pgAdmin 4** pelo menu Iniciar e conecte no servidor local com o usuário `postgres` e a senha definida.

### 4. Instalação no macOS e Linux

**macOS (Homebrew):**

```bash
brew update
brew install postgresql@18
brew services start postgresql@18
```

- `brew update` atualiza a lista de pacotes do Homebrew.
- `brew install postgresql@18` instala o PostgreSQL 18.
- `brew services start postgresql@18` inicia o servidor e o mantém rodando em segundo plano.

**Ubuntu/Debian (apt):**

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl enable --now postgresql
```

- `postgresql-contrib` adiciona extensões e funções extras.
- `systemctl enable --now postgresql` ativa o serviço e o inicia agora.

No Linux, a instalação cria automaticamente um superusuário chamado `postgres`. Para acessar o console:

```bash
sudo -i -u postgres
psql
```

### 5. Instalação via Docker (opcional)

Útil para criar um ambiente isolado e reproduzível:

```bash
docker run --name meu-postgres \
  -e POSTGRES_PASSWORD=minhasenha \
  -p 5432:5432 -d postgres:18

docker exec -it meu-postgres psql -U postgres
```

- `-e POSTGRES_PASSWORD=...` define a senha do superusuário.
- `-p 5432:5432` expõe a porta padrão para a máquina.
- `docker exec -it ... psql` abre o console dentro do container.

### 6. Verificação da instalação

Depois de instalar, confirme que tudo funciona:

```bash
# 1. Versão do cliente instalado
psql --version

# 2. O servidor está aceitando conexões?
pg_isready

# 3. Conectar ao servidor (pedirá a senha do postgres)
psql -U postgres -h localhost
```

Dentro do console `psql`:

```sql
-- Mostra a versão do servidor
SELECT version();

-- Mostra os detalhes da conexão atual
\conninfo

-- Sai do console
\q
```

No **pgAdmin 4**, a verificação é visual: criar a conexão para `localhost:5432`, usuário `postgres`, senha definida na instalação — se o servidor aparecer na árvore à esquerda, a instalação foi concluída com sucesso.

### 7. Observações importantes

- **Senha do `postgres`**: sem ela não há acesso ao servidor. Guarde em um gerenciador de senhas.
- **Porta 5432**: se você trocar a porta na instalação, todas as conexões futuras precisarão usar a nova porta.
- **Firewall**: para uso local de estudo, normalmente nada precisa ser configurado. Para conexões remotas, libere a porta 5432.
- **No Linux, autenticação local**: por padrão, o acesso via terminal usa o mecanismo _peer_ (o sistema operacional identifica o usuário). Para conectar com senha pelo pgAdmin (via TCP), pode ser necessário ajustar o arquivo `pg_hba.conf` — isso será visto em módulos mais avançados.
- **Backup básico**: os comandos `pg_dump` e `pg_restore` fazem cópia e restauração de bancos:

```bash
pg_dump -U postgres -h localhost meubanco > backup.sql
psql -U postgres -h localhost meubanco < backup.sql
```