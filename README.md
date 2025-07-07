
# 📈 EURO STOXX 50 – Análisis Financiero & ESG

Bienvenida/o al repositorio del proyecto desarrollado por **Valentina Bailón Cano** como parte del Módulo 1 del Máster en Data Science & IA de **Evolve**.  
Esta aplicación interactiva, construida con **Streamlit**, ofrece un análisis completo del índice **EURO STOXX 50**, combinando métricas **financieras**, criterios de **sostenibilidad ESG** y herramientas estadísticas avanzadas.

---

## 🔍 ¿Qué encontrarás en esta app?

### 🏆 1. Top 5 Acciones
Identificación automática de las 5 mejores empresas del índice mediante un sistema de puntuación multicriterio que integra indicadores financieros y ESG.

### 📊 2. Comparativa con el Índice
Análisis comparativo entre las Top 5 seleccionadas y el resto del índice. Visualizaciones dinámicas y diferencias porcentuales por categoría.

### 🗺️ 3. Mapa Europeo
Visualización 3D de las empresas por país y sector usando **PyDeck**, con alturas proporcionales, colores automáticos y tooltips informativos.

### 📉 4. Análisis Estadístico
Histogramas, correlaciones, regresiones y pruebas de hipótesis aplicadas a variables financieras y de sostenibilidad. Incluye filtrado por país o sector.

### 🙋‍♀️ 5. Sobre mí
Sección personal con información profesional, fotografía y enlace a LinkedIn.

### 🎯 6. Simulador de Inversión Ética
Elige tus preferencias (ESG vs. finanzas, sector, riesgo) y recibe un portafolio personalizado de 3 empresas recomendadas.

### 📊 7. Dashboard de KPIs
Visualiza comparaciones entre empresas, países o sectores eligiendo tus propios indicadores clave (KPIs).

### 📈 8. Ranking ESG Histórico
Explora cómo han evolucionado las puntuaciones ESG a lo largo del tiempo para cada empresa (datos simulados).

### 🤖 9. Chat de Consulta con Empresas
Haz preguntas como “mejor empresa alemana en ESG” y recibe una tabla filtrada automáticamente.

### 🌍 10. Comparativa con otros Índices
Compara EURO STOXX 50 con IBEX 35 y S&P 500 en indicadores clave financieros y de sostenibilidad.

---

---

## 🧠 Tecnologías utilizadas

- `Python`
- `Streamlit`
- `Pandas`, `NumPy`, `OpenPyXL`
- `Seaborn`, `Matplotlib`, `Plotly`
- `Scipy`, `Statsmodels`
- `PyDeck`, `PIL`

---

## 📁 Estructura del proyecto

```
📦 analisis_eurostoxx50/
├── data/
│   ├── Datos_STOXX50_.xlsx
│   └── empresas_europeas.xlsx
├── images/
│   ├── evolve_logo.png
│   └── valen.png
├── pages/
│ ├── 1_📊_Top_5_Acciones.py
│ ├── 2_📈_Comparativa_Index.py
│ ├── 3_🗺️_Mapa_Europeo.py
│ ├── 4_📉_Análisis_Estadístico.py
│ ├── 5_🙋‍♀️_Sobre_mí.py
│ ├── 6_🎯_Simulador_Ético.py
│ ├── 7_📊_Dashboard_KPIs.py
│ ├── 8_📈_Ranking_ESG_Historico.py
│ ├── 9_🤖_Consulta_Empresas.py
│ └── 10_🌍_Comparativa_Índices.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Cómo ejecutar la app

```bash
# 1. Clona este repositorio
git clone https://github.com/valentinabailoncano-code/Analisis_Eurostoxx50.git
cd Analisis_Eurostoxx50

# 2. (Opcional) Crea un entorno virtual
python -m venv env
source env/bin/activate  # En Windows: .\env\Scripts\activate

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Ejecuta la app
streamlit run main.py
```

---

## 🌐 Enlace a la App

🔗 *Próximamente disponible en Streamlit Cloud*

---

## 👩‍💻 Autora

**Valentina Bailón Cano**  
Máster en Data Science & IA – Evolve  
📫 [LinkedIn](https://www.linkedin.com/in/valentina-bailon-2653b22b7)

---

## 📜 Licencia

Proyecto de carácter académico y personal.  
No se permite su uso o distribución comercial sin autorización explícita de la autora.

---
