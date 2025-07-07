# main.py
import streamlit as st
from PIL import Image

# Configuración general
st.set_page_config(
    page_title="EURO STOXX 50 - Proyecto Valentina",
    page_icon="📈",
    layout="wide"
)

# Mostrar logo de Evolve
logo = Image.open("images/evolve_logo.png")
st.image(logo, width=200)

# Título principal
st.title("📈 Análisis Integral del EURO STOXX 50")

# Descripción general
st.markdown("""
Este proyecto ha sido desarrollado por **Valentina Bailón Cano** como parte del Módulo 1 del Máster en Data Science & IA en **Evolve**.

Se analiza el índice **EURO STOXX 50** combinando:
- Indicadores financieros clave (crecimiento, rentabilidad, valoración, apalancamiento)
- Métricas ESG (Environmental, Social & Governance)
- Herramientas estadísticas reales (correlaciones, regresión, hipótesis)

El objetivo: **identificar oportunidades de inversión éticas y rentables** con visualizaciones claras y análisis automatizado.

Este proyecto también destaca por su estructura modular, profesional y lista para despliegue en GitHub y Streamlit Cloud.
""")

# Motivación personal
st.markdown("""
---
### ¿Por qué el EURO STOXX 50?
Este índice representa a las 50 mayores empresas de la eurozona. Analizarlo:
- Permite trabajar con datos financieros reales y diversos
- Une métricas de rendimiento con sostenibilidad corporativa
- Refuerza habilidades en visualización, análisis y desarrollo profesional

Este proyecto refleja mi aprendizaje aplicado hasta ahora en el máster.
""")

# Guía de navegación
st.markdown("""
---
### 🧭 Navegación del Proyecto
Explora cada sección desde el menú lateral. A continuación, un resumen de funcionalidades:

#### 📊 Top 5 Acciones
Modelo de puntuación multicriterio que selecciona las 5 mejores empresas del índice combinando métricas financieras y ESG.

#### 📈 Comparativa con el Índice
Compara las Top 5 frente al promedio del EURO STOXX 50. Visualiza diferencias por KPI y en porcentaje.

#### 🗺️ Mapa Europeo
Visualización 3D interactiva que muestra la distribución geográfica y sectorial de las empresas del índice.

#### 📉 Análisis Estadístico
Explora correlaciones, distribuciones, regresión y pruebas estadísticas aplicadas a métricas ESG y financieras.

#### 🎯 Simulador de Inversión Ética
Configura tus preferencias ESG, nivel de riesgo y sector deseado. El sistema recomienda 3 empresas personalizadas.

#### 📊 Dashboard de KPIs
Compara cualquier KPI por empresa, país o sector con gráficos dinámicos.

#### 📈 Ranking ESG Histórico
Visualiza la evolución simulada del rendimiento ESG a lo largo del tiempo.

#### 🤖 Consulta con Empresas
Haz preguntas tipo "mejor empresa de salud con baja deuda" y recibe una respuesta automática basada en filtros inteligentes.

#### 🌍 Comparativa de Índices
Compara el EURO STOXX 50 con el IBEX 35 y S&P 500 en rendimiento, valoración y sostenibilidad.

#### 🙋‍♀️ Sobre mí
Descubre quién soy, por qué hice este proyecto y cómo puedes contactarme. Incluye bio y enlace a mi LinkedIn.
""")

# Mensaje final destacado
st.success("¡Bienvenida a la herramienta de análisis del EURO STOXX 50 desarrollada por Valentina Bailón Cano!")

# Cierre
st.markdown("""
---
¿Quieres saber más? Explora el código en GitHub o consulta cada sección de la app. ¡Gracias por tu visita!
""")
