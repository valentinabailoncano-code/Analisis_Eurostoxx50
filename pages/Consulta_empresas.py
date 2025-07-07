# 9_🤖_Consulta_Empresas.py
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("🤖 Consulta rápida de empresas")

st.markdown("""
Haz preguntas simples sobre las empresas del EURO STOXX 50. El sistema interpreta tu consulta y filtra automáticamente los resultados más relevantes.

**Ejemplos**:
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

    # Filtrar por país (soporte flexible)
    for pais in df["País"].dropna().unique():
        if pais.lower() in consulta:
            resultado = resultado[resultado["País"].str.lower() == pais.lower()]

    # Filtrar por sector
    for sector in df["Sector"].dropna().unique():
        if sector.lower() in consulta:
            resultado = resultado[resultado["Sector"].str.lower() == sector.lower()]

    # Filtros por indicadores clave
    if "mejor" in consulta and "esg" in consulta:
        resultado = resultado.sort_values("ESG", ascending=False).head(5)

    elif "mejor" in consulta and "rentabilidad" in consulta:
        resultado = resultado.sort_values("Rentabilidad", ascending=False).head(5)

    elif "baja deuda" in consulta or "menos deuda" in consulta or "apalancamiento" in consulta:
        resultado = resultado.sort_values("Apalancamiento", ascending=True).head(5)

    elif "crecimiento" in consulta:
        resultado = resultado.sort_values("Crecimiento", ascending=False).head(5)

    elif "valoración" in consulta or "p/e" in consulta:
        resultado = resultado.sort_values("Valoración", ascending=True).head(5)

    elif "top" in consulta:
        # Detectar un número (top 3, top 5)
        import re
        match = re.search(r"top\s*(\d+)", consulta)
        if match:
            n = int(match.group(1))
            resultado = resultado.sort_values("ESG", ascending=False).head(n)

    # Mostrar resultado
    if not resultado.empty:
        st.success("Resultado para tu consulta:")
        st.dataframe(
            resultado[
                ["Nombre", "País", "Sector", "E", "S", "G", "Crecimiento", "Rentabilidad", "Valoración", "Apalancamiento"]
            ].round(2),
            use_container_width=True
        )
    else:
        st.warning("No se encontraron resultados. Intenta reformular tu consulta.")

