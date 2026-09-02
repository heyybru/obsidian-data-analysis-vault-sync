
## 🔷 Social Media Analytics: Análise de Redes Sociais para RH e QA

Social Media Analytics é como um "termômetro digital" da reputação da empresa**.  
Você mede temperatura (sentimento), pressão (engajamento) e batimentos cardíacos (alcance) da marca nas redes.

✅ **No seu contexto (RH + QA)**:

- **RH**: Analisar percepção da marca como empregadora, recrutar talentos
- **QA**: Monitorar reclamações de clientes, identificar problemas de produto

---

## 🔷 O que é Social Media Analytics?

### ✅ **Definição**:

- **Coleta e análise** de dados de redes sociais
- **Métricas quantitativas**: Likes, shares, comentários, alcance
- **Análise qualitativa**: Sentimento, tópicos, influenciadores
- **Insights acionáveis**: Melhorar produtos, marketing, atendimento

### ✅ **Plataformas principais**:

```
📱 Facebook      → Demografia ampla, grupos
📸 Instagram     → Visual, marca empregadora
🐦 Twitter/X     → Conversas em tempo real, suporte
💼 LinkedIn      → Recrutamento, B2B, profissional
🎥 TikTok        → Geração Z, conteúdo viral
📹 YouTube       → Tutorial, reviews, unboxing
```

---

## 🔷 Métricas Fundamentais

### ✅ **Métricas de Alcance**:

```python
# Exemplo de cálculo em Python
import pandas as pd

dados_social = pd.DataFrame({
    'data': pd.date_range('2026-01-01', periods=7, freq='D'),
    'seguidores': [10000, 10050, 10100, 10150, 10200, 10250, 10300],
    'alcance': [5000, 5200, 4800, 5500, 6000, 5800, 6200],
    'impressoes': [15000, 15500, 14800, 16000, 16500, 16200, 17000]
})

# Crescimento de seguidores
dados_social['crescimento_seguidores'] = dados_social['seguidores'].diff()
dados_social['taxa_crescimento'] = dados_social['crescimento_seguidores'] / dados_social['seguidores'].shift() * 100

print(dados_social[['data', 'seguidores', 'crescimento_seguidores', 'taxa_crescimento']])
```

### ✅ **Métricas de Engajamento**:

```python
# Dados de posts
posts = pd.DataFrame({
    'post_id': [1, 2, 3, 4, 5],
    'likes': [150, 200, 80, 300, 120],
    'comentarios': [20, 35, 10, 50, 15],
    'shares': [5, 8, 2, 12, 4],
    'alcance': [1000, 1200, 800, 1500, 900]
})

# Calcular taxas de engajamento
posts['taxa_engajamento'] = (posts['likes'] + posts['comentarios'] + posts['shares']) / posts['alcance'] * 100
posts['taxa_like'] = posts['likes'] / posts['alcance'] * 100
posts['taxa_comentario'] = posts['comentarios'] / posts['alcance'] * 100

print(posts[['post_id', 'alcance', 'taxa_engajamento', 'taxa_like', 'taxa_comentario']].round(2))
```

---

## 🔷 Análise de Sentimento (NLP)

### ✅ **Classificar comentários como positivo/negativo/neutro**:

```python
import pandas as pd
from textblob import TextBlob  # Biblioteca para análise de sentimento

# Comentários de exemplo
comentarios = [
    "Adorei o novo aplicativo! Muito intuitivo.",
    "O suporte demorou muito para responder.",
    "Funciona bem, mas poderia ter mais features.",
    "Péssima experiência, o app crashou 3 vezes.",
    "Recomendo para todos os amigos!",
    "A atualização piorou a performance.",
    "Interface bonita e fácil de usar.",
    "Não consigo fazer login desde ontem."
]

# Analisar sentimento
analises = []
for comentario in comentarios:
    blob = TextBlob(comentario)
    polaridade = blob.sentiment.polarity  # -1 (negativo) a +1 (positivo)
    subjetividade = blob.sentiment.subjectivity  # 0 (objetivo) a 1 (subjetivo)
    
    # Classificar
    if polaridade > 0.1:
        sentimento = 'POSITIVO'
    elif polaridade &lt; -0.1:
        sentimento = 'NEGATIVO'
    else:
        sentimento = 'NEUTRO'
    
    analises.append({
        'comentario': comentario,
        'polaridade': polaridade,
        'subjetividade': subjetividade,
        'sentimento': sentimento
    })

# Criar DataFrame
df_sentimento = pd.DataFrame(analises)

# Estatísticas
print("📊 Análise de Sentimento:")
print(f"Total comentários: {len(df_sentimento)}")
print(f"Positivos: {len(df_sentimento[df_sentimento['sentimento'] == 'POSITIVO'])}")
print(f"Negativos: {len(df_sentimento[df_sentimento['sentimento'] == 'NEGATIVO'])}")
print(f"Neutros: {len(df_sentimento[df_sentimento['sentimento'] == 'NEUTRO'])}")
print(f"Polaridade média: {df_sentimento['polaridade'].mean():.3f}")

# Mostrar comentários negativos
print("\n⚠️ Comentários Negativos:")
for idx, row in df_sentimento[df_sentimento['sentimento'] == 'NEGATIVO'].iterrows():
    print(f"  - {row['comentario']}")
```

### ✅ **Análise mais avançada com VADER**:

```python
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Baixar recursos (primeira vez)
# nltk.download('vader_lexicon')

# Inicializar analisador
sia = SentimentIntensityAnalyzer()

# Comentários sobre produto
comentarios_produto = [
    "O app é incrível! Muito rápido e intuitivo.",
    "Não gostei da nova interface, está confusa.",
    "Funciona perfeitamente no meu celular.",
    "Consome muita bateria, preciso carregar 3x ao dia.",
    "O suporte foi muito prestativo, resolveram meu problema em 10 minutos."
]

# Analisar cada comentário
for comentario in comentarios_produto:
    scores = sia.polarity_scores(comentario)
    print(f"\n📝 Comentário: {comentario}")
    print(f"  Positivo: {scores['pos']:.3f}")
    print(f"  Neutro: {scores['neu']:.3f}")
    print(f"  Negativo: {scores['neg']:.3f}")
    print(f"  Composto: {scores['compound']:.3f}")
    
    # Interpretar
    if scores['compound'] >= 0.05:
        print("  ✅ Sentimento: Positivo")
    elif scores['compound'] &lt;= -0.05:
        print("  ❌ Sentimento: Negativo")
    else:
        print("  ⚪ Sentimento: Neutro")
```

---

## 🔷 Análise de Tópicos (Topic Modeling)

### ✅ **Identificar tópicos em comentários**:

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np

# Comentários sobre empresa (RH perspectiva)
comentarios_empresa = [
    "Salários competitivos e bons benefícios",
    "Ambiente de trabalho tóxico e pressão alta",
    "Ótimas oportunidades de crescimento profissional",
    "Horários flexíveis e home office",
    "Gestão autoritária e sem transparência",
    "Equipe jovem e dinâmica, muito colaborativa",
    "Falta de reconhecimento e baixos salários",
    "Cultura organizacional forte e valores claros",
    "Processos burocráticos e lentos",
    "Inovação constante e tecnologia de ponta"
]

# Vetorizar texto
vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
X = vectorizer.fit_transform(comentarios_empresa)

# Aplicar LDA para encontrar tópicos
lda = LatentDirichletAllocation(n_components=3, random_state=42)
lda.fit(X)

# Mostrar palavras-chave por tópico
feature_names = vectorizer.get_feature_names_out()

print("🔍 Tópicos identificados nos comentários:")
for topic_idx, topic in enumerate(lda.components_):
    print(f"\n📌 Tópico {topic_idx + 1}:")
    top_words_idx = topic.argsort()[:-10 - 1:-1]
    top_words = [feature_names[i] for i in top_words_idx]
    print(f"  Palavras-chave: {', '.join(top_words)}")
    
    # Comentários mais relacionados a este tópico
    topic_dist = lda.transform(X)[:, topic_idx]
    top_comments_idx = topic_dist.argsort()[-2:][::-1]
    print(f"  Comentários representativos:")
    for idx in top_comments_idx:
        print(f"    - {comentarios_empresa[idx][:50]}...")
```

---

## 🔷 Análise de Influenciadores

### ✅ **Identificar usuários mais influentes**:

```python
import networkx as nx
import pandas as pd

# Dados simulados de interações
interacoes = pd.DataFrame({
    'usuario': ['@joao', '@maria', '@carlos', '@ana', '@pedro', '@julia'],
    'seguidores': [1000, 5000, 800, 12000, 3000, 7000],
    'engajamento_medio': [2.5, 4.8, 1.2, 6.3, 3.1, 5.2],
    'mencionado_por': [
        ['@maria', '@ana'],
        ['@joao', '@carlos', '@pedro'],
        ['@maria'],
        ['@joao', '@maria', '@pedro', '@julia'],
        ['@ana'],
        ['@maria', '@ana']
    ]
})

# Calcular métricas de influência
interacoes['taxa_engajamento'] = interacoes['engajamento_medio'] / interacoes['seguidores'] * 1000
interacoes['mencionado_count'] = interacoes['mencionado_por'].apply(len)
interacoes['influencia_score'] = (
    interacoes['seguidores'] * 0.3 +
    interacoes['engajamento_medio'] * 0.4 +
    interacoes['mencionado_count'] * 0.3
)

# Ordenar por influência
interacoes = interacoes.sort_values('influencia_score', ascending=False)

print("🏆 Ranking de Influenciadores:")
for idx, row in interacoes.iterrows():
    print(f"\n{idx+1}. {row['usuario']}")
    print(f"   Seguidores: {row['seguidores']:,}")
    print(f"   Engajamento: {row['engajamento_medio']:.1f}%")
    print(f"   Mencionado por: {row['mencionado_count']} usuários")
    print(f"   Score influência: {row['influencia_score']:.1f}")
```

---

## 🔷 Social Listening para QA

### ✅ **Monitorar menções a bugs/problemas**:

```python
import re
from datetime import datetime, timedelta

# Dados simulados de menções nas redes
mencoes = [
    {"usuario": "@cliente1", "texto": "O app crasha quando tento fazer login", "data": "2026-01-25 10:30", "plataforma": "Twitter"},
    {"usuario": "@cliente2", "texto": "Não consigo finalizar a compra no site", "data": "2026-01-25 11:15", "plataforma": "Facebook"},
    {"usuario": "@cliente3", "texto": "Erro 404 na página de contato", "data": "2026-01-25 12:45", "plataforma": "Instagram"},
    {"usuario": "@cliente4", "texto": "O suporte não responde há 3 dias", "data": "2026-01-24 09:20", "plataforma": "Twitter"},
    {"usuario": "@cliente5", "texto": "App lento após a última atualização", "data": "2026-01-24 14:30", "plataforma": "Play Store"},
    {"usuario": "@cliente6", "texto": "Problema com pagamento via cartão", "data": "2026-01-23 16:45", "plataforma": "Facebook"}
]

# Converter para DataFrame
df_mencoes = pd.DataFrame(mencoes)
df_mencoes['data'] = pd.to_datetime(df_mencoes['data'])

# Palavras-chave para problemas
keywords_problemas = {
    'bug': ['crasha', 'erro', 'bug', 'falha', 'não funciona'],
    'performance': ['lento', 'travando', 'demora', 'congelou'],
    'usabilidade': ['confuso', 'difícil', 'complicado', 'intuitivo'],
    'suporte': ['suporte', 'responder', 'atendimento', 'esperando'],
    'pagamento': ['pagamento', 'compra', 'cartão', 'transação']
}

# Classificar menções
def classificar_menção(texto):
    texto_lower = texto.lower()
    categorias = []
    
    for categoria, palavras in keywords_problemas.items():
        for palavra in palavras:
            if palavra in texto_lower:
                categorias.append(categoria)
                break
    
    return ', '.join(set(categorias)) if categorias else 'outros'

df_mencoes['categoria'] = df_mencoes['texto'].apply(classificar_menção)

# Análise
print("📊 Social Listening - Problemas Reportados:")
print(f"Total menções: {len(df_mencoes)}")
print(f"Período: {df_mencoes['data'].min().date()} a {df_mencoes['data'].max().date()}")

print("\n🔍 Por categoria:")
categoria_counts = df_mencoes['categoria'].value_counts()
for categoria, count in categoria_counts.items():
    print(f"  {categoria}: {count} menções ({count/len(df_mencoes)*100:.1f}%)")

print("\n📱 Por plataforma:")
plataforma_counts = df_mencoes['plataforma'].value_counts()
for plataforma, count in plataforma_counts.items():
    print(f"  {plataforma}: {count} menções")

# Alertas para problemas críticos
print("\n🚨 Alertas Críticos (últimas 24h):")
limite = datetime.now() - timedelta(hours=24)
recentes = df_mencoes[df_mencoes['data'] > limite]

if len(recentes) > 0:
    for _, mencao in recentes.iterrows():
        if 'bug' in mencao['categoria'] or 'pagamento' in mencao['categoria']:
            print(f"  ⚠️ {mencao['usuario']}: {mencao['texto']} ({mencao['plataforma']})")
else:
    print("  ✅ Nenhum alerta crítico nas últimas 24h")
```

---

## 🔷 Employer Branding (RH)

### ✅ **Analisar percepção como empregador**:

```python
# Dados de reviews no Glassdoor/Indeed
reviews_empresa = pd.DataFrame({
    'data': pd.date_range('2025-07-01', periods=50, freq='W'),
    'rating_geral': np.random.normal(4.2, 0.8, 50).clip(1, 5),
    'rating_cultura': np.random.normal(4.0, 0.9, 50).clip(1, 5),
    'rating_salario': np.random.normal(3.8, 1.0, 50).clip(1, 5),
    'rating_crescimento': np.random.normal(4.3, 0.7, 50).clip(1, 5),
    'sentimento': np.random.choice(['Positivo', 'Negativo', 'Neutro'], 50, p=[0.6, 0.2, 0.2])
})

# Análise temporal
reviews_empresa['media_movel'] = reviews_empresa['rating_geral'].rolling(window=4).mean()

print("🏢 Employer Branding Analysis:")
print(f"Período analisado: {reviews_empresa['data'].min().date()} a {reviews_empresa['data'].max().date()}")
print(f"Total reviews: {len(reviews
```