# 10_🌍_Comparativa_Índices.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Comparativa de Índices", layout="wide")
st.title("🌍 Comparativa: EURO STOXX 50 vs IBEX 35 vs S&P 500")

# Introducción
st.markdown("""
En esta sección comparamos los promedios de métricas clave entre tres grandes índices bursátiles: **EURO STOXX 50**, **IBEX 35** y **S&P 500**.  
Los datos son simulados, pero replican comportamientos reales para fines académicos y de análisis comparativo.
""")

# Datos simulados
data = {
    "Índice": ["EURO STOXX 50", "IBEX 35", "S&P 500"],
    "Crecimiento": [6.2, 5.0, 8.5],
    "Rentabilidad": [7.1, 6.8, 9.3],
    "Valoración": [5.5, 6.0, 7.8],
    "Apalancamiento": [3.2, 3.8, 2.9],
    "E": [68, 59, 73],
    "S": [65, 57, 71],
    "G": [70, 60, 75]
}
df = pd.DataFrame(data)
df["ESG"] = df[["E", "S", "G"]].mean(axis=1)

# Métricas disponibles
metricas = ["Crecimiento", "Rentabilidad", "Valoración", "Apalancamiento", "E", "S", "G", "ESG"]
metrica_sel = st.selectbox("Selecciona una métrica para comparar:", metricas)

# Gráfico comparativo
fig = px.bar(
    df,
    x="Índice",
    y=metrica_sel,
    color="Índice",
    text_auto=True,
    title=f"Comparativa de {metrica_sel} entre índices",
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig.update_layout(yaxis_title=metrica_sel, xaxis_title="Índice", height=500)
st.plotly_chart(fig, use_container_width=True)

# Tabla con métricas
st.markdown("---")
st.subheader("📋 Detalle completo por índice")
st.dataframe(df.set_index("Índice").round(2), use_container_width=True)
