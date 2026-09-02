## 🔷 Laços de repetição em Python (for / while)

Laços (loops) servem para **repetir um bloco de código** até cumprir uma condição ou percorrer uma sequência. Em dados, isso aparece em **varrer listas**, **processar linhas**, **validar input**, **simular testes**, etc.

---

## 🔷 1) `for` (quando você sabe “o que percorrer”)

### ✅ Percorrendo uma lista

```python
bugs = ["CRITICO", "ALTO", "BAIXO"]

for sev in bugs:
    print(sev)
```

### ✅ `range()` (repetir N vezes)

```python
for i in range(5):
    print(i)  # 0,1,2,3,4
```

✅ Muito usado: `range(inicio, fim, passo)`

```python
for i in range(1, 11, 2):
    print(i)  # 1,3,5,7,9
```

---

## 🔷 2) `while` (quando depende de condição)

### ✅ Repetir até o usuário digitar algo válido

```python
while True:
    idade = input("Digite sua idade: ")
    if idade.isdigit() and int(idade) >= 18:
        break
    print("Entrada inválida. Tente de novo.")
```

---

## 🔷 3) `break` e `continue`

- **`break`**: sai do loop imediatamente
- **`continue`**: pula para a próxima iteração

```python
for i in range(1, 6):
    if i == 3:
        continue  # pula o 3
    if i == 5:
        break     # para no 5
    print(i)      # 1,2,4
```

---

## 🔷 4) Laços + condicionais (padrão “real”)

### ✅ QA: contar bugs críticos abertos

```python
bugs = [
    {"id": 1, "sev": "CRITICO", "status": "ABERTO"},
    {"id": 2, "sev": "ALTO", "status": "ABERTO"},
    {"id": 3, "sev": "CRITICO", "status": "FECHADO"},
]

criticos_abertos = 0
for b in bugs:
    if b["sev"] == "CRITICO" and b["status"] == "ABERTO":
        criticos_abertos += 1

print(criticos_abertos)
```

---

## 🔷 5) `else` em loops (pouca gente usa, mas cai em prova)

✅ O `else` do `for/while` roda **somente se o loop terminar sem `break`**.

```python
nums = [2, 4, 6, 7]

for n in nums:
    if n % 2 != 0:
        print("Achei ímpar:", n)
        break
else:
    print("Não achei nenhum ímpar")
```

---

## 🔷 6) Dicas práticas (pra não virar bagunça)

✅ Evite muitos níveis de loop (fica difícil ler)  
✅ Prefira `for` para listas/arquivos  
✅ Use `while` para validação de input e repetição por condição  
✅ Quando der, use `sum`, `any`, `all`, `list comprehension` (mais “Pythonic”)

Exemplo “mais limpo” do contador:

```python
criticos_abertos = sum(
    1 for b in bugs if b["sev"] == "CRITICO" and b["status"] == "ABERTO"
)
```