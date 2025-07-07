# 2_📈_Comparativa_Index.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Configuración inicial de la página
st.set_page_config(page_title="Comparativa con el Índice", layout="wide")
st.title("📈 Comparativa entre las Top 5 Acciones y el EURO STOXX 50")

# Introducción explicativa para contextualizar esta sección
st.markdown("""
Esta sección permite comparar las **5 mejores acciones seleccionadas** frente al conjunto total del índice EURO STOXX 50. 

Se analizan métricas promedio por categoría, mostrando si las Top 5 realmente superan al índice de forma significativa o no.
""")

# Cargar los resultados previamente calculados
@st.cache_data
def cargar_resultados():
    try:
        df = pd.read_excel("data/Datos_STOXX50_.xlsx", header=0)
        df['Año'] = pd.to_datetime(df['Año'], errors='coerce').dt.year
        df.dropna(subset=['Año'], inplace=True)
        return df
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame()

# Diccionario con categorías y métricas
CATEGORIAS = {
    'Crecimiento': ['Revenue', 'EPS'],
    'Rentabilidad': ['ROE', 'EBITDA Margin'],
    'Valoración': ['P/E Ratio'],
    'Apalancamiento': ['WACC'],
    'ESG': ['ESG Score', 'Governance Score']
}

# Cargar los datos
df = cargar_resultados()

if not df.empty:
    available_years = sorted(df['Año'].dropna().unique())
    year = st.selectbox("Selecciona un año para la comparación:", options=available_years)
    df_year = df[df['Año'] == year]

    # Obtener todas las empresas
    empresas = df_year['Nombre'].dropna().unique().tolist()
    resumen_empresas = {}

    for empresa in empresas:
        resumen_empresas[empresa] = {}
        df_empresa = df_year[df_year['Nombre'] == empresa]
        for categoria, metricas in CATEGORIAS.items():
            for metrica in metricas:
                if metrica in df_empresa.columns:
                    resumen_empresas[empresa][f"{categoria} - {metrica}"] = df_empresa[metrica].mean()

    # Convertir a DataFrame
    resumen_df = pd.DataFrame(resumen_empresas).T.dropna(axis=1, how='all')

    # Calcular promedio general del índice
    promedio_index = resumen_df.mean()

    # Selección Top 5 (simulada)
    top5 = resumen_df.sum(axis=1).sort_values(ascending=False).head(5).index.tolist()
    top5_df = resumen_df.loc[top5]

    # Promedio Top 5
    promedio_top5 = top5_df.mean()

    # Comparación visual
    comparativa = pd.DataFrame({
        'Top 5': promedio_top5,
        'STOXX 50': promedio_index
    })
    comparativa['Diferencia %'] = 100 * (comparativa['Top 5'] - comparativa['STOXX 50']) / comparativa['STOXX 50']
    comparativa = comparativa.reset_index().rename(columns={'index': 'Métrica'})

    # Mostrar tabla
    st.subheader("📊 Comparación de Promedios por Métrica")
    st.dataframe(comparativa, use_container_width=True)

    # Gráfico de barras
    fig = go.Figure()
    fig.add_trace(go.Bar(x=comparativa['Métrica'], y=comparativa['STOXX 50'], name='STOXX 50', marker_color='lightgray'))
    fig.add_trace(go.Bar(x=comparativa['Métrica'], y=comparativa['Top 5'], name='Top 5', marker_color='darkblue'))
    fig.update_layout(barmode='group', xaxis_title='Métrica', yaxis_title='Valor Promedio')
    st.plotly_chart(fig, use_container_width=True)

    # Gráfico de mejora porcentual
    fig2 = px.bar(comparativa, x='Métrica', y='Diferencia %', color='Diferencia %', color_continuous_scale='Blues',
                  title='Diferencia porcentual: Top 5 vs STOXX 50')
    fig2.update_traces(texttemplate='%{y:.2f}%', textposition='outside')
    st.plotly_chart(fig2, use_container_width=True)

else:
    st.warning("No se pudieron cargar datos para mostrar comparación.")
