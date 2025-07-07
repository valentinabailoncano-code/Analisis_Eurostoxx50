# 1_📊_Top_5_Acciones.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import re

# Configuración de la página
st.set_page_config(page_title="Top 5 Acciones", layout="wide")
st.title("📊 Selección de las Top 5 Acciones del EURO STOXX 50")

# Explicación inicial para el usuario
st.markdown("""
En esta sección se identifican las **5 mejores acciones** del índice EURO STOXX 50 mediante un modelo de puntuación que integra métricas financieras y de sostenibilidad (ESG).

Puedes seleccionar un año específico o considerar todos los disponibles para obtener una visión más global.
""")

# Cargar los datos desde el Excel preparado previamente
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("data/Datos_STOXX50_.xlsx", header=[0, 1])
        df.columns = [(str(a), str(b)) for a, b in df.columns]  # asegurar consistencia
        df[('Fecha', 'Año')] = pd.to_datetime(df[('Fecha', 'Año')], errors='coerce')
        df.dropna(subset=[('Fecha', 'Año')], inplace=True)
        df[('Fecha', 'Año')] = df[('Fecha', 'Año')].dt.year
        return df
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame()

# Función para normalizar métricas con dirección (más alto = mejor o viceversa)
def normalize(series, inverse=False):
    series = series.astype(float)
    if inverse:
        return 1 - (series - series.min()) / (series.max() - series.min())
    else:
        return (series - series.min()) / (series.max() - series.min())

# Diccionario con pesos y sentido de cada categoría
CATEGORIAS = {
    'Crecimiento': {
        'metricas': ['Revenue', 'EPS'],
        'peso': 0.15,
        'inverse': False
    },
    'Rentabilidad': {
        'metricas': ['ROE', 'EBITDA Margin'],
        'peso': 0.20,
        'inverse': False
    },
    'Valoración': {
        'metricas': ['P/E Ratio'],
        'peso': 0.15,
        'inverse': True  # menor P/E es mejor
    },
    'Apalancamiento': {
        'metricas': ['WACC'],
        'peso': 0.05,
        'inverse': True
    },
    'ESG': {
        'metricas': ['ESG Score', 'Governance Score'],
        'peso': 0.45,
        'inverse': False
    }
}

# Cargar los datos
df = load_data()

if not df.empty:
    # Obtener años únicos disponibles
    available_years = sorted(df[('Fecha', 'Año')].dropna().unique())
    selected_year = st.selectbox("Selecciona un año específico para el análisis:", options=["Todos"] + available_years)

    # Filtrar por año si no es "Todos"
    if selected_year != "Todos":
        df = df[df[('Fecha', 'Año')] == selected_year]

    # Extraer lista de empresas (niveles del primer nivel de columnas)
    tickers = sorted(set([col[0] for col in df.columns if col[0] not in ['Fecha']]))
    resultados = []

    for ticker in tickers:
        puntuacion_total = 0
        detalles_categoria = {}

        for categoria, info in CATEGORIAS.items():
            puntuaciones = []
            for metrica in info['metricas']:
                columnas_filtradas = [col for col in df.columns if col[0] == ticker and re.search(metrica, col[1], re.IGNORECASE)]
                for col in columnas_filtradas:
                    serie = df[col].copy()
                    normalizada = normalize(serie, inverse=info['inverse'])
                    media = normalizada.mean()
                    puntuaciones.append(media)
            if puntuaciones:
                score_cat = np.mean(puntuaciones)
                detalles_categoria[categoria] = score_cat
                puntuacion_total += score_cat * info['peso']

        resultados.append({
            'Ticker': ticker,
            'Puntuación Total': puntuacion_total,
            **detalles_categoria
        })

    # Crear DataFrame con resultados
    resultados_df = pd.DataFrame(resultados).sort_values(by='Puntuación Total', ascending=False).reset_index(drop=True)
    top5_df = resultados_df.head(5)

    # Mostrar tabla de resultados
    st.subheader("🏆 Ranking: Top 5 Acciones")
    st.dataframe(top5_df, use_container_width=True)

    # Gráfico de barras de puntuación
    fig = px.bar(top5_df,
                 x='Ticker',
                 y='Puntuación Total',
                 color='Puntuación Total',
                 color_continuous_scale='Viridis',
                 text='Puntuación Total',
                 title='Puntuaciones Totales por Empresa')
    fig.update_traces(texttemplate='%{text:.3f}', textposition='outside')
    fig.update_layout(xaxis_title='Empresa', yaxis_title='Puntuación', height=500)
    st.plotly_chart(fig, use_container_width=True)

    # Desglose por categoría
    st.subheader("📂 Detalle por Categoría (Top 5)")
    st.dataframe(top5_df.drop(columns=['Puntuación Total']), use_container_width=True)

else:
    st.warning("No se encontraron datos válidos para mostrar.")