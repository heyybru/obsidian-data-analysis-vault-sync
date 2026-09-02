## 🔷 A Arte de Contar Histórias com Dados

**Visualização de dados é como "traduzir números para imagens" que nosso cérebro entende instantaneamente**.  
Enquanto tabelas mostram números, gráficos mostram **padrões, tendências e insights**.

✅ **No seu contexto (RH + QA)**:

- **RH**: Gráficos de salários, distribuição de idade, turnover por departamento
- **QA**: Bugs por severidade, tempo de resolução, métricas de qualidade

---

## 🔷 1. Por que Visualizar Dados?

### ✅ **Vantagens da visualização**:

1. **Identificação rápida de padrões**: Tendências, outliers, clusters
2. **Comunicação eficiente**: Stakeholders entendem gráficos mais rápido que tabelas
3. **Tomada de decisão**: Insights visuais levam a ações mais rápidas
4. **Detecção de problemas**: Anomalias saltam aos olhos

### ✅ **Bibliotecas principais**:

```python
# Instalação
pip install matplotlib seaborn plotly pandas

# Import
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import numpy as np

# Configuração básica
plt.style.use('seaborn-v0_8')  # Estilo moderno
sns.set_palette('husl')         # Paleta de cores
```

---

## 🔷 2. Tipos de Gráficos e Quando Usar

### ✅ **Guia de escolha**:

|Tipo de Dados|Pergunta|Gráfico Recomendado|
|---|---|---|
|**Comparação**|Como A se compara com B?|Barras, Colunas|
|**Distribuição**|Como os dados estão distribuídos?|Histograma, Boxplot, Violin|
|**Composição**|Quais são as partes do todo?|Pizza, Barras empilhadas|
|**Relação**|Existe correlação entre variáveis?|Scatter, Heatmap|
|**Tendência**|Como algo muda ao longo do tempo?|Linha, Área|
|**Hierarquia**|Qual é a estrutura?|Treemap, Sunburst|

---

## 🔷 3. Gráficos Básicos com Matplotlib

### ✅ **Gráfico de Linhas (Tendências)**:

```python
# Bugs reportados por mês (QA)
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
bugs = [45, 52, 38, 61, 49, 55]

plt.figure(figsize=(10, 6))
plt.plot(meses, bugs, marker='o', linewidth=2, color='red', markersize=8)
plt.title('Bugs Reportados por Mês', fontsize=14, fontweight='bold')
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Número de Bugs', fontsize=12)
plt.grid(True, alpha=0.3)
plt.ylim(0, 70)
plt.fill_between(meses, bugs, alpha=0.2, color='red')
plt.show()
```

### ✅ **Gráfico de Barras (Comparações)**:

```python
# Candidatos por departamento (RH)
departamentos = ['TI', 'RH', 'Vendas', 'Marketing', 'Financeiro']
candidatos = [25, 15, 20, 12, 18]

plt.figure(figsize=(10, 6))
bars = plt.bar(departamentos, candidatos, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

# Adicionar valores nas barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{int(height)}', ha='center', va='bottom', fontsize=11)

plt.title('Candidatos por Departamento', fontsize=14, fontweight='bold')
plt.xlabel('Departamento', fontsize=12)
plt.ylabel('Número de Candidatos', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### ✅ **Histograma (Distribuição)**:

```python
# Distribuição de salários (RH)
np.random.seed(42)
salarios = np.random.normal(6000, 1500, 1000)

plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(salarios, bins=30, edgecolor='black', alpha=0.7, color='skyblue')

# Destacar faixas
for i in range(len(patches)):
    if bins[i] < 4500:
        patches[i].set_facecolor('lightcoral')  # Baixo salário
    elif bins[i] > 7500:
        patches[i].set_facecolor('lightgreen')  # Alto salário

plt.axvline(np.mean(salarios), color='red', linestyle='--', linewidth=2, label=f'Média: R$ {np.mean(salarios):.0f}')
plt.axvline(np.median(salarios), color='orange', linestyle='--', linewidth=2, label=f'Mediana: R$ {np.median(salarios):.0f}')

plt.title('Distribuição de Salários', fontsize=14, fontweight='bold')
plt.xlabel('Salário (R$)', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### ✅ **Scatter Plot (Relação)**:

```python
# Experiência vs Salário (RH)
np.random.seed(42)
experiencia = np.random.uniform(0, 15, 100)
salario = 3000 + 400 * experiencia + np.random.normal(0, 500, 100)

plt.figure(figsize=(10, 6))
plt.scatter(experiencia, salario, alpha=0.6, s=100, c=experiencia, cmap='viridis')

# Linha de regressão
z = np.polyfit(experiencia, salario, 1)
p = np.poly1d(z)
plt.plot(experiencia, p(experiencia), "r--", linewidth=2, label='Tendência')

plt.title('Relação: Experiência vs Salário', fontsize=14, fontweight='bold')
plt.xlabel('Anos de Experiência', fontsize=12)
plt.ylabel('Salário (R$)', fontsize=12)
plt.colorbar(label='Anos de Experiência')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### ✅ **Gráfico de Pizza (Composição)**:

```python
# Bugs por severidade (QA)
severidades = ['Baixo', 'Médio', 'Alto', 'Crítico']
quantidades = [30, 45, 20, 5]
cores = ['#2ca02c', '#ff7f0e', '#d62728', '#8c564b']

plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(quantidades, labels=severidades, colors=cores,
                                   autopct='%1.1f%%', startangle=90,
                                   explode=(0, 0, 0.1, 0.2))  # Destacar

# Estilizar
plt.setp(autotexts, size=12, weight="bold", color='white')
plt.setp(texts, size=12)

plt.title('Distribuição de Bugs por Severidade', fontsize=14, fontweight='bold')
plt.axis('equal')  # Círculo perfeito
plt.show()
```

---

## 🔷 4. Gráficos Avançados com Seaborn

### ✅ **Boxplot (Distribuição com outliers)**:

```python
# Salários por departamento (RH)
np.random.seed(42)
dados = []
departamentos = ['TI', 'RH', 'Vendas', 'Marketing']

for dept in departamentos:
    if dept == 'TI':
        salarios = np.random.normal(7000, 1000, 50)
    elif dept == 'RH':
        salarios = np.random.normal(5500, 800, 50)
    elif dept == 'Vendas':
        salarios = np.random.normal(6000, 1200, 50)
    else:
        salarios = np.random.normal(5000, 700, 50)
    
    for salario in salarios:
        dados.append({'Departamento': dept, 'Salário': salario})

df = pd.DataFrame(dados)

plt.figure(figsize=(10, 6))
sns.boxplot(x='Departamento', y='Salário', data=df, palette='Set2')
plt.title('Distribuição de Salários por Departamento', fontsize=14, fontweight='bold')
plt.xlabel('Departamento', fontsize=12)
plt.ylabel('Salário (R$)', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')
plt.show()
```

### ✅ **Violin Plot (Distribuição detalhada)**:

```python
plt.figure(figsize=(10, 6))
sns.violinplot(x='Departamento', y='Salário', data=df, palette='muted', inner='quartile')
plt.title('Distribuição Detalhada de Salários', fontsize=14, fontweight='bold')
plt.xlabel('Departamento', fontsize=12)
plt.ylabel('Salário (R$)', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')
plt.show()
```

### ✅ **Heatmap (Correlação)**:

```python
# Matriz de correlação entre métricas
np.random.seed(42)
n = 100
dados_corr = pd.DataFrame({
    'Experiência': np.random.normal(5, 2, n),
    'Idade': np.random.normal(30, 5, n),
    'Salário': 3000 + 400 * np.random.normal(5, 2, n) + np.random.normal(0, 500, n),
    'Bugs_Resolvidos': np.random.poisson(20, n),
    'Horas_Trabalhadas': np.random.normal(160, 20, n)
})

correlacao = dados_corr.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})

plt.title('Matriz de Correlação - Métricas RH/QA', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### ✅ **Pair Plot (Relações múltiplas)**:

```python
# Para datasets pequenos (≤ 10 colunas)
sns.pairplot(dados_corr, diag_kind='kde', corner=True, plot_kws={'alpha': 0.6})
plt.suptitle('Pair Plot - Relações entre Variáveis', y=1.02, fontsize=14, fontweight='bold')
plt.show()
```

### ✅ **Facet Grid (Múltiplos gráficos)**:

```python
# Adicionar coluna de gênero
dados_corr['Gênero'] = np.random.choice(['M', 'F'], n)

g = sns.FacetGrid(dados_corr, col='Gênero', height=5, aspect=1.2)
g.map(sns.scatterplot, 'Experiência', 'Salário', alpha=0.6)
g.set_axis_labels('Experiência (anos)', 'Salário (R$)')
g.set_titles('Gênero: {col_name}')
g.add_legend()

plt.suptitle('Salário vs Experiência por Gênero', y=1.05, fontsize=14, fontweight='bold')
plt.show()
```

---

## 🔷 5. Gráficos Interativos com Plotly

### ✅ **Gráfico interativo de linha**:

```python
import plotly.express as px
import plotly.graph_objects as go

# Dados temporais
datas = pd.date_range('2026-01-01', periods=12, freq='M')
bugs_mensais = [45, 52, 38, 61, 49, 55, 48, 60, 52, 47, 58, 51]
bugs_criticos = [2, 3, 1, 4, 2, 3, 2, 5, 3, 2, 4, 3]

df_temporal = pd.DataFrame({
    'Data': datas,
    'Bugs_Total': bugs_mensais,
    'Bugs_Críticos': bugs_criticos
})

fig = px.line(df_temporal, x='Data', y=['Bugs_Total', 'Bugs_Críticos'],
              title='Bugs Reportados ao Longo do Tempo',
              labels={'value': 'Número de Bugs', 'variable': 'Tipo'},
              template='plotly_white')

fig.update_layout(
    hovermode='x unified',
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
)

fig.show()
```

### ✅ **Gráfico de barras interativo**:

```python
# Salário por departamento e gênero
departamentos = ['TI', 'RH', 'Vendas', 'Marketing']
generos = ['M', 'F']

dados = []
for dept in departamentos:
    for gen in generos:
        if dept == 'TI':
            salario = np.random.normal(7000, 1000) if gen == 'M' else np.random.normal(6500, 1000)
        elif dept == 'RH':
            salario = np.random.normal(5500, 800) if gen == 'M' else np.random.normal(5000, 800)
        else:
            salario = np.random.normal(6000, 900)
        dados.append({'Departamento': dept, 'Gênero': gen, 'Salário': salario})

df_salario = pd.DataFrame(dados)

fig = px.bar(df_salario, x='Departamento', y='Salário', color='Gênero',
             barmode='group', title='Salário por Departamento e Gênero',
             template='plotly_white',
             color_discrete_map={'M': '#1f77b4', 'F': '#ff7f0e'})

fig.update_layout(
    xaxis_title="Departamento",
    yaxis_title="Salário (R$)",
    legend_title="Gênero"
)

fig.show()
```

### ✅ **Treemap interativo**:

```python
# Estrutura organizacional
dados_treemap = pd.DataFrame({
    'Departamento': ['TI', 'TI', 'TI', 'RH', 'RH', 'Vendas', 'Vendas'],
    'Equipe': ['Desenvolvimento', 'Infraestrutura', 'QA', 'Recrutamento', 'Treinamento', 'Vendas Internas', 'Vendas Externas'],
    'Funcionários': [25, 15, 10, 8, 6, 12, 18],
    'Orçamento': [500000, 300000, 200000, 150000, 100000, 250000, 350000]
})

fig = px.treemap(dados_treemap, path=['Departamento', 'Equipe'],
                 values='Funcionários',
                 color='Orçamento',
                 hover_data=['Funcionários', 'Orçamento'],
                 color_continuous_scale='RdBu',
                 title='Estrutura Organizacional - Funcionários e Orçamento')

fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig.show()
```

### ✅ **Dashboard interativo**:

```python
from plotly.subplots import make_subplots

# Criar subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Bugs por Mês', 'Distribuição de Salários',
                    'Bugs por Severidade', 'Correlação Experiência-Salário'),
    specs=[[{'type': 'scatter'}, {'type': 'histogram'}],
           [{'type': 'pie'}, {'type': 'scatter'}]]
)

# Gráfico 1: Linha
fig.add_trace(
    go.Scatter(x=datas, y=bugs_mensais, mode='lines+markers', name='Bugs'),
    row=1, col=1
)

# Gráfico 2: Histograma
fig.add_trace(
    go.Histogram(x=salarios, nbinsx=30, name='Salários'),
    row=1, col=2
)

# Gráfico 3: Pizza
fig.add_trace(
    go.Pie(labels=severidades, values=quantidades, name='Severidade'),
    row=2, col=1
)

# Gráfico 4: Scatter
fig.add_trace(
    go.Scatter(x=experiencia, y=salario, mode='markers', name='Experiência-Salário'),
    row=2, col=2
)

fig.update_layout(height=800, width=1000, title_text="Dashboard RH + QA", showlegend=False)
fig.show()
```

---

## 🔷 6. Visualização para Análise Exploratória (EDA)

### ✅ **Pipeline de EDA visual**:

```python
def eda_visual(df, target_col=None):
    """
    Análise Exploratória Visual Automatizada
    """
    print(f"📊 EDA Visual -
```