# 6_🎯_Simulador_Ético.py
import streamlit as st
import pandas as pd

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_excel("data/Datos_STOXX50_.xlsx")

df = load_data()

# Título
st.set_page_config(layout="wide")
st.title("🎯 Simulador de Inversión Ética Personalizado")

st.markdown("""
Este simulador te permite seleccionar tus preferencias éticas y financieras para recibir una recomendación personalizada de empresas del EURO STOXX 50.
""")

# Sidebar: configuración de preferencias
st.sidebar.header("🔧 Personaliza tu inversión")

# Peso ESG vs Financiero
peso_esg = st.sidebar.slider("¿Qué peso das al componente ESG?", 0, 100, 50)
peso_fin = 100 - peso_esg

# Preferencias ESG
preferencias_esg = st.sidebar.multiselect(
    "¿Qué áreas te importan más?",
    ["Medioambiente", "Social", "Gobernanza"],
    default=["Medioambiente", "Gobernanza"]
)

# Sector preferido
sectores = df["Sector"].dropna().unique().tolist()
sector_sel = st.sidebar.selectbox("📂 Sector preferido (opcional)", ["Todos"] + sectores)

# Nivel de riesgo
riesgo = st.sidebar.radio(
    "⚖️ Nivel de aversión al riesgo",
    ["Alta (prefiero empresas estables)", "Media", "Baja (me arriesgo por más rentabilidad)"]
)

# Verificación de columnas necesarias
columnas_fin = ["Crecimiento", "Rentabilidad", "Valoración", "Apalancamiento"]
columnas_esg = {"Medioambiente": "E", "Social": "S", "Gobernanza": "G"}

if all(col in df.columns for col in columnas_fin):
    df["score_fin"] = df[columnas_fin].mean(axis=1)
else:
    st.error("Faltan columnas financieras en el Excel.")

if all(col in df.columns for col in columnas_esg.values()):
    columnas_usadas = [columnas_esg[c] for c in preferencias_esg]
    df["score_esg"] = df[columnas_usadas].mean(axis=1)
else:
    st.error("Faltan columnas ESG en el Excel.")

# Score combinado total
df["score_total"] = (peso_esg / 100) * df["score_esg"] + (peso_fin / 100) * df["score_fin"]

# Filtro por sector
if sector_sel != "Todos":
    df = df[df["Sector"] == sector_sel]

# Filtro por nivel de riesgo
if "Volatilidad" in df.columns:
    if riesgo == "Alta (prefiero empresas estables)":
        df = df[df["Volatilidad"] < df["Volatilidad"].quantile(0.33)]
    elif riesgo == "Baja (me arriesgo por más rentabilidad)":
        df = df[df["Volatilidad"] > df["Volatilidad"].quantile(0.66)]
else:
    st.warning("No se encontró la columna 'Volatilidad'. No se aplicará filtro de riesgo.")

# Mostrar resultados
st.markdown("---")
st.subheader("🏅 Recomendación de empresas para ti")

if not df.empty:
    resultado = df.sort_values("score_total", ascending=False).head(3)
    st.dataframe(resultado[["Nombre", "País", "Sector", "score_esg", "score_fin", "score_total"]].round(2))
    st.success("Recomendación generada con éxito. Puedes ajustar tus preferencias para explorar más posibilidades.")
else:
    st.warning("No hay empresas que cumplan con los filtros seleccionados.")
