# 9_🤖_Consulta_RACE_IM.py
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("🤖 Consulta rápida sobre RACE IM")

st.markdown("""
Haz preguntas simples sobre la empresa **RACE IM** del EURO STOXX 50.  
El sistema interpreta tu consulta y muestra automáticamente las métricas relevantes.

**Ejemplos:**
- "¿Cuál es el ROE más alto?"
- "Muestra los años con mejor ESG"
- "¿Cuándo fue menor la valoración?"
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

# Crear columna con promedio ESG simulado
df["ESG"] = df[["RACE IM  .10", "RACE IM  .13"]].mean(axis=1)

# Diccionario de alias por variable
alias = {
    "roe": "RACE IM  .6",
    "roi": "RACE IM  .7",
    "dividendos": "RACE IM  .4",
    "valoración": "RACE IM  ",
    "esg": "ESG"
}

consulta = st.text_input("Escribe tu consulta sobre RACE IM:")

if consulta:
    consulta = consulta.lower()
    columna_detectada = None

    for clave, col in alias.items():
        if clave in consulta:
            columna_detectada = col
            break

    if columna_detectada and columna_detectada in df.columns:
        orden = "menor" in consulta or "bajo" in consulta or "mínimo" in consulta
        top = df[["Año", columna_detectada]].dropna().sort_values(columna_detectada, ascending=orden).head(5)
        st.success(f"Top valores para '{clave.upper()}'")
        st.dataframe(top.rename(columns={columna_detectada: clave.upper()}).reset_index(drop=True))
    else:
        st.warning("No se pudo interpretar tu consulta. Prueba con palabras como 'ROE', 'ESG', 'dividendos', 'valoración', etc.")

