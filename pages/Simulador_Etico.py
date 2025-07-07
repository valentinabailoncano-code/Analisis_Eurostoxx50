# 6_🎯_Simulador_Ético.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Simulador Ético", layout="wide")

# Título
st.title("🎯 Simulador de Inversión Ética Personalizado")

st.markdown("""
Este simulador te permite ajustar tus prioridades éticas y financieras para analizar si la empresa **RACE IM** se alinea con tus valores.
""")

# Sidebar: preferencias del usuario
st.sidebar.header("🔧 Personaliza tu inversión")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_excel("data/Datos_STOXX50_.xlsx", sheet_name="Financiero")
    df["Fecha"] = pd.to_datetime(df["Dates"], errors='coerce')
    df.dropna(subset=["Fecha"], inplace=True)
    df["Año"] = df["Fecha"].dt.year
    return df

df = load_data()

# Usuario elige año
available_years = sorted(df["Año"].dropna().unique())
year_selected = st.sidebar.selectbox("Selecciona el año de análisis:", available_years)

df = df[df["Año"] == year_selected]

# Pesos ESG vs Financieros
peso_esg = st.sidebar.slider("¿Qué peso das al componente ESG?", 0, 100, 50)
peso_fin = 100 - peso_esg

# Selección de áreas ESG
preferencias_esg = st.sidebar.multiselect(
    "¿Qué componentes ESG te importan más?",
    ["Medioambiente", "Social", "Gobernanza"],
    default=["Medioambiente", "Gobernanza"]
)

# Mapeo a columnas del Excel
map_esg = {
    "Medioambiente": "RACE IM  .10",
    "Social": "RACE IM  .11",
    "Gobernanza": "RACE IM  .13"
}

columnas_esg = [map_esg[p] for p in preferencias_esg if map_esg[p] in df.columns]
columnas_fin = ['RACE IM  .6', 'RACE IM  .7', 'RACE IM  .4', 'RACE IM  ']  # ROE, ROI, Dividendo, P/E

# Validación y cálculo
if df.empty or not columnas_esg or not all(col in df.columns for col in columnas_fin):
    st.warning("No hay datos suficientes para realizar el análisis en este año.")
else:
    df["score_esg"] = df[columnas_esg].mean(axis=1)
    
    # Valoración se invierte (menor P/E es mejor)
    df["score_valoracion"] = 1 - (df['RACE IM  '] - df['RACE IM  '].min()) / (df['RACE IM  '].max() - df['RACE IM  '].min())

    df["score_fin"] = df[["RACE IM  .6", "RACE IM  .7", "RACE IM  .4"]].mean(axis=1) * 0.75 + df["score_valoracion"] * 0.25

    # Score final
    df["score_total"] = (peso_esg / 100) * df["score_esg"] + (peso_fin / 100) * df["score_fin"]

    # Mostrar resultados
    st.markdown("---")
    st.subheader(f"📈 Resultado de RACE IM en {year_selected}")
    st.dataframe(df[["Fecha", "score_esg", "score_fin", "score_total"]].round(3), use_container_width=True)

    st.success("Simulación completada. Puedes modificar los criterios para ver cómo cambia el resultado.")

