# 1_📊_Top_5_Acciones.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Top 5 Acciones", layout="wide")
st.title("📊 Selección de las Top 5 Acciones del EURO STOXX 50")

st.markdown("""
En esta sección se identifican las **5 mejores acciones** del índice EURO STOXX 50 mediante un modelo de puntuación que integra métricas financieras y de sostenibilidad (ESG).

Puedes seleccionar un año específico o considerar todos los disponibles para obtener una visión más global.
""")

# Cargar los datos desde el Excel preparado previamente
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("data/Datos_STOXX50_.xlsx", sheet_name="Financiero")
        df["Fecha"] = pd.to_datetime(df["Dates"], errors='coerce')
        df.dropna(subset=["Fecha"], inplace=True)
        df["Año"] = df["Fecha"].dt.year
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

# Diccionario con pesos y sentido de cada categoría para RACE IM
CATEGORIAS = {
    'Rentabilidad': {
        'metricas': ['RACE IM  .6', 'RACE IM  .7'],  # ROE, ROI
        'peso': 0.20,
        'inverse': False
    },
    'Dividendos': {
        'metricas': ['RACE IM  .4'],  # Dividends per Share
        'peso': 0.15,
        'inverse': False
    },
    'Valoración': {
        'metricas': ['RACE IM  '],  # P/E
        'peso': 0.20,
        'inverse': True
    },
    'ESG': {
        'metricas': ['RACE IM  .10', 'RACE IM  .13'],  # ESG simulados
        'peso': 0.45,
        'inverse': False
    }
}

# Cargar los datos
df = load_data()

if not df.empty:
    available_years = sorted(df["Año"].dropna().unique())
    selected_year = st.selectbox("Selecciona un año específico para el análisis:", options=["Todos"] + list(available_years))

    if selected_year != "Todos":
        df = df[df["Año"] == selected_year]

    resultados = []
    ticker = "RACE IM"
    puntuacion_total = 0
    detalles_categoria = {}

    for categoria, info in CATEGORIAS.items():
        puntuaciones = []
        for col in info['metricas']:
            if col in df.columns:
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

    resultados_df = pd.DataFrame(resultados).sort_values(by='Puntuación Total', ascending=False).reset_index(drop=True)
    top5_df = resultados_df.head(5)

    st.subheader("🏆 Ranking: Top 5 Acciones")
    st.dataframe(top5_df, use_container_width=True)

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

    st.subheader("📂 Detalle por Categoría (Top 5)")
    st.dataframe(top5_df.drop(columns=['Puntuación Total']), use_container_width=True)

else:
    st.warning("No se encontraron datos válidos para mostrar.")