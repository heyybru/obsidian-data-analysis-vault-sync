### **O Que São Gráficos de Dispersão?**

- **Definição curta**: Pontos plotados em X/Y pra mostrar **relações entre 2 variáveis** (correlação positiva/negativa, clusters).
- **Por quê usar?**: Revela padrões ocultos (ex: seniors ganham mais?).

### **Tipos Principais**

- **Dispersão Simples**: 2 vars. Ex: `experiencia_anos` (X) x `pretensao_salarial` (Y).
- **Com Bolhas**: 3ª var pelo tamanho/cor. Ex: + `nota_entrevista_tecnica` (tamanho bolha).
- **Com Linha de Tendência**: Adicione regressão linear pra força da correlação.

### **Como Criar no Google Sheets (Manual)**

1. Selecione 2 cols (ex: experiencia_anos, pretensao_salarial).
2. Inserir > Gráfico > Dispersão (X/Y).
3. Personalize: Série cor por `foi_contratado`, linha tendência (Configurar > Série > Tendência). Ex: No dataset: Correlação positiva (r~0.7, seniors >10k)!

### **Exemplo Prático no Seu Dataset**

```
Experiência (X) | Salário (Y)
2 anos          • 5k
5 anos          • 8k
10 anos         •██ 12k (cluster seniors)
```

**Insight negócio**: Correlação exp-salário forte – priorize seniors pra ROI alto (**Metricas Boss**).