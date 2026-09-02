Python é como uma "caixa de ferramentas" onde cada biblioteca é uma ferramenta específica**.  
Você não precisa usar todas, mas conhecer as essenciais ajuda a resolver problemas de dados de forma eficiente.

✅ **No seu contexto (RH + QA)**:

- **RH**: Pandas para analisar currículos, NumPy para cálculos de turnover, Scikit-learn para prever contratações
- **QA**: Pandas para analisar logs de bugs, Matplotlib para gráficos de qualidade, Requests para APIs de testes

---

## 🔷 Instalação Básica

### ✅ **Via pip (recomendado)**

```bash
# Instale o pip se não tiver
python -m ensurepip --upgrade

# Crie ambiente virtual (sempre!)
python -m venv meu_projeto
source meu_projeto/bin/activate  # Linux/Mac
# meu_projeto\Scripts\activate   # Windows

# Instale bibliotecas essenciais
pip install pandas numpy matplotlib seaborn scikit-learn requests sqlalchemy
```

### ✅ **Via Anaconda (para iniciantes)**

```bash
# Baixe Anaconda (https://anaconda.com)
conda create -n dados python=3.11
conda activate dados
conda install pandas numpy matplotlib seaborn scikit-learn requests sqlalchemy
```

---

## 🔷 1. Pandas: Manipulação de Dados Tabulares

**Para que serve**: Trabalhar com dados como tabelas Excel, mas muito mais poderoso.

### ✅ **Instalação e import**

```bash
pip install pandas
```

```python
import pandas as pd
```

### ✅ **Exemplos práticos (RH)**

```python
# Carregar dados de candidatos
candidatos = pd.read_csv('candidatos.csv')

# Ver primeiras linhas
print(candidatos.head())

# Filtrar candidatos experientes
experientes = candidatos[candidatos['experiencia_anos'] >= 3]

# Calcular salário médio por cargo
salario_medio = candidatos.groupby('cargo')['salario'].mean()

# Salvar resultado
salario_medio.to_csv('salario_por_cargo.csv')
```

### ✅ **Exemplos práticos (QA)**

```python
# Carregar logs de bugs
bugs = pd.read_csv('bugs.csv')

# Contar bugs por severidade
bugs_por_severidade = bugs['severidade'].value_counts()

# Filtrar bugs críticos não resolvidos
criticos_abertos = bugs[(bugs['severidade'] == 'critico') & 
                       (bugs['status'] != 'resolvido')]

# Calcular tempo médio de resolução
tempo_medio = bugs['horas_resolucao'].mean()
```

---

## 🔷 2. NumPy: Arrays e Cálculos Numéricos

**Para que serve**: Trabalhar com números de forma eficiente (base de tudo em dados científicos).

### ✅ **Instalação e import**

```bash
pip install numpy
```

```python
import numpy as np
```

### ✅ **Exemplos práticos**

```python
# Arrays eficientes
salarios = np.array([5000, 6000, 7000, 5500])
bonus = np.array([500, 600, 700, 550])

# Operações vetorizadas (rápidas)
total = salarios + bonus  # [5500, 6600, 7700, 6050]

# Estatísticas
media = np.mean(salarios)      # Média salarial
desvio = np.std(salarios)      # Desvio padrão
mediana = np.median(salarios)  # Mediana

# Matrizes para correlações
dados_rh = np.array([
    [4, 5000],  # [experiência, salário]
    [2, 4000],
    [6, 7000]
])
correlacao = np.corrcoef(dados_rh[:, 0], dados_rh[:, 1])[0, 1]
```

---

## 🔷 3. Matplotlib: Visualização Básica

**Para que serve**: Criar gráficos simples para explorar dados.

### ✅ **Instalação e import**

```bash
pip install matplotlib
```

```python
import matplotlib.pyplot as plt
```

### ✅ **Exemplos práticos (RH)**

```python
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
candidatos = pd.read_csv('candidatos.csv')

# Gráfico de barras: Candidatos por estado
candidatos['estado'].value_counts().plot(kind='bar')
plt.title('Candidatos por Estado')
plt.xlabel('Estado')
plt.ylabel('Número de Candidatos')
plt.show()

# Histograma: Distribuição de salários
plt.hist(candidatos['salario'], bins=10, edgecolor='black')
plt.title('Distribuição de Salários')
plt.xlabel('Salário (R$)')
plt.ylabel('Frequência')
plt.show()
```

### ✅ **Exemplos práticos (QA)**

```python
# Gráfico de pizza: Bugs por severidade
bugs['severidade'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Bugs por Severidade')
plt.show()

# Linha temporal: Bugs por dia
bugs['data'] = pd.to_datetime(bugs['data'])
bugs_por_dia = bugs.groupby('data')['id'].count()
bugs_por_dia.plot(kind='line')
plt.title('Bugs por Dia')
plt.xlabel('Data')
plt.ylabel('Número de Bugs')
plt.show()
```

---

## 🔷 4. Seaborn: Visualização Estatística

**Para que serve**: Gráficos mais bonitos e estatísticos (baseado no Matplotlib).

### ✅ **Instalação e import**

```bash
pip install seaborn
```

```python
import seaborn as sns
```

### ✅ **Exemplos práticos**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar dados
candidatos = pd.read_csv('candidatos.csv')

# Boxplot: Salário por cargo
plt.figure(figsize=(10, 6))
sns.boxplot(x='cargo', y='salario', data=candidatos)
plt.title('Distribuição de Salários por Cargo')
plt.xticks(rotation=45)
plt.show()

# Scatter plot com regressão: Experiência vs Salário
plt.figure(figsize=(8, 6))
sns.regplot(x='experiencia_anos', y='salario', data=candidatos)
plt.title('Correlação: Experiência vs Salário')
plt.show()

# Heatmap: Correlação entre variáveis numéricas
plt.figure(figsize=(8, 6))
numeric_cols = ['experiencia_anos', 'salario', 'idade']
correlation = candidatos[numeric_cols].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlação entre Variáveis')
plt.show()
```

---

## 🔷 5. Scikit-learn: Machine Learning

**Para que serve**: Algoritmos de ML para classificação, regressão, clustering.

### ✅ **Instalação e import**

```bash
pip install scikit-learn
```

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
```

### ✅ **Exemplos práticos (RH)**

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Carregar dados
candidatos = pd.read_csv('candidatos.csv')

# Preparar dados para ML
X = candidatos[['experiencia_anos', 'idade']]  # Features
y = candidatos['salario']                       # Target

# Dividir treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Treinar modelo de regressão
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Fazer previsões
y_pred = modelo.predict(X_test)

# Avaliar modelo
mse = mean_squared_error(y_test, y_pred)
print(f'Erro médio quadrático: R$ {mse:.2f}')

# Prever salário de novo candidato
novo_candidato = pd.DataFrame([[5, 28]], columns=['experiencia_anos', 'idade'])
salario_previsto = modelo.predict(novo_candidato)
print(f'Salário previsto: R$ {salario_previsto[0]:.2f}')
```

### ✅ **Exemplos práticos (QA)**

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Carregar dados de bugs
bugs = pd.read_csv('bugs.csv')

# Preparar dados para clustering
features = bugs[['horas_resolucao', 'severidade_num']]  # severidade_num: critico=3, alto=2, medio=1, baixo=0

# Normalizar dados
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Aplicar K-means (3 clusters)
kmeans = KMeans(n_clusters=3, random_state=42)
bugs['cluster'] = kmeans.fit_predict(features_scaled)

# Analisar clusters
print(bugs.groupby('cluster')[['horas_resolucao', 'severidade_num']].mean())
```

---

## 🔷 6. Requests: Comunicação com APIs

**Para que serve**: Fazer requisições HTTP para APIs web.

### ✅ **Instalação e import**

```bash
pip install requests
```

```python
import requests
```

### ✅ **Exemplos práticos**

```python
# API de dados de RH (simulado)
response = requests.get('https://api.rh-empresa.com/candidatos')
if response.status_code == 200:
    candidatos_api = response.json()
    print(f"Total candidatos na API: {len(candidatos_api)}")

# Enviar dados para API de QA
bug_data = {
    'titulo': 'Erro no login',
    'severidade': 'critico',
    'modulo': 'autenticacao'
}

response = requests.post('https://api.qa-empresa.com/bugs', 
                        json=bug_data)
if response.status_code == 201:
    print("Bug reportado com sucesso!")

# API com autenticação
headers = {'Authorization': 'Bearer seu_token_aqui'}
response = requests.get('https://api.empresa.com/metricas', 
                       headers=headers)
metricas = response.json()
```

---

## 🔷 7. SQLAlchemy: Bancos de Dados

**Para que serve**: Conectar e consultar bancos de dados SQL.

### ✅ **Instalação e import**

```bash
pip install sqlalchemy
```

```python
from sqlalchemy import create_engine, text
```

### ✅ **Exemplos práticos**

```python
from sqlalchemy import create_engine, text
import pandas as pd

# Conectar ao banco PostgreSQL
engine = create_engine('postgresql://user:password@localhost:5432/rh_db')

# Consultar candidatos
query = """
SELECT nome, cargo, salario, experiencia_anos 
FROM candidatos 
WHERE experiencia_anos >= 3 
ORDER BY salario DESC
"""

candidatos_df = pd.read_sql(query, engine)
print(candidatos_df.head())

# Inserir novo bug
insert_query = text("""
INSERT INTO bugs (titulo, severidade, desenvolvedor) 
VALUES (:titulo, :severidade, :desenvolvedor)
""")

with engine.connect() as conn:
    conn.execute(insert_query, {
        'titulo': 'Erro 404 na página principal',
        'severidade': 'medio',
        'desenvolvedor': 'João Silva'
    })
    conn.commit()

print("Bug inserido no banco!")
```

---

## 🔷 8. Outras Bibliotecas Úteis

### ✅ **Jupyter Notebook**: Ambiente interativo

```bash
pip install jupyter
jupyter notebook
```

### ✅ **Plotly**: Gráficos interativos

```bash
pip install plotly
```

### ✅ **BeautifulSoup**: Web scraping

```bash
pip install beautifulsoup4
```

### ✅ **FastAPI**: APIs web

```bash
pip install fastapi uvicorn
```

---

## 🔷 Estrutura de Projeto Recomendada

```
meu_projeto/
├── venv/                    # Ambiente virtual
├── data/                    # Dados (CSV, JSON)
├── notebooks/               # Jupyter notebooks
├── scripts/                 # Scripts Python
├── requirements.txt         # Dependências
└── README.md               # Documentação
```

### ✅ **requirements.txt**

```
pandas==2.0.3
numpy==1.24.3
matplotlib==3.7.2
seaborn==0.12.2
scikit-learn==1.3.0
requests==2.31.0
sqlalchemy==2.0.20
jupyter==1.0.0
```

---

## 🔷 Boas Práticas

### ✅ **Imports organizados**

```python
# Padrão: bibliotecas padrão primeiro, depois externas
import os
import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
```

### ✅ **Tratamento de erros**

```python
try:
    df = pd.read_csv('dados.csv')
except FileNotFoundError:
    print("Arquivo não encontrado!")
except pd.errors.EmptyDataError:
    print("Arquivo vazio!")
```

### ✅ **Performance**

```python
# Use operações vetorizadas (Pandas/NumPy)
# Evite loops quando possível
# Use .apply() só quando necessário
```

---

## 🔷 Exercício Prático: Dashboard RH+QA

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# 1. Carregar dados
candidatos = pd.read_csv('candidatos.csv')
bugs = pd.read_csv('bugs.csv')

# 2. Análise RH
print("=== DASHBOARD RH ===")
print(f"Total candidatos: {len(candidatos)}")
print(f"Salário médio: R$ {candidatos['salario'].mean():.2f}")

# Candidatos por estado
plt.figure(figsize=(8, 5))
candidatos['estado'].value_counts().plot(kind='bar')
plt.title('Candidatos por Estado')
plt.show()

# 3. Análise QA
print("\n=== DASHBOARD QA ===")
print(f"Total bugs: {len(bugs)}")
bugs_por_severidade = bugs['severidade'].value_counts()
print("Bugs por severidade:")
print(bugs_por_severidade)

# Tempo médio de resolução
tempo_medio = bugs['horas_resolucao'].mean()
print(f"Tempo médio resolução: {tempo_medio:.1f} horas")

# Gráfico de bugs
plt.figure(figsize=(6, 6))
bugs_por_severidade.plot(kind='pie', autopct='%1.1f%%')
plt.title('Bugs por Severidade')
plt.show()

# 4. Correlação RH-QA (simulado)
print("\n=== CORRELAÇÃO RH-QA ===")
# Simular dados de correlação
experiencia = candidatos['experiencia_anos']
salario = candidatos['salario']

# Regressão linear
X = experiencia.values.reshape(-1, 1)
y = salario.values
modelo = LinearRegression()
modelo.fit(X, y)

print(f"Coeficiente: {modelo.coef_[0]:.2f} (R$ por ano de experiência)")
print(f"Intercepto: R$ {modelo.intercept_:.2f}")

# Gráfico
plt.figure(figsize=(8, 6))
plt.scatter(experiencia, salario, alpha=0.5)
plt.plot(experiencia, modelo.predict(X), color='red')
plt.title('Correlação: Experiência vs Salário')
plt.xlabel('Anos de Experiência')
plt.ylabel('Salário (R$)')
plt.show()
```

