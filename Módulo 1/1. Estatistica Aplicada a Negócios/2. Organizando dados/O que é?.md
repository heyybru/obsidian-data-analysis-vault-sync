[Material](obsidian://open?vault=Analise%20de%20Dados&file=img%2FDescomplica%2FDescomplica%20_%20Estat%C3%ADstica%20Aplicada%20A%20Neg%C3%B3cios.pdf)
### **1. Limpar os dados**

**Remover duplicados**

1. **O que é:** Eliminar registros idênticos ou repetidos no dataset.
2. **Por que fazer:** Evita distorções em médias e contagens, garantindo precisão (**Métricas Boss**, +40% de acurácia).
3. **Como fazer:** No Excel/Pandas: `df.drop_duplicates()` ou "Remover Duplicatas" no menu Dados. Ex.: Duplicatas de candidatos RH.

**Corrigir erros de digitação**

1. **O que é:** Identificar e consertar inconsistências como "QA" vs "qa".
2. **Por que fazer:** Padroniza pra buscas fáceis, reduzindo vieses em análises.
3. **Como fazer:** Busca/substituir (Ctrl+H Excel) ou `df.replace()`. Ex. : "Bug API" → "Bug_API".

**Preencher (ou tratar) valores faltando**

1. **O que é:** Substituir ou remover células vazias (NaN).
2. **Por que fazer:** Evita perda de dados e erros em cálculos (**Preditiva.ai**, 50% menos de bias).
3. **Como fazer:** Média/mediana (`df.fillna(df.mean())`) ou excluir (`df.dropna()`). Ex.: Tempo de teste faltante no workbook = média da sprint.

**Padronizar formatos (datas, nomes, números)**

1. **O que é:** Uniformizar (ex.: "01/01/2024" pra todas).
2. **Por que fazer:** Facilita comparações e automação.
3. **Como fazer:** Funções como `pd.to_datetime()` ou formatação do Excel. Ex.: Salários "R$1.000" → 1000.

### **2. Classificar e separar**

**Colocar cada informação no lugar certo**

1. **O que é:** Atribuir dados a colunas/variáveis corretas.
2. **Por que fazer:** Evita confusão, acelerando queries (**Cappra Institute**).
3. **Como fazer:** Pivot tables ou `pd.pivot()`. Ex.: Separar "bugs por módulo" no workbook.

**Criar categorias (ex.: áreas, cargos, regiões, status)**

1. **O que é:** Agrupar dados em grupos lógicos.
2. **Por que fazer:** Revela padrões segmentados.
3. **Como fazer:** `pd.cut()` ou filtros Excel. Ex: Cargos RH: "QA Júnior/Sênior".

### **3. Estruturar**

**Montar tabelas organizadas**

1. **O que é:** Criar estruturas em linhas/colunas claras.
2. **Por que fazer:** Base pra análises avançadas.
3. **Como fazer:** Excel Tables ou `df.to_excel()`. Ex: Tabela sprints x bugs.

**Criar colunas com nomes claros**

1. **O que é:** Renomear pra descritivo (ex.: "bugs_total").
2. **Por que fazer:** Facilita colaboração e scripts.
3. **Como fazer:** `df.rename(columns={'old':'new'})`. Ex.: "Col1" → "Tempo_Teste".

**Definir unidades (ex.: horas, reais, quantidade)**

1. **O que é:** Especificar medidas consistentes.
2. **Por que fazer:** Evita erros de escala.
3. **Como fazer:** Adicionar coluna "unidade". Ex.: Tempo em "horas".

### **4. Transformar em visualizações**

**Gráficos simples (pizza, barras, linha)**

1. **O que é:** Converter dados em imagens intuitivas.
2. **Por que fazer:** Detecta tendências visuais rápidas (**AILabs**).
3. **Como fazer:** Excel Charts ou Matplotlib. Ex.: Pizza de bugs por tipo.

**Tabelas e listas**

1. **O que é:** Resumos tabulares legíveis.
2. **Por que fazer:** Fácil compartilhamento.
3. **Como fazer:** Pivot ou `df.groupby()`. Ex.: Lista top de módulos falhos.

**Quadros-resumo**

1. **O que é:** Painéis com KPIs-chave.
2. **Por que fazer:** Visão executiva.
3. **Como fazer:** Power BI ou `df.describe()`. Ex: Resumo sprints.

### **Para que serve?**

- **Para que os dados façam sentido:** Transforma caos em insights acionáveis.
- **Quando estão organizados, fica fácil ver padrões, analisar e tirar conclusões:** Ganho 60% em produtividade QA (**Snaq.co**).