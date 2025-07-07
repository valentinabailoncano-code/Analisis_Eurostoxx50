# 7_📊_Dashboard_KPIs.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard KPIs", layout="wide")

# Título
st.title("📊 Evolución de KPIs de RACE IM")

st.markdown("""
Este dashboard muestra la evolución temporal de indicadores financieros y de sostenibilidad (ESG) de la empresa **RACE IM**, perteneciente al EURO STOXX 50.
""")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_excel("data/Datos_STOXX50_.xlsx", sheet_name="Financiero")
    df["Fecha"] = pd.to_datetime(df["Dates"], errors='coerce')
    df.dropna(subset=["Fecha"], inplace=True)
    df["Año"] = df["Fecha"].dt.year
    return df

df = load_data()

# Diccionario de métricas con nombres legibles
kpi_map = {
    "P/E Ratio": "RACE IM  ",
    "Dividendos por Acción": "RACE IM  .4",
    "ROE (%)": "RACE IM  .6",
    "ROI (%)": "RACE IM  .7",
    "Rentabilidad sobre el Capital (simulada)": "RACE IM  .8",
    "Volatilidad": "RACE IM  .9",
    "Medioambiente (E)": "RACE IM  .10",
    "Social (S)": "RACE IM  .11",
    "Gobernanza (G)": "RACE IM  .13"
}

kpi_seleccionado = st.selectbox("Selecciona el KPI que deseas visualizar:", list(kpi_map.keys()))

columna = kpi_map[kpi_seleccionado]

if columna not in df.columns:
    st.warning("La métrica seleccionada no está disponible para esta empresa.")
else:
    df_kpi = df[["Año", columna]].dropna().sort_values("Año")
    st.line_chart(df_kpi.set_index("Año"), use_container_width=True)

    st.markdown("---")
    st.subheader("📋 Valores históricos del KPI seleccionado")
    st.dataframe(df_kpi.rename(columns={columna: kpi_seleccionado}).reset_index(drop=True).round(2))

