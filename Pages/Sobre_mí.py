# 5_🙋‍♀️_Sobre_mí.py
import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Sobre mí", layout="centered")
st.title("🙋‍♀️ Sobre mí")

# Mostrar imagen de perfil
st.image("images/valen.png", width=220)

# Nombre
st.markdown("## Valentina Bailón Cano")

# Breve descripción en primera persona
st.markdown("""
¡Hola! Soy estudiante del Máster en Data Science & Inteligencia Artificial en **Evolve** y autora de este proyecto.

Me apasionan el análisis de datos, la estrategia empresarial y los retos intelectuales. Hablo español, inglés y tengo conocimientos básicos de francés e italiano. Me considero una persona **proactiva, curiosa y con muchas ganas de aprender**.

Este proyecto me ha permitido aplicar conocimientos clave del máster, como:
- Programación en Python
- Visualización de datos (Plotly, Streamlit, PyDeck)
- Análisis estadístico e inferencia
- ESG, finanzas y sostenibilidad

Y sobre todo... ¡darle sentido a los datos para tomar mejores decisiones!
""")

# Enlace a LinkedIn con logo
linkedin_url = "https://www.linkedin.com/in/valentina-bailon-2653b22b7"
st.markdown(f"[![LinkedIn](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)]({linkedin_url}) Conéctate conmigo en LinkedIn")

# Frase de cierre personalizada
st.success("Gracias por visitar este proyecto. ¡Espero que te inspire tanto como a mí desarrollarlo!")