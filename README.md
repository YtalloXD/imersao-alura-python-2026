# Dashboard de Análise de Salários na Área de Dados 📊

Um aplicativo interativo construído com **Streamlit** para análise e visualização de dados salariais na área de dados e tecnologia. O dashboard oferece filtros dinâmicos, métricas de KPI e visualizações gráficas para explorar tendências salariais globais.

## 📋 Funcionalidades

- **Filtros Interativos**: Filtre dados por ano, nível de experiência, cargo e tamanho da empresa
- **Métricas Principais**: Visualize salário médio, salário máximo, total de registros e cargo mais frequente
- **Gráficos Visuais**:
  - Top 10 cargos por salário médio (gráfico de barras)
  - Distribuição de salários (histograma)
  - Proporção de tipos de trabalho (gráfico de pizza)
  - Número de funcionários por país (mapa coropletico)
- **Tabela Detalhada**: Exiba e inspecione todos os dados filtrados

## 🛠️ Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **pip** (gerenciador de pacotes Python - geralmente incluído com Python)
- **Git** (opcional, para clonar o repositório)

## 📦 Estrutura do Projeto

```
imersao-pythondados/
├── index.py                          # Arquivo principal do aplicativo
├── requirements.txt                  # Dependências do projeto
├── docs/
│   └── data_imersao_2026.csv        # Dataset com dados salariais
└── README.md                         # Este arquivo
```

## 🚀 Instalação e Execução

### 1. Clone ou Baixe o Repositório

```bash
# Via Git (se preferir)
git clone <url-do-repositorio>
cd imersao-pythondados
```

Ou simplesmente baixe os arquivos e navegue até a pasta do projeto.

### 2. Crie um Ambiente Virtual (Recomendado)

Um ambiente virtual isola as dependências do projeto de outras instalações Python.

**No Windows (PowerShell ou CMD):**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**No macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as Dependências

Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

Este comando instala as seguintes bibliotecas:

- **pandas** (2.2.3) - Manipulação e análise de dados
- **streamlit** (1.44.1) - Framework para criar aplicativos web
- **plotly** (5.24.1) - Criação de gráficos interativos

### 4. Execute o Aplicativo

```bash
streamlit run index.py
```

O aplicativo abrirá automaticamente no seu navegador padrão (geralmente em `http://localhost:8501`).

## 📊 Usando o Dashboard

### Filtros Disponíveis

Na barra lateral esquerda, você encontrará os seguintes filtros:

1. **Ano**: Selecione um ou mais anos para análise (padrão: todos os anos)
2. **Experience level**: Filtre por nível de experiência (Junior, Pleno, Senior, Executive)
3. **Tipo de Contrato**: Escolha cargos/posições específicas
4. **Tamanho da Empresa**: Selecione Small, Medium ou Large

### Interpretando os Dados

O dataset contém as seguintes colunas:

| Coluna             | Descrição                                         |
| ------------------ | ------------------------------------------------- |
| `work_year`        | Ano do registro                                   |
| `experience_level` | Nível de experiência profissional                 |
| `employment_type`  | Tipo de contrato (Full-time, Part-time, Contract) |
| `job_title`        | Cargo/Posição profissional                        |
| `salary`           | Salário em moeda local                            |
| `salary_currency`  | Código da moeda (USD, GBP, EUR, etc.)             |
| `salary_in_usd`    | Salário convertido para USD                       |
| `employee_country` | País do funcionário                               |
| `remote_ratio`     | Tipo de trabalho (Remote, On-site)                |
| `company_country`  | País da empresa                                   |
| `company_size`     | Tamanho da empresa                                |

## 📝 Exemplos de Uso

### Exemplo 1: Analisar Salários de Data Engineers em 2025

1. Na barra lateral, deixe **Ano** como 2025
2. Em **Tipo de Contrato**, selecione apenas "Data Engineer"
3. Observe os gráficos atualizando automaticamente com dados filtrados

### Exemplo 2: Comparar Salários entre Níveis de Experiência

1. Use apenas o filtro **Experience level** para selecionar níveis específicos
2. O gráfico de top 10 cargos mostrará a diferença salarial entre os níveis

## 🔧 Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'streamlit'"

**Solução**: Certifique-se de que o ambiente virtual está ativado e execute `pip install -r requirements.txt` novamente.

### Problema: O aplicativo não abre no navegador

**Solução**: Abra manualmente em seu navegador em `http://localhost:8501`

### Problema: Erro ao carregar dados do CSV

**Solução**: Verifique se o arquivo `docs/data_imersao_2026.csv` existe no diretório correto.

## 📚 Dependências

### pandas (2.2.3)

Biblioteca para manipulação e análise de dados. Usada para:

- Carregar dados do CSV
- Filtrar e agrupar dados
- Calcular métricas (média, máximo, contagem)

### streamlit (1.44.1)

Framework web que simplifica a criação de dashboards. Usado para:

- Interface da barra lateral
- Exibição de métricas (KPIs)
- Renderização de gráficos
- Tabelas interativas

### plotly (5.24.1)

Biblioteca de visualização de dados. Usada para criar:

- Gráficos de barras
- Histogramas
- Gráficos de pizza
- Mapas coropléticos (coropleth maps)

## 🌐 Alternativa: Carregar Dados de URL Remota

Se preferir usar dados de uma URL remota em vez do arquivo local, você pode descomentar a linha no `index.py`:

```python
# df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")
```

## 📄 Fonte dos Dados

**Dataset Original**: [Dashboard - Dados de salários](https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv)

Os dados incluem informações de salários na área de dados de 2025, com representação global de múltiplos países.

## 👤 Desenvolvedor

**Reginaldo Ytalo**

- LinkedIn: [Reginaldo Ytalo Felix Mota](https://www.linkedin.com/in/reginaldo-ytalo-felix-mota/)

## 📄 Licença

Este projeto é fornecido como está para fins educacionais e de análise.

---

**Desenvolvido com ❤️ usando Streamlit, Pandas e Plotly**
