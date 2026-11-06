### Organização de pastas

📁 Curso-PostgreSQL/
📁 Curso-PostgreSQL/
├── 📁 consultas/          ← queries salvas (blocos pg)
├── 📁 esquemas/           ← DDL das tabelas (CREATE TABLE)
├── 📁 dados/              ← CSVs de exemplo
└── 📁 resultados/         ← resultados congelados (tabelas markdown)

### Nomenclatura

- Nomeie as consultas com o número do módulo: `M02-SELECT-LIMIT.md`.
- Use comentários nos blocos SQL (`-- explicação`) para lembrar o propósito.

Templates: Crie um template de nota de consulta no Obsidian:

```markdown
modulo: "Módulo {{title}}"
tipo: consulta
data: {{date}}
---

## {{title}}

**Objetivo:** [descreva aqui]

```pg
-- query aqui 
```

Resultado esperado:

**Credenciais**
- **NUNCA** escreva senhas ou tokens em notas de texto puro.
- Use o **Local Secret Vault** para armazenar credenciais criptografadas.
- No Postgres DB, as conexões ficam salvas nas configurações do plugin (não nas notas), o que já é mais seguro — mas evite sincronizar o vault com serviços de nuvem não criptografados.

**Versionamento**
- Considere versionar o vault (ou só a pasta do curso) com Git. Assim suas queries e anotações têm histórico.

### Observações sobre segurança e confiabilidade

**Modo restrito**
O Obsidian vem com **Restricted Mode** ativado por padrão. Você precisa desativá-lo em **Settings → Community plugins** para instalar qualquer plugin. Só desative se confiar nos autores — e mantenha essa lista enxuta.

**Confiabilidade dos plugins**
- Prefira plugins com **muitas estrelas no GitHub**, **atualizações recentes** e **autores conhecidos** na comunidade.
- A comunidade Obsidian está implementando **trust badges e attestation** para plugins — fique de olho nesses selos de verificação.
- Plugins **desktop-only** (como DuckData e SQLSeal) rodam só no computador, o que reduz a superfície de ataque em dispositivos móveis.

**Plugins que acessam rede (Postgres DB, MotherDuck)**
- O Postgres DB se conecta ao seu servidor local — risco baixo.
- O MotherDuck envia queries para a nuvem. Use tokens com escopo limitado e nunca compartilhe o vault com o token.
- **Local Secret Vault** mantém tokens criptografados dentro do vault, resolvendo o dilema "onde guardar a senha".

**Read-only vs. editável**
- **SQL Viewer** é read-only — seguro para inspecionar bancos sem risco de alteração acidental.
- **SQLite DB Viewer** permite editar — útil, mas exige cuidado. Se você só precisa consultar, prefira o SQL Viewer.

**Sincronização**
- Se usar Obsidian Sync, iCloud ou Dropbox, lembre-se: as configurações dos plugins (incluindo conexões do Postgres DB) ficam na pasta `.obsidian` do vault. Em serviços criptografados (Obsidian Sync), isso é OK. Em serviços sem criptografia, evite.