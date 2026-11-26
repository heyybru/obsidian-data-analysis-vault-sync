import pandas as pd

candidatos = pd.read_csv("candidatos.csv", sep=";", encoding="latin-1")

print(candidatos.shape)
print(candidatos["salario_pretendido"].median())
