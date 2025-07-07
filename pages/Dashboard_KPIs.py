# 7_📊_Dashboard_KPIs.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_excel("data/Datos_STOXX50_.xlsx")

df = load_data()

# Título de la página
st.title("📊 Dashboard Dinámico de KPIs")

st.markdown("""
Personaliza el análisis seleccionando los indicadores clave (KPIs) que más te interesen. 
Puedes comparar empresas, países o sectores de forma visual e interactiva.
""")

# Opciones disponibles
kpi_disponibles = ["Crecimiento", "Rentabilidad", "Valoración", "Apalancamiento", "E", "S", "G"]
agrupaciones = ["Nombre", "País", "Sector"]

# Selecciones del usuario
col1, col2 = st.columns(2)

with col1:
    kpi_seleccionado = st.selectbox("Selecciona el KPI a visualizar:", kpi_disponibles)

with col2:
    agrupacion = st.selectbox("Agrupar por:", agrupaciones)

# Verificar si las columnas existen antes de agrupar
if agrupacion not in df.columns or kpi_seleccionado not in df.columns:
    st.error("La columna seleccionada no se encuentra en los datos.")
else:
    # Calcular promedio por agrupación
    df_grouped = df.groupby(agrupacion)[kpi_seleccionado].mean().reset_index()

    # Gráfico de barras horizontal
    fig = px.bar(
        df_grouped,
        x=kpi_seleccionado,
        y=agrupacion,
        orientation='h',
        color=kpi_seleccionado,
        color_continuous_scale='Blues',
        title=f"{kpi_seleccionado} promedio por {agrupacion}"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Mostrar tabla de datos
    st.markdown("---")
    st.subheader("📋 Datos detallados")
    st.dataframe(df_grouped.sort_values(kpi_seleccionado, ascending=False).round(2))
