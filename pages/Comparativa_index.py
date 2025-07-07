# 2_📈_Comparativa_RACE_IM_vs_Index.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Configuración inicial
st.set_page_config(page_title="Comparativa con el Índice", layout="wide")
st.title("📈 Comparativa entre RACE IM y el Promedio del EURO STOXX 50")

st.markdown("""
Esta sección compara las métricas clave de la empresa **RACE IM** frente al **promedio del índice EURO STOXX 50**.

Se analizan dimensiones como **rentabilidad**, **dividendos**, **valoración** y **ESG**.
""")

# Cargar datos simulados
@st.cache_data
def cargar_datos():
    df = pd.read_excel("data/Datos_STOXX50_.xlsx", sheet_name="Financiero")
    df["Fecha"] = pd.to_datetime(df["Dates"], errors='coerce')
    df.dropna(subset=["Fecha"], inplace=True)
    df["Año"] = df["Fecha"].dt.year
    df["ESG"] = df[["RACE IM  .10", "RACE IM  .13"]].mean(axis=1)
    return df

df = cargar_datos()

# Diccionario con métricas relevantes
METRICAS = {
    "Dividendos": "RACE IM  .4",
    "ROE": "RACE IM  .6",
    "ROI": "RACE IM  .7",
    "Valoración (P/E)": "RACE IM  ",
    "ESG": "ESG"
}

# Años disponibles
años = sorted(df["Año"].unique())
año_sel = st.selectbox("Selecciona un año:", años)
df_year = df[df["Año"] == año_sel]

# Calcular valores
valores_race = {}
valores_index = {}

for etiqueta, columna in METRICAS.items():
    if columna in df.columns:
        valores_race[etiqueta] = df_year[columna].values[0]  # Solo una fila = RACE IM
        valores_index[etiqueta] = df_year[columna].mean()     # Promedio general

# Crear DataFrame comparativo
comparativa = pd.DataFrame({
    "Métrica": list(METRICAS.keys()),
    "RACE IM": list(valores_race.values()),
    "EURO STOXX 50": list(valores_index.values())
})
comparativa["Diferencia %"] = 100 * (comparativa["RACE IM"] - comparativa["EURO STOXX 50"]) / comparativa["EURO STOXX 50"]

# Mostrar tabla
st.subheader("📊 Comparativa por Métrica")
st.dataframe(comparativa.round(2), use_container_width=True)

# Gráfico de comparación
fig = go.Figure()
fig.add_trace(go.Bar(x=comparativa["Métrica"], y=comparativa["EURO STOXX 50"], name="EURO STOXX 50", marker_color="gray"))
fig.add_trace(go.Bar(x=comparativa["Métrica"], y=comparativa["RACE IM"], name="RACE IM", marker_color="darkblue"))
fig.update_layout(barmode='group', xaxis_title="Métrica", yaxis_title="Valor", title="Comparativa entre RACE IM y el índice")
st.plotly_chart(fig, use_container_width=True)

# Gráfico de diferencia porcentual
fig2 = px.bar(comparativa, x="Métrica", y="Diferencia %", color="Diferencia %", color_continuous_scale="Blues",
              title="Diferencia porcentual RACE IM vs EURO STOXX 50")
fig2.update_traces(texttemplate='%{y:.2f}%', textposition='outside')
st.plotly_chart(fig2, use_container_width=True)

