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
        df = pd.read_excel("data/Datos_STOXX50_.xlsx", header=[0, 1])
        df.columns = [(str(a), str(b)) for a, b in df.columns]  # estandarizar columnas
        df[('Fecha', 'Año')] = pd.to_datetime(df[('Fecha', 'Año')], errors='coerce')
        df.dropna(subset=[('Fecha', 'Año')], inplace=True)
        df[('Fecha', 'Año')] = df[('Fecha', 'Año')].dt.year
        return df
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame()

# Diccionario con categorías y métricas (igual que en Top 5)
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
    # Obtener tickers y años
    tickers = sorted(set([col[0] for col in df.columns if col[0] != 'Fecha']))
    available_years = sorted(df[('Fecha', 'Año')].dropna().unique())
    year = st.selectbox("Selecciona un año para la comparación:", options=available_years)
    df_year = df[df[('Fecha', 'Año')] == year]

    # Seleccionar las top 5 del año (según alguna métrica sencilla para ejemplo)
    resumen_empresas = {}
    for categoria, metricas in CATEGORIAS.items():
        for metrica in metricas:
            for ticker in tickers:
                columnas = [col for col in df_year.columns if col[0] == ticker and metrica in col[1]]
                for col in columnas:
                    if ticker not in resumen_empresas:
                        resumen_empresas[ticker] = {}
                    resumen_empresas[ticker][f"{categoria} - {metrica}"] = df_year[col].mean()

    # Convertir a DataFrame
    resumen_df = pd.DataFrame(resumen_empresas).T.dropna(axis=1, how='all')

    # Calcular promedio general del índice
    promedio_index = resumen_df.mean()

    # Simular selección de Top 5 (en práctica deberíamos importar del módulo anterior)
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