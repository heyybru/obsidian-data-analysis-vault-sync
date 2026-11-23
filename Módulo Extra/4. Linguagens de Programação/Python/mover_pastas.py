from pathlib import Path
import shutil

# ============ CONFIGURACAO ============
SIMULAR = False      # True = so mostra | False = move de verdade

# ============ LOCALIZAR O VAULT ============
# Usa a pasta onde ESTE script esta salvo. Sem caminho digitado.
VAULT = Path(__file__).resolve().parent

print("=" * 64)
print("LOCALIZACAO")
print("=" * 64)
print(f"Script em: {VAULT}")

marcadores = ["00 - MOC", "01 - Fundamentos", "Python-Vault"]
achados = [m for m in marcadores if (VAULT / m).exists()]

if not achados:
    print("\n[ERRO] Esta pasta nao parece ser a raiz do vault.")
    print("Salve o script dentro da pasta 'Python' e rode de novo.\n")
    print("Conteudo encontrado aqui:")
    for item in sorted(VAULT.iterdir()):
        print(f"  - {item.name}{'/' if item.is_dir() else ''}")
    raise SystemExit(1)

print(f"Encontrado: {', '.join(achados)}")

# ============ LOCALIZAR A ORIGEM ============
origens = []
for p in VAULT.iterdir():
    if not p.is_dir():
        continue
    nome = p.name.lower().replace("-", "").replace("_", "").replace(" ", "")
    if nome.startswith("pythonvault"):
        origens.append(p)

if not origens:
    print("\n[ERRO] Nao encontrei a pasta 'Python-Vault' aqui dentro.")
    print("Ou ja foi movida, ou as notas estao em outro lugar.\n")
    print("Pastas que existem aqui agora:")
    for p in sorted(VAULT.iterdir()):
        if p.is_dir():
            qtd = len(list(p.glob("*.md")))
            print(f"  - {p.name}/  ({qtd} arquivos .md)")
    raise SystemExit(1)

ORIGEM = origens[0]
print(f"Origem  : {ORIGEM.name}")
print(f"Modo    : {'SIMULACAO (nada sera movido)' if SIMULAR else 'EXECUCAO REAL'}")
print("-" * 64)

# ============ MOVER ============
movidas, mescladas, conflitos = [], [], []

for item in sorted(ORIGEM.iterdir()):
    if not item.is_dir():
        continue

    destino = VAULT / item.name

    if not destino.exists():
        if not SIMULAR:
            shutil.move(str(item), str(destino))
        movidas.append(item.name)
        print(f"[MOVER]   {item.name}")
        continue

    print(f"[MESCLAR] {item.name}")
    for arq in sorted(item.iterdir()):
        alvo = destino / arq.name
        if alvo.exists():
            conflitos.append(f"{item.name}/{arq.name}")
            print(f"   [CONFLITO] {arq.name} ja existe - mantido")
        else:
            if not SIMULAR:
                shutil.move(str(arq), str(alvo))
            mescladas.append(f"{item.name}/{arq.name}")
            print(f"   [OK]       {arq.name}")

# ============ RESUMO ============
print("-" * 64)
print(f"Pastas movidas inteiras : {len(movidas)}")
print(f"Arquivos mesclados      : {len(mescladas)}")
print(f"Conflitos (nao movidos) : {len(conflitos)}")
for c in conflitos:
    print(f"   - {c}")

if SIMULAR:
    print("\n>>> Nada foi alterado. Mude SIMULAR = False e rode de novo.")
else:
    print("\n>>> Movimento concluido. Conferindo o resultado:\n")
    for pasta in sorted(VAULT.iterdir()):
        if pasta.is_dir() and pasta.name != ORIGEM.name:
            qtd = len(list(pasta.glob("*.md")))
            print(f"   {pasta.name:<26} {qtd:>3} arquivos .md")