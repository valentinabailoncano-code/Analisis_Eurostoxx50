# 4_📉_Análisis_Estadístico.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

# Configuración
st.set_page_config(page_title="Análisis Estadístico", layout="wide")
st.title("📉 Análisis Estadístico de RACE IM")

st.markdown("""
En esta sección se exploran **relaciones estadísticas** entre las métricas financieras y sostenibles de **RACE IM** a lo largo del tiempo.

Se aplican herramientas como:
- Histogramas
- Regresión lineal
- Correlaciones entre variables
""")

# Cargar datos simulados de RACE IM
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("data/Datos_STOXX50_.xlsx", sheet_name="Financiero")
        df["Fecha"] = pd.to_datetime(df["Dates"], errors='coerce')
        df.dropna(subset=["Fecha"], inplace=True)
        df["Año"] = df["Fecha"].dt.year
        df["ESG"] = df[["RACE IM  .10", "RACE IM  .13"]].mean(axis=1)
        return df
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame()

df = load_data()

# Selección de año (para filtrar si se desea)
años = sorted(df["Año"].unique())
año_sel = st.selectbox("Selecciona un año para análisis:", options=["Todos"] + años)

if año_sel != "Todos":
    df = df[df["Año"] == año_sel]

# Variables disponibles
variables = {
    "Dividendos": "RACE IM  .4",
    "ROE": "RACE IM  .6",
    "ROI": "RACE IM  .7",
    "P/E Ratio": "RACE IM  ",
    "ESG Score": "ESG"
}

# Selección de variables para análisis
col1, col2 = st.columns(2)
with col1:
    var_x = st.selectbox("Variable X (independiente)", list(variables.keys()))
with col2:
    var_y = st.selectbox("Variable Y (dependiente)", list(variables.keys()), index=1)

# Crear DataFrame para análisis
if variables[var_x] in df.columns and variables[var_y] in df.columns:
    df_simple = df[[variables[var_x], variables[var_y]]].dropna()
    df_simple.columns = ['X', 'Y']

    # Histogramas
    st.subheader("📊 Distribuciones")
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(px.histogram(df_simple, x="X", nbins=10, title=f"Distribución de {var_x}"), use_container_width=True)
    with c2:
        st.plotly_chart(px.histogram(df_simple, x="Y", nbins=10, title=f"Distribución de {var_y}"), use_container_width=True)

    # Correlación simple
    corr_val = df_simple.corr().iloc[0, 1]
    st.subheader("🔗 Correlación de Pearson")
    st.write(f"**Coeficiente de correlación (r):** {corr_val:.4f}")

    # Regresión lineal
    st.subheader("📐 Regresión Lineal")
    slope, intercept, r_value, p_value, std_err = stats.linregress(df_simple['X'], df_simple['Y'])
    df_simple["Pred"] = intercept + slope * df_simple["X"]

    st.markdown(f"**Ecuación:** Y = {intercept:.3f} + {slope:.3f}·X")
    st.markdown(f"**R² =** {r_value**2:.4f} | **p-valor =** {p_value:.4e}")

    fig = px.scatter(df_simple, x="X", y="Y", trendline="ols", title="Regresión lineal")
    st.plotly_chart(fig, use_container_width=True)

    # Interpretación
    st.markdown("""
    > 🔍 **Nota:** Si el p-valor es menor a 0.05 y R² es alto, la relación entre las variables podría ser significativa.
    """)
else:
    st.warning("Las variables seleccionadas no están disponibles.")
