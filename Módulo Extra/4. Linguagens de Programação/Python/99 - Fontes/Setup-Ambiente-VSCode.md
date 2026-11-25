---
tags: [setup, python, vscode, ambiente, referencia]
tipo: guia-reutilizavel
status: validado
---
# 📁 Nota: Setup do Ambiente Python — Referência

Nota pronta para colar no Obsidian como 03-Referencias/Setup-Ambiente-Python.md. As três seções são independentes — você pode consultar só a que precisar.

---
## 1. Setup do ambiente Python

### 1.1 Diagnóstico inicial

Antes de instalar qualquer coisa, veja o que já existe:

```markdown
python3 --version
pip3 --version
which python3 
```

- **Os dois respondem** → pule para 1.3
- **python3 responde, pip3 não** → python3 -m ensurepip --upgrade
- **Nenhum responde** → instale o Python (1.2)

> [!info] Por que sempre python3 e pip3 No macOS e no Linux, python e pip podem apontar para versões antigas do sistema. O sufixo 3 é explícito e à prova de ambiguidade.

### 1.2 Instalar o Python

**macOS (Homebrew):**

```markdown 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```

Alternativa sem Homebrew: instalador em [python.org/downloads](https://www.python.org/downloads/macos/).

**Windows:** instalador de [python.org/downloads](https://www.python.org/downloads/windows/) — marque **"Add python.exe to PATH"** na primeira tela.

**Linux (Debian/Ubuntu):**

```markdown 
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### 1.3 Criar o ambiente virtual

O venv isola as bibliotecas do projeto. Sem ele, instalações globais podem quebrar o sistema (externally-managed-environment).

```markdown 
mkdir -p ~/pos-engenharia-de-dados
cd ~/pos-engenharia-de-dados
python3 -m venv .venv
```

### 1.4 Ativar e desativar

**macOS / Linux:**

```markdown 
source .venv/bin/activate
```

**Windows (PowerShell):**

```markdown 
.venv\Scripts\Activate.ps1
```

O sinal de sucesso: o terminal mostra (.venv) no início da linha. Para sair:

```markdown 
deactivate
```

> [!warning] Sempre ative antes de instalar pip install fora do .venv ativa a proteção do sistema e falha com externally-managed-environment. Nunca use sudo pip.

### 1.5 Instalar as bibliotecas

```markdown 
pip install --upgrade pip
pip install pandas numpy jupyter matplotlib seaborn
```

### 1.6 Congelar dependências

O requirements.txt é o que permite recriar o ambiente em outra máquina:

```markdown 
pip freeze > requirements.txt
```

Para restaurar:

```markdown 
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> [!tip] Congele só o essencial pip freeze registra tudo, inclusive dependências indiretas. Para um projeto limpo, mantenha um requirements.in com só o que você usa e gere o requirements.txt a partir dele.

### 1.7 Apontar o VS Code para o .venv

1. Abra a pasta do projeto no VS Code (File → Open Folder)
2. Cmd+Shift+P (mac) ou Ctrl+Shift+P (Windows/Linux)
3. Digite **Python: Select Interpreter**
4. Escolha o caminho que contém .venv/bin/python

Confirmação: no canto inferior direito aparece Python 3.x.x ('.venv'). Em notebooks, use **Select Kernel** no canto superior direito.

### 1.8 Checklist de recriação em outra máquina

☐ 1. python3 --version          → Python instalado?
☐ 2. brew install python        → se faltar
☐ 3. cd na pasta do projeto
☐ 4. python3 -m venv .venv
☐ 5. source .venv/bin/activate  → confere (.venv) no prompt
☐ 6. pip install -r requirements.txt
☐ 7. pip list                   → confere se instalou
☐ 8. VS Code: Select Interpreter → escolher .venv
☐ 9. Rodar um script de teste
☐ 10. code --version            → comando code funciona?

### 1.9 Problemas comuns no ambiente

|Sintoma|Causa|Solução|
|---|---|---|
|externally-managed-environment|pip fora do venv|Ativar o .venv antes|
|ModuleNotFoundError: No module named 'pandas'|Interpretador errado no VS Code|Select Interpreter → .venv|
|command not found: pip|pip não instalado|python3 -m ensurepip --upgrade|
|Permission denied no activate|Falta de permissão|chmod +x .venv/bin/activate|
|Notebook não achou o kernel|Kernel não registrado|Select Kernel → .venv|

---
## 2. Problemas com o comando code no terminal

### 2.1 Por que acontece

O code é um **script binário dentro do pacote do VS Code**, não um programa instalado no sistema. Ele fica em:

macOS:   /Applications/Visual Studio Code.app/Contents/Resources/app/bin/code
Linux:   /usr/share/code/bin/code
Windows: C:\Program Files\Microsoft VS Code\bin\code.cmd

Para o terminal encontrar o comando, essa pasta precisa estar no **PATH** — a lista de lugares onde o shell procura programas. O instalador do VS Code nem sempre cria esse atalho, e é por isso que aparece:

zsh: command not found: code

### 2.2 Correção oficial (macOS e Linux)

1. Abra o VS Code
2. Cmd+Shift+P (mac) ou Ctrl+Shift+P (Linux) → **Command Palette**
3. Digite: **Shell Command: Install 'code' command in PATH**
4. Rode a opção que aparecer
5. **Feche e reabra o terminal**

Esse comando cria o link simbólico necessário. Funciona no macOS e no Linux.

### 2.3 Correção manual (macOS)

Se a opção da Command Palette não aparecer ou falhar:

Depois reabra o terminal.

### 2.4 Correção no Windows

O comando existe, mas só funciona se a pasta bin estiver no PATH:

1. Reinstale o VS Code marcando **"Add to PATH"** (a opção fica na tela de tarefas adicionais)
2. Ou use Ctrl+Shift+P → **Shell Command: Install 'code' command in PATH**
3. Se o VS Code estiver aberto como **Administrador**, rode normalmente uma vez — o Windows pode ter bloqueado a escrita no PATH

### 2.5 Verificar se funcionou

O retorno esperado é a versão e o caminho do binário.

> [!warning] Reabra o terminal O PATH é lido na abertura do shell. Um terminal já aberto não reconhece o comando novo — feche e abra de novo antes de concluir que falhou.

### 2.6 Alternativas enquanto corrige

### 2.7 Diagnóstico rápido

|Sintoma|Causa provável|Ação|
|---|---|---|
|command not found: code|PATH sem o binário|Command Palette → Install in PATH|
|Funciona no VS Code, não no terminal externo|Terminal aberto antes do fix|Reabrir o terminal|
|code abre outro programa|Conflito de nome|Use code --version para conferir|
|Funciona no zsh, não no bash|Configurado só em um shell|Repita o comando para o outro shell|

---

## 3. Extensões recomendadas para VS Code

### 3.1 Desenvolvimento Python

|Extensão|ID|Para que serve|
|---|---|---|
|Python|ms-python.python|Base: instala Pylance, Debugger e Environments|
|Jupyter|ms-toolsai.jupyter|Notebooks .ipynb dentro do VS Code|
|Ruff|charliermarsh.ruff|Lint + formatação + imports em um só|
|Data Wrangler|ms.datawrangler|Ver DataFrame em grade e gerar código Pandas|
|autoDocstring|njpwerner.autodocstring|Gera docstrings a partir da assinatura da função|
|SQLTools|mtxr.sqltools|Rodar SQL dentro do editor|

> [!caution] Não instale à parte **Pylance**, **Python Debugger** e **Python Environments** vêm com a extensão Python. Instalar separadamente pode gerar conflito de versão.

### 3.2 Produtividade geral

|Extensão|ID|Para que serve|
|---|---|---|
|Error Lens|usernamehw.errorlens|Mostra o erro na própria linha, sem passar o mouse|
|Code Spell Checker|streetsidesoftware.code-spell-checker|Corrige erros de digitação em nomes e comentários|
|Better Comments|aaron-bond.better-comments|Comentários coloridos por tipo (TODO, !, ?)|
|Material Icon Theme|pkief.material-icon-theme|Ícones por tipo de arquivo — leitura mais rápida|
|Indent Rainbow|oderwat.indent-rainbow|Colore a indentação; no Python, espaço é sintaxe|
|EditorConfig|editorconfig.editorconfig|Mantém indentação consistente entre editores|
|Bookmarks|alefragnani.bookmarks|Marca linhas para voltar depois|

### 3.3 Organização do fluxo de trabalho

|Extensão|ID|Para que serve|
|---|---|---|
|GitLens|eamodio.gitlens|Histórico e autoria por linha|
|Git Graph|mhutchie.git-graph|Grafo visual dos commits e branches|
|Project Manager|alefragnani.project-manager|Salva e alterna entre projetos|
|Todo Tree|gruntfuggly.todo-tree|Agrupa todos os TODO e FIXME do projeto em um painel|
|Markdown All in One|yzhang.markdown-all-in-one|Atalhos, sumário e preview de Markdown — útil para as notas Obsidian|
|Rainbow CSV|mechatroner.rainbow-csv|Colore colunas de CSV e revela separador errado|
|Remote - SSH|ms-vscode-remote.remote-ssh|Editar código em máquina remota|
|Dev Containers|ms-vscode-remote.remote-containers|Rodar o projeto em container isolado|

### 3.4 Instalação em lote

### 3.5 settings.json recomendado

Cmd+Shift+P → **Preferences: Open User Settings (JSON)**:

> [!tip] Projeto portátil O bloco python.defaultInterpreterPath com ${workspaceFolder} faz o VS Code procurar o .venv da própria pasta. Assim a configuração funciona em qualquer máquina, sem caminho absoluto.

---

## Vínculos sugeridos no Obsidian

[[Setup-Ambiente-Python]]
 ├── [[Mapa-de-Estudos]]
 ├── [[Trilha-de-Progresso]]
 └── [[Processamento-e-Modelagem-de-Dados-Inteligentes]]

---

Se quiser, posso:

- Gerar o **script setup.sh** que executa todo o setup de uma vez na máquina nova
- Criar o **requirements.txt completo** para a disciplina (Pandas, NumPy, Jupyter, Matplotlib, Seaborn, scikit-learn)
- Montar a nota irmã de **Git e versionamento**, para versionar os scripts da pós desde o início