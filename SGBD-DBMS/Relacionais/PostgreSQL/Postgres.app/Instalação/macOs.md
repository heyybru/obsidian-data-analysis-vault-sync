[download](https://postgresapp.com/)

## 🧩 O que é o Postgres.app

É um app nativo do macOS que já vem com o PostgreSQL embutido, com uma janelinha para ligar/desligar o servidor e ver seus bancos. Você arrasta para a pasta Aplicativos, clica em **Initialize** e pronto: servidor rodando.

> **Premissas que estou assumindo:** seu Mac está com um macOS atual de 2026 (linha 26 "Tahoe" ou mais novo) e você nunca instalou PostgreSQL antes. Se já usou Homebrew ou o instalador da EDB, vale desinstalar antes para evitar conflito de porta.

## 📥 Passo 1 — Baixar

1. Acesse **[https://postgresapp.com/downloads.html](https://postgresapp.com/downloads.html)**
2. Baixe o pacote **Postgres.app v2.9.6 (PostgreSQL 18.6, Universal)** — ~123 MB.
3. "Universal" significa que roda nativamente em Apple Silicon, incluindo o **M5** — sem precisar de Rosetta.

> 💡 **Por que essa versão:** é a estável mais recente (agosto/2026). Existe também um pacote com todas as versões (533 MB), útil só se você quiser testar PostgreSQL 17/16 ao mesmo tempo. Deixe a versão 19 Beta (alpha) de lado por enquanto — é experimental.

## 📦 Passo 2 — Instalar

1. Abra o arquivo `.dmg` baixado.
2. **Arraste o Postgres.app para a pasta Aplicativos** (importante: rodar de outro lugar faz alguns recursos falharem).
3. Dê duplo clique no app. Na primeira abertura, o macOS pode perguntar se você confirma abrir um app baixado da internet → clique em **Abrir**.

## 🚀 Passo 3 — Inicializar o servidor

1. Na janela do app, clique em **Initialize** (ou "Create a new server").
2. Ele cria o _cluster_ — o servidor e seus bancos — e já cria um banco com o **mesmo nome do seu usuário do macOS**.

> 🔎 **Definição rápida:** _cluster_ é o "pacote-mãe" que contém todos os bancos do servidor. Pense como uma gaveta onde cada banco é uma pasta.
> 
> ✔️ **Check rápido:** qual banco o Postgres.app cria por padrão? _(Resposta: o que tem o mesmo nome do seu usuário.)_

## 🖥️ Passo 4 — (Opcional, recomendado) Usar o `psql` no Terminal

1. Abra o **Terminal** e cole:

```bash
sudo mkdir -p /etc/paths.d && echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp
```

1. Digite sua senha de administrador quando pedir (a senha não aparece na tela — é normal).
2. **Feche e abra um Terminal novo** (sem isso, o PATH não é recarregado).
3. Confirme com:

```bash
which psql
```

> Esperado: `/Applications/Postgres.app/Contents/Versions/latest/bin/psql`

## 🧪 Passo 5 — Criar um banco de teste

```bash
createdb aprendizado
```

Ou crie pelo próprio app (botão "+" na lista de bancos).

## ✅ Passo 6 — Confirmar que está funcionando

- **No app:** o servidor aparece com indicador verde/"running" e a lista de bancos.
- **No Terminal:**

```bash
psql --version
psql -l
psql -c "SELECT version();"
```

> Esperado: versão **PostgreSQL 18.6** e a lista de bancos aparecendo. Se aparecer, está tudo certo! 🎉

## 🔐 Permissões de segurança no macOS 2026

- O Postgres.app é **assinado e notarizado** pelo desenvolvedor → normalmente abre sem truques.
- Fluxo comum: aviso "app baixado da internet" → **Abrir**.
- Se o macOS bloquear (mais comum em builds alpha/beta): **Ajustes do Sistema → Privacidade e Segurança → "Abrir Mesmo Assim"**.
- O comando do Passo 4 usa `sudo`, então exige senha de administrador.
- Os dados ficam em `~/Library/Application Support/Postgres/var-18` — sem permissões especiais necessárias.

> ⚠️ **Incerteza:** o texto exato dos avisos e o nome dos painéis podem variar entre versões do macOS (26 vs 27). O caminho "Abrir Mesmo Assim" é o mesmo há várias versões, mas confirme na sua tela.

## 🧭 Diferenças e incertezas em 2026 (transparência)

- **Fundamento consolidado:** o fluxo "arrastar → Initialize → PATH" é estável há anos, não deve mudar.
- **Prática atual:** v2.9.6 com PostgreSQL 18.6 é o recomendado hoje.
- **Experimental:** a linha **3alpha8** (PostgreSQL 19 Beta) cita correções para "macOS 27 Beta" e "menos avisos no macOS Tahoe" — sinal de que macOS muito novos ainda podem gerar pequenos avisos dependendo da versão do app.
- **Não consegui confirmar:** nenhuma nota pública específica sobre o **M5**. Mas como o binário é **Universal (arm64)**, ele cobre qualquer Apple Silicon (M1 a M5) nativamente.

## 🆘 Se algo der errado

- `psql: command not found` → PATH não aplicado: abra um Terminal novo e confira se o arquivo `/etc/paths.d/postgresapp` existe.
- Porta 5432 ocupada → provavelmente existe outro PostgreSQL (Homebrew/EDB). Desligue/desinstale o antigo.
- App não abre → Privacidade e Segurança → **Abrir Mesmo Assim**.