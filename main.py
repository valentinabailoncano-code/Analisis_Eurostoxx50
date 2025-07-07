# main.py
import streamlit as st
from PIL import Image

# Configuración general de la página principal de la app
st.set_page_config(
    page_title="EURO STOXX 50 - Proyecto Valentina",
    page_icon="📈",
    layout="wide"
)

# Mostrar el logo de Evolve al inicio
logo = Image.open("images/evolve_logo.png")
st.image(logo, width=200)

# Título principal del proyecto
st.title("Análisis Integral del EURO STOXX 50")

# Descripción general del proyecto y contexto
st.markdown("""
Este proyecto ha sido desarrollado por **Valentina Bailón Cano** como parte del Módulo 1 del Máster en Data Science & IA en **Evolve**.

A lo largo de este trabajo se realiza un análisis exhaustivo del índice **EURO STOXX 50**, combinando:
- Indicadores financieros clave (crecimiento, rentabilidad, valoración, apalancamiento).
- Métricas de sostenibilidad ESG (Environmental, Social & Governance).
- Análisis estadístico aplicado (distribuciones, correlaciones, inferencia).

El objetivo principal es **identificar las mejores oportunidades de inversión** dentro del índice, equilibrando rendimiento financiero con responsabilidad corporativa y sostenibilidad. Esto permite no solo tomar decisiones rentables, sino también éticas y alineadas con los criterios más exigentes del entorno económico y regulatorio actual.

Este proyecto no solo responde a criterios cuantitativos, sino que también busca representar buenas prácticas de visualización de datos, organización modular en Streamlit y preparación para despliegue profesional (GitHub y Streamlit Cloud).
""")

# Sección: Motivación personal
st.markdown("""
---
### ¿Por qué el EURO STOXX 50?
El EURO STOXX 50 es uno de los índices bursátiles más representativos de Europa. Aglutina 50 de las empresas más grandes y líquidas de la zona euro, abarcando sectores diversos como tecnología, energía, consumo, finanzas y salud.

Analizar este índice representa una oportunidad de:
- Explorar datos reales y complejos del entorno financiero europeo.
- Aplicar técnicas de analítica de datos y sostenibilidad.
- Desarrollar una app con criterios profesionales y prácticos.

Este proyecto me ha permitido integrar todo lo aprendido en el máster hasta ahora, desde programación en Python hasta estadística aplicada, visualización y buenas prácticas de ingeniería de datos.
""")

# Sección: Guía de navegación por secciones
st.markdown("""
---
### Navegación del Proyecto
Usa el menú lateral izquierdo para explorar todas las funcionalidades. A continuación, se presenta una descripción ampliada de cada módulo:

#### 📊 Top 5 Acciones
> Sistema automatizado de puntuación multicriterio que selecciona las cinco mejores empresas del índice. Utiliza métricas ponderadas de crecimiento, rentabilidad, valoración, apalancamiento y ESG. El resultado es una tabla y gráficos dinámicos.

#### 📈 Comparativa con el Índice
> Compara estadísticamente las Top 5 frente al total del índice STOXX50. Se muestran diferencias porcentuales por categoría, y gráficos de barras para observar fortalezas relativas.

#### 🗺️ Mapa Europeo
> Visualización geográfica 3D donde cada país representa las empresas que lo integran. Se utiliza PyDeck para ilustrar densidad de empresas y diversidad sectorial. Incluye leyenda, filtros y análisis textual del panorama económico europeo.

#### 📉 Análisis Estadístico
> Página donde se aplican técnicas estadísticas reales aprendidas en el máster: histogramas, tests de hipótesis, correlaciones entre métricas ESG y financieras, y regresiones simples. Se puede filtrar por sector o país para exploración avanzada.

#### 🙋‍♀️ Sobre mí
> Espacio personal donde explico quién soy, qué me motivó a desarrollar este proyecto y cómo contactarme profesionalmente. Incluye imagen, bio, idiomas y enlace directo a LinkedIn.
""")

# Mensaje de bienvenida destacado al pie de la portada
st.success("¡Bienvenida a la herramienta de análisis del EURO STOXX 50 desarrollada por Valentina Bailón Cano!")

# Cierre con agradecimiento
st.markdown("""
---
¿Quieres saber más sobre cómo se desarrolló esta app? Explora el código fuente en GitHub o consulta la documentación interna en cada sección. ¡Gracias por visitar!
""")
