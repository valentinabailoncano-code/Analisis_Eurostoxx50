# 4_📉_Análisis_Estadístico.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

# Configuración de la página
st.set_page_config(page_title="Análisis Estadístico", layout="wide")
st.title("📉 Análisis Estadístico sobre Empresas del EURO STOXX 50")

# Descripción introductoria
st.markdown("""
En esta sección se exploran **relaciones estadísticas** entre métricas ESG y financieras.

Se aplican herramientas como:
- Histogramas de distribución.
- Matriz de correlación.
- Regresión lineal simple.
- Pruebas de hipótesis estadísticas.
""")

# Cargar datos procesados
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("data/Datos_STOXX50_.xlsx", header=[0, 1])
        df.columns = [(str(a), str(b)) for a, b in df.columns]
        df[('Fecha', 'Año')] = pd.to_datetime(df[('Fecha', 'Año')], errors='coerce')
        df.dropna(subset=[('Fecha', 'Año')], inplace=True)
        df[('Fecha', 'Año')] = df[('Fecha', 'Año')].dt.year
        return df
    except Exception as e:
        st.error(f"Error al cargar datos: {e}")
        return pd.DataFrame()

# Cargar
full_df = load_data()

if not full_df.empty:
    available_years = sorted(full_df[('Fecha', 'Año')].unique())
    year = st.selectbox("Selecciona el año de análisis:", options=available_years)
    df = full_df[full_df[('Fecha', 'Año')] == year].copy()

    # Filtro: buscar columnas ESG y financieras comunes
    posibles_vars = [col for col in df.columns if col[0] not in ['Fecha'] and df[col].dtype in [np.float64, np.int64]]
    vars_dict = {f"{col[0]} - {col[1]}": col for col in posibles_vars}

    # Selección de variables para análisis
    st.markdown("---")
    var_x = st.selectbox("Variable X (independiente)", options=vars_dict.keys())
    var_y = st.selectbox("Variable Y (dependiente)", options=vars_dict.keys(), index=1)

    col_x = vars_dict[var_x]
    col_y = vars_dict[var_y]

    # Crear DataFrame limpio para análisis
    df_simple = df[[col_x, col_y]].dropna()
    df_simple.columns = ['X', 'Y']

    # Mostrar distribuciones
    st.subheader("📊 Histogramas")
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.histogram(df_simple, x='X', nbins=20, title=f'Distribución de {var_x}')
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = px.histogram(df_simple, x='Y', nbins=20, title=f'Distribución de {var_y}')
        st.plotly_chart(fig2, use_container_width=True)

    # Matriz de correlación
    st.subheader("🔗 Matriz de Correlación")
    all_numeric = df[[col for col in posibles_vars]].copy()
    corr_df = all_numeric.corr()
    fig_corr, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr_df, cmap="coolwarm", annot=False, fmt=".2f", ax=ax)
    st.pyplot(fig_corr)

    # Regresión lineal simple
    st.subheader("📐 Regresión Lineal Simple")
    slope, intercept, r_value, p_value, std_err = stats.linregress(df_simple['X'], df_simple['Y'])
    df_simple['Pred'] = intercept + slope * df_simple['X']
    r2 = r_value ** 2

    # Mostrar resultados
    st.markdown(f"**Ecuación estimada:**  Y = {intercept:.3f} + {slope:.3f}·X")
    st.markdown(f"**R² =** {r2:.4f}  |  **p-valor =** {p_value:.4e}")

    # Gráfico con predicción
    fig3 = px.scatter(df_simple, x='X', y='Y', trendline="ols",
                      title=f'Regresión entre {var_x} y {var_y}')
    st.plotly_chart(fig3, use_container_width=True)

    # Interpretación textual
    st.markdown("""
    > 🔍 **Interpretación:** Si el valor de R² es cercano a 1 y el p-valor es menor a 0.05,
    se puede considerar que existe una relación estadísticamente significativa entre las variables.
    """)

else:
    st.warning("No hay datos válidos para análisis en este año.")
