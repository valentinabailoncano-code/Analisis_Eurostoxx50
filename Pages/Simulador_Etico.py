# 6_🎯_Simulador_Ético.py
import streamlit as st
import pandas as pd

# Cargar datos
@st.cache_data

def load_data():
    df = pd.read_excel("data/Datos_STOXX50_.xlsx")
    return df

df = load_data()

# Título de la página
st.title("🎯 Simulador de Inversión Ética Personalizado")

st.markdown("""
Este simulador te permite seleccionar tus preferencias éticas y financieras para recibir una recomendación personalizada de empresas del EURO STOXX 50.
""")

# Filtros de usuario
st.sidebar.header("🔧 Personaliza tu inversión")

# Selección de prioridades ESG
peso_esg = st.sidebar.slider("¿Qué peso das al componente ESG?", 0, 100, 50)
peso_fin = 100 - peso_esg

# Preferencias ESG específicas
preferencias_esg = st.sidebar.multiselect(
    "¿Qué áreas te importan más?",
    ["Medioambiente", "Social", "Gobernanza"],
    default=["Medioambiente", "Gobernanza"]
)

# Selección de sector
sectores = df["Sector"].dropna().unique().tolist()
sector_sel = st.sidebar.selectbox("📂 Sector preferido (opcional)", ["Todos"] + sectores)

# Aversión al riesgo
riesgo = st.sidebar.radio(
    "⚖️ Nivel de aversión al riesgo",
    ["Alta (prefiero empresas estables)", "Media", "Baja (me arriesgo por más rentabilidad)"]
)

# Ponderaciones base
df["score_esg"] = df[["E", "S", "G"]].mean(axis=1)
df["score_fin"] = df[["Crecimiento", "Rentabilidad", "Valoración", "Apalancamiento"]].mean(axis=1)

# Aplicar preferencias ESG específicas
if preferencias_esg:
    columnas_esg = {"Medioambiente": "E", "Social": "S", "Gobernanza": "G"}
    seleccionadas = [columnas_esg[etica] for etica in preferencias_esg]
    df["score_esg"] = df[seleccionadas].mean(axis=1)

# Score combinado final
score = (peso_esg/100) * df["score_esg"] + (peso_fin/100) * df["score_fin"]
df["score_total"] = score

# Filtrado por sector (opcional)
if sector_sel != "Todos":
    df = df[df["Sector"] == sector_sel]

# Filtrado por riesgo
if riesgo == "Alta (prefiero empresas estables)":
    df = df[df["Volatilidad"] < df["Volatilidad"].quantile(0.33)]
elif riesgo == "Baja (me arriesgo por más rentabilidad)":
    df = df[df["Volatilidad"] > df["Volatilidad"].quantile(0.66)]

# Top 3 empresas personalizadas
st.markdown("---")
st.subheader("🏅 Recomendación de empresas para ti")

df_resultado = df.sort_values("score_total", ascending=False).head(3)

st.dataframe(df_resultado[["Nombre", "País", "Sector", "score_esg", "score_fin", "score_total"]].round(2))

st.success("Recomendación generada con éxito. Puedes ajustar tus preferencias para explorar más posibilidades.")