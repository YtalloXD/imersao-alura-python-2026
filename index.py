import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
# Define o título da página, o ícone e o layout para ocupar a largura inteira.
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)

# --- Carregamento dos dados ---
csv_path = './docs/data_imersao_2026.csv'
df = pd.read_csv(csv_path)
# df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")
print(df.head())

# --- Barra Lateral (Filtros) ---
st.sidebar.header("🔍 Filtros")

# Filtro de Ano
work_year_available = sorted(df['work_year'].unique())
work_year_available = st.sidebar.multiselect("Ano", work_year_available, default=work_year_available)

# Filtro de Senioridade
experience_level_selected = sorted(df['experience_level'].unique())
experience_level_selected = st.sidebar.multiselect("Experience level", experience_level_selected, default=experience_level_selected)

# Filtro por Tipo de Contrato
job_title_available = sorted(df['job_title'].unique())
job_title_available = st.sidebar.multiselect("Tipo de Contrato", job_title_available, default=job_title_available)

# Filtro por Tamanho da Empresa
company_size_available = sorted(df['company_size'].unique())
company_size_available = st.sidebar.multiselect("Tamanho da Empresa", company_size_available, default=company_size_available)


# --- Filtragem do DataFrame ---
# O dataframe principal é filtrado com base nas seleções feitas na barra lateral.
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
st.subheader("Métricas gerais (Salário anual em USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['salary_in_usd'].mean()
    salario_maximo = df_filtrado['salary_in_usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["job_title"].mode()[0]
else:
    salario_medio, salario_mediano, salario_maximo, total_registros, cargo_mais_comum = 0, 0, 0, ""

col1, col2, col3, col4 = st.columns(4)
col1.metric("Salário médio", f"${salario_medio:,.0f}")
col2.metric("Salário máximo", f"${salario_maximo:,.0f}")
col3.metric("Total de registros", f"{total_registros:,}")
col4.metric("Cargo mais frequente", cargo_mais_frequente)

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
st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('job_title')['salary_in_usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
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
        remoto_contagem = df_filtrado['remote_ratio'].value_counts().reset_index()
        remoto_contagem.columns = ['employment_type', 'quantity']
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
        # Contagem de funcionários por país (todas as ocupações)
        contagem_paises = df_filtrado.groupby('employee_country').size().reset_index(name='employee_count')
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
st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)
     