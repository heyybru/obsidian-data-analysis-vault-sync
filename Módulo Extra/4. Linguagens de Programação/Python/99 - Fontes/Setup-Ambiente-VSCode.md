---
tags: [setup, python, vscode, ambiente, referencia]
tipo: guia-reutilizavel
status: validado
---
# 📁 Nota: Setup do Ambiente Python — Referência

Nota pronta para colar no Obsidian como 03-Referencias/Setup-Ambiente-Python.md. As três seções são independentes — você pode consultar só a que precisar.

---
## 1. Diagnóstico inicial

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

## 2. Instalar o Python

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

## 3. Criar o ambiente virtual

O venv isola as bibliotecas do projeto. Sem ele, instalações globais podem quebrar o sistema (externally-managed-environment).

```markdown 
mkdir -p ~/pos-engenharia-de-dados
cd ~/pos-engenharia-de-dados
python3 -m venv .venv
```

## 4. Ativar e desativar

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

## 5. Instalar as bibliotecas

```markdown 
pip install --upgrade pip
pip install pandas numpy jupyter matplotlib seaborn
```

### 6. Congelar dependências

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

## 7. Apontar o VS Code para o .venv

1. Abra a pasta do projeto no VS Code (File → Open Folder)
2. Cmd+Shift+P (mac) ou Ctrl+Shift+P (Windows/Linux)
3. Digite **Python: Select Interpreter**
4. Escolha o caminho que contém .venv/bin/python

Confirmação: no canto inferior direito aparece Python 3.x.x ('.venv'). Em notebooks, use **Select Kernel** no canto superior direito.

## 8. Checklist de recriação em outra máquina

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

## 9. Problemas comuns no ambiente

|Sintoma|Causa|Solução|
|---|---|---|
|externally-managed-environment|pip fora do venv|Ativar o .venv antes|
|ModuleNotFoundError: No module named 'pandas'|Interpretador errado no VS Code|Select Interpreter → .venv|
|command not found: pip|pip não instalado|python3 -m ensurepip --upgrade|
|Permission denied no activate|Falta de permissão|chmod +x .venv/bin/activate|
|Notebook não achou o kernel|Kernel não registrado|Select Kernel → .venv|
