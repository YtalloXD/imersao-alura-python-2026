"""Dashboard de Análise de Salários na Área de Dados

Este aplicativo Streamlit exibe uma análise interativa dos salários
na área de dados, permitindo filtrar e visualizar dados através de gráficos.
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
# Define as configurações de metadados e layout do aplicativo Streamlit.
# layout='wide' permite usar toda a largura da tela para os conteúdos.
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)

# --- Carregamento dos Dados ---
# Carrega o arquivo CSV contendo os dados de salários na área de dados.
# O dataframe 'df' é o dataset principal utilizado em todo o aplicativo.
csv_path = './docs/data_imersao_2026.csv'
df = pd.read_csv(csv_path)
# Alternativa: carregar dados de uma URL remota
# df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")
print(df.head())  # Exibe as primeiras 5 linhas para verificação

# --- Barra Lateral (Filtros) ---
# A barra lateral oferece controles interativos para filtrar os dados.
# Todos os filtros têm valores padrão selecionados (mostram todos os dados).
# Os usuários podem desselecionar opções para refinar a análise.

st.sidebar.header("🔍 Filtros")

# Filtro de Ano: permite selecionar um ou mais anos para análise
work_year_available = sorted(df['work_year'].unique())
work_year_available = st.sidebar.multiselect("Ano", work_year_available, default=work_year_available)

# Filtro de Senioridade: Junior, Pleno, Senior, Executive, etc.
experience_level_selected = sorted(df['experience_level'].unique())
experience_level_selected = st.sidebar.multiselect("Experience level", experience_level_selected, default=experience_level_selected)

# Filtro por Cargo: permite selecionar tipos de cargos específicos
job_title_available = sorted(df['job_title'].unique())
job_title_available = st.sidebar.multiselect("Tipo de Contrato", job_title_available, default=job_title_available)

# Filtro por Tamanho da Empresa: Small, Medium, Large
company_size_available = sorted(df['company_size'].unique())
company_size_available = st.sidebar.multiselect("Tamanho da Empresa", company_size_available, default=company_size_available)


# --- Filtragem do DataFrame ---
# Aplica todos os filtros selecionados pelo usuário ao dataset principal.
# O resultado é armazenado em 'df_filtrado' para uso nas visualizações e métricas.
df_filtrado = df[
    (df['work_year'].isin(work_year_available)) &
    (df['experience_level'].isin(experience_level_selected)) &
    (df['job_title'].isin(job_title_available)) &
    (df['company_size'].isin(company_size_available))
]

# --- Conteúdo Principal ---
st.title("🎲 Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")

# --- Métricas Principais (KPIs) ---
# Exibe indicadores-chave de desempenho (salário médio, máximo, etc.)
# Estas métricas são recalculadas dinamicamente conforme os filtros mudam.
st.subheader("Métricas gerais (Salário anual em USD)")

if not df_filtrado.empty:
    # Calcula as métricas baseadas nos dados filtrados
    salario_medio = df_filtrado['salary_in_usd'].mean()  # Média salarial
    salario_maximo = df_filtrado['salary_in_usd'].max()  # Maior salário
    total_registros = df_filtrado.shape[0]  # Total de registros
    cargo_mais_frequente = df_filtrado["job_title"].mode()[0]  # Cargo mais comum
else:
    # Define valores padrão se não houver dados para exibir
    salario_medio, salario_mediano, salario_maximo, total_registros, cargo_mais_comum = 0, 0, 0, ""

# Divide a tela em 4 colunas e exibe cada métrica em formato de card
col1, col2, col3, col4 = st.columns(4)
col1.metric("Salário médio", f"${salario_medio:,.0f}")  # Valor médio dos salários
col2.metric("Salário máximo", f"${salario_maximo:,.0f}")  # Maior valor salarial
col3.metric("Total de registros", f"{total_registros:,}")  # Quantidade de registros
col4.metric("Cargo mais frequente", cargo_mais_frequente)  # Ocupação mais comum

with st.expander("+Info"):
    st.markdown(
        """
        Este dashboard foi desenvolvido para analisar os salários na área de dados com base em um conjunto de dados abrangente. 
        Utilize os filtros disponíveis na barra lateral para explorar diferentes aspectos dos dados salariais.
        
        **Fonte dos Dados:** [Kaggle - Data Science Salary Data](https://www.kaggle.com/datasets/ruchi798/data-science-salary-data)
        
        **Tecnologias Utilizadas:** Streamlit, Pandas, Plotly
        
        **Desenvolvedor:** Reginaldo Ytalo
        
        **Contato:** [LinkedIn](https://www.linkedin.com/in/reginaldo-ytalo-felix-mota/)
        """
    )
    st.image('https://media.licdn.com/dms/image/v2/D4D03AQFHAa6AjCDcpA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1727807393346?e=1771459200&v=beta&t=26aqC4zLTbLiiodX4-I6YSZYjIpeAu_tHaKmSOrJnmo', width=200)

st.markdown("---")


# --- Análises Visuais com Plotly ---
# Exibe 4 gráficos interativos para visualizar diferentes aspectos dos dados.
# Cada gráfico é responsivo e se adapta ao tamanho da tela.
st.subheader("Gráficos")

# Primeira linha de gráficos: Cargos top 10 e Distribuição de Salários
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtrado.empty:
        # Agrupa os dados por cargo e calcula o salário médio de cada um
        # Depois seleciona os 10 maiores e ordena de forma crescente para melhor visualização
        top_cargos = df_filtrado.groupby('job_title')['salary_in_usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        # Cria um gráfico de barras horizontal mostrando os top 10 cargos por salário
        grafico_cargos = px.bar(
            top_cargos,
            x='salary_in_usd',
            y='job_title',
            orientation='h',
            title="Top 10 cargos por salário médio",
            labels={'salary_in_usd': 'Média salarial anual (USD)', 'job_title': ''}
        )
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")

with col_graf2:
    if not df_filtrado.empty:
        # Cria um histograma mostrando a distribuição de salários
        # nbins=30 define 30 intervalos para melhor visualização da distribuição
        grafico_hist = px.histogram(
            df_filtrado,
            x='salary_in_usd',
            nbins=30,
            title="Distribuição de salários anuais",
            labels={'salary_in_usd': 'Faixa salarial (USD)', 'count': ''}
        )
        grafico_hist.update_layout(title_x=0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        # Conta o número de registros por tipo de trabalho (Remote, On-site, etc.)
        remoto_contagem = df_filtrado['remote_ratio'].value_counts().reset_index()
        # Renomeia as colunas para melhor compreensão
        remoto_contagem.columns = ['employment_type', 'quantity']
        # Cria um gráfico de pizza mostrando a proporção de cada tipo de trabalho
        grafico_remoto = px.pie(
            remoto_contagem,
            names='employment_type',
            values='quantity',
            title='Proporção dos tipos de trabalho',
            hole=0.5
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

with col_graf4:
    if not df_filtrado.empty:
        # Conta o número de funcionários por país (independente da ocupação)
        # A função size() conta o número de linhas em cada grupo
        contagem_paises = df_filtrado.groupby('employee_country').size().reset_index(name='employee_count')
        # Cria um mapa coroplético (choropleth) mostrando a distribuição global de funcionários
        # A cor mais intensa indica maior quantidade de funcionários
        grafico_paises = px.choropleth(
            contagem_paises,
            locations='employee_country',
            color='employee_count',
            color_continuous_scale='Blues',
            title='Número de funcionários por país',
            labels={'employee_count': 'Quantidade de funcionários', 'employee_country': 'País'}
        )
        grafico_paises.update_layout(title_x=0.1)
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.")

# --- Tabela de Dados Detalhados ---
# Exibe a tabela completa dos dados filtrados para inspeção detalhada
# A tabela é interativa e permite ordenar/filtrar diretamente no Streamlit
st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)
     