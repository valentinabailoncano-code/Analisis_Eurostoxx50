# 9_🤖_Consulta_Empresas.py
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("🤖 Consulta rápida de empresas")

st.markdown("""
Haz preguntas simples sobre las empresas del EURO STOXX 50. El sistema interpreta tu consulta y filtra automáticamente los resultados más relevantes.

Ejemplos:
- "Empresa con mejor puntuación ESG"
- "Mejor empresa alemana en rentabilidad"
- "Top 3 empresas de salud con baja deuda"
""")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_excel("data/Datos_STOXX50_.xlsx")

df = load_data()

# Entrada de usuario
consulta = st.text_input("Escribe tu pregunta o consulta:")

if consulta:
    consulta = consulta.lower()

    resultado = df.copy()

    # Filtros simples por país
    for pais in df["País"].dropna().unique():
        if pais.lower() in consulta:
            resultado = resultado[resultado["País"] == pais]

    # Filtros por sector
    for sector in df["Sector"].dropna().unique():
        if sector.lower() in consulta:
            resultado = resultado[resultado["Sector"] == sector]

    # Interpretaciones simples
    if "mejor" in consulta and "esg" in consulta:
        resultado = resultado.sort_values("ESG", ascending=False).head(5)

    elif "mejor" in consulta and "rentabilidad" in consulta:
        resultado = resultado.sort_values("Rentabilidad", ascending=False).head(5)

    elif "baja deuda" in consulta or "menos deuda" in consulta:
        resultado = resultado.sort_values("Apalancamiento").head(5)

    elif "crecimiento" in consulta:
        resultado = resultado.sort_values("Crecimiento", ascending=False).head(5)

    # Resultado mostrado
    if not resultado.empty:
        st.success("Resultado para tu consulta:")
        st.dataframe(resultado[["Nombre", "País", "Sector", "E", "S", "G", "Crecimiento", "Rentabilidad", "Valoración", "Apalancamiento"]].round(2))
    else:
        st.warning("No se encontraron resultados. Intenta reformular tu consulta.")
