# 8_📈_Ranking_ESG_Historico.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("📈 Evolución Histórica ESG")

st.markdown("""
Este módulo permite visualizar cómo han evolucionado las puntuaciones ESG de las empresas del EURO STOXX 50 a lo largo del tiempo.

**Nota:** Este módulo utiliza datos simulados por ahora. Puedes reemplazarlos con valores reales históricos ESG.
""")

# Simulación de datos ESG históricos para demostración
data = {
    "Nombre": ["Adidas", "Adidas", "Adidas", "TotalEnergies", "TotalEnergies", "TotalEnergies"],
    "Año": [2021, 2022, 2023, 2021, 2022, 2023],
    "E": [65, 70, 74, 40, 45, 55],
    "S": [60, 66, 69, 50, 52, 54],
    "G": [70, 75, 78, 45, 50, 58]
}
df = pd.DataFrame(data)
df["ESG_total"] = df[["E", "S", "G"]].mean(axis=1)

# Selección de empresa
empresas = df["Nombre"].unique().tolist()
empresa_sel = st.selectbox("Selecciona una empresa:", empresas)

# Filtrar datos
df_filtrada = df[df["Nombre"] == empresa_sel]

# Gráfico de evolución ESG
fig = px.line(
    df_filtrada,
    x="Año",
    y=["E", "S", "G", "ESG_total"],
    markers=True,
    title=f"Evolución ESG de {empresa_sel}"
)
fig.update_layout(yaxis_title="Puntuación", legend_title="Dimensión ESG")

st.plotly_chart(fig, use_container_width=True)

# Mostrar tabla
st.markdown("---")
st.subheader("📋 Datos ESG por año")
st.dataframe(df_filtrada.round(2))
