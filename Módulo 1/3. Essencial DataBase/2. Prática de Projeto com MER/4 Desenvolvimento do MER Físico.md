> [!info] 
> O **MER Físico** é a etapa onde o modelo **vira banco de dados de verdade**. É aqui que: 

- **Escolhemos o SGBD** (MySQL, PostgreSQL, Oracle…)
- Definimos **tipos de dados reais**
- Definimos **restrições** (constraints)
- Pensamos em **performance e armazenamento**

📌 É o modelo **dependente do SGBD** — diferente do conceitual (independente) e do lógico (quase independente).

🔑 **Analogia:** se o conceitual é a **planta da casa** e o lógico é a **lista de materiais**, o físico é a **construção da casa** — você executa os comandos e o banco ganha vida.

---
## 1. Do MER Lógico para o MER Físico

A diferença é o **nível de detalhe**:

|No Lógico você dizia|No Físico você define|
|---|---|
|`INT`|Tamanho exato, auto incremento → `INT AUTO_INCREMENT`|
|`VARCHAR`|Tamanho exato → `VARCHAR(100)`|
|(nada)|Regras → `NOT NULL`, `UNIQUE`|
|(nada)|Auto incremento → `AUTO_INCREMENT` / `SERIAL`|

---

## 2. Tipos de Dados (exemplo MySQL)

| Conceito       | Tipo Físico   | Exemplo         |
| -------------- | ------------- | --------------- |
| Identificador  | INT           | id_departamento |
| Texto curto    | VARCHAR(100)  | nome            |
| Texto longo    | TEXT          | descrição       |
| Data           | DATE          | data_nascimento |
| Número decimal | DECIMAL(10,2) | salario         |

## 3. Restrições (Constraints)

As restrições garantem a **integridade** dos dados:

### 🔑 PRIMARY KEY

- Identifica o registro
- **Não aceita nulo**

```sql
id_departamento INT PRIMARY KEY
```

### 🔗 FOREIGN KEY

- Garante **integridade referencial**

```sql
FOREIGN KEY (id_departamento)
REFERENCES Departamento(id_departamento)
```

### ❗ NOT NULL

- Campo **obrigatório**

```sql
nome VARCHAR(100) NOT NULL
```

### 🔁 UNIQUE

- **Não permite valores repetidos**

```sql
email VARCHAR(100) UNIQUE
```

---

## 4. Exemplo Completo — MER Físico

**🎯 Cenário:** empresa com Departamentos e Colaboradores.

**🏢 DEPARTAMENTO (MySQL):**

```sql
CREATE TABLE Departamento (
  id_departamento INT AUTO_INCREMENT PRIMARY KEY,
  nome_departamento VARCHAR(100) NOT NULL
);
```

**🧑 COLABORADOR (MySQL):**

```sql
CREATE TABLE Colaborador (
  id_colaborador INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  cargo VARCHAR(50) NOT NULL,
  id_departamento INT NOT NULL,
  CONSTRAINT fk_departamento
    FOREIGN KEY (id_departamento)
    REFERENCES Departamento(id_departamento)
);
```

---

## 5. Tratamento dos Relacionamentos no Físico

|Relacionamento|Como fica no físico|
|---|---|
|**1:N**|FK no lado N + constraint de chave estrangeira|
|**1:1**|FK com `UNIQUE` → `id_colaborador INT UNIQUE`|
|**N:N**|Tabela associativa com PK composta|

**Exemplo N:N:**

```sql
CREATE TABLE Aluno_Curso (
  id_aluno INT,
  id_curso INT,
  PRIMARY KEY (id_aluno, id_curso)
);
```

---

## 6. Diferença Rápida (Conceitual × Lógico × Físico)

| Etapa      | O que define                  |
| ---------- | ----------------------------- |
| Conceitual | Entidades e relacionamentos   |
| Lógico     | Tabelas, PK e FK              |
| Físico     | SQL, tipos reais e restrições |

---

## 7. Regras de Nomenclatura

Ao criar o modelo físico, você transforma o modelo lógico em **tabelas reais** — por isso, é obrigatório seguir as **regras do SGBD**. Algumas são comuns a todos:

1. **Nome não pode começar com número** — ❌ `1cliente` → ✅ `cliente1`
2. **Não pode haver nomes duplicados** — duas tabelas/colunas com o mesmo nome no mesmo contexto
3. **Não pode usar palavras reservadas** — ❌ `SELECT`, `TABLE`, `ORDER` → ✅ `pedido`, `tabela_pedido`
4. **Caracteres especiais permitidos** — somente `_`, `$`, `#` → ❌ `cliente-novo` → ✅ `cliente_novo`
5. **Pode usar letras e números** — desde que não comece com número
6. **Tamanho do nome** — depende do SGBD. Ex.: Oracle 10g+ → até **128 caracteres**

---

## 8. Ordem de Criação das Tabelas

A ordem **importa** por causa das **chaves estrangeiras (FK)**. Ordem correta:

1. **Entidades fortes** (não dependem de ninguém) — primeiro
2. **Entidades fracas** (dependem de outra) — depois
3. **Entidades associativas** (N:N) — por último

Isso evita **erros de violação de constraints** (restrições de integridade).

**📦 Exemplo — Fábrica de Autopeças:**

```
Cliente → Vendedor → Depósito → Pedido → Peça → Pedido_Peça (associativa)
```

A tabela `Pedido_Peça` depende de `Pedido` e `Peça`, então vem por último.

**Trecho do script (Oracle):**

```sql
CREATE TABLE CLIENTE (
  Cod_do_Cliente number(5) PRIMARY KEY,
  Nome_do_Cliente varchar2(50),
  Endereco_do_Cliente varchar2(50),
  Limite_de_Credito number(9,2),
  Faturamento_Acumulado number(9,2)
);

CREATE TABLE PEDIDO (
  Cod_do_Pedido number(5) PRIMARY KEY,
  Cod_do_Cliente number(5) REFERENCES Cliente (Cod_do_Cliente),
  Cod_do_Vendedor number(5) REFERENCES Vendedor (Cod_do_Vendedor),
  Data_do_Pedido date
);
```

### ![](https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1683312869705-GEs18q9Fiz.png)
---

## 9. Técnica Alternativa (muito usada)

Para **não se preocupar com a ordem** em bancos grandes:

1. Cria todas as tabelas **sem constraints**
2. Depois adiciona as PKs e FKs com `ALTER TABLE`

**Exemplo:**

```sql
ALTER TABLE Pedido
ADD CONSTRAINT pk_pedido PRIMARY KEY (id_pedido);
```

👉 Isso facilita muito quando o banco é grande.

---

## 10. População das Tabelas

Depois de criar, o banco é preenchido com **INSERT + COMMIT**.

⚠️ **Cuidado:** insira nas FKs apenas códigos que **já existem como PK**, senão dá **erro de violação de chave estrangeira**.

---

## 11. Conexão entre os Níveis (a escada completa)

Os níveis formam uma **escada de abstração** (do mais "abstrato" ao mais "concreto"):

1. **Conceitual** → desenha a ideia (entidades, atributos, relacionamentos, cardinalidade)
2. **Relacionamentos e Chaves** → define quantos de cada lado e onde fica cada FK
3. **Lógico** → transforma o desenho em tabelas, tipos de dados, PKs e FKs
4. **Físico** → escreve os scripts e cria o banco de verdade

**Frase-chave:** o conceitual é o **quê**, os relacionamentos definem **quanto**, o lógico é o **como organizar**, e o físico é o **construir**.

---

## 📋 Resumindo

- **MER Físico** = banco implementado, **dependente do SGBD**, usa **SQL**
- Define **performance, integridade e armazenamento**
- **Restrições:** PK, FK, NOT NULL, UNIQUE
- **Regras de nomenclatura:** sem número no início, sem palavras reservadas, só `_`, `$`, `#`
- **Ordem de criação:** fortes → fracas → associativas
- **Técnica alternativa:** criar sem constraints e ajustar com `ALTER TABLE`
- **Conexão:** conceitual → relacionamentos → lógico → físico = do desenho ao banco pronto