# 📈 EURO STOXX 50 - Análisis ESG y Financiero

Este repositorio contiene una app desarrollada en **Streamlit** por **Valentina Bailón Cano**, como parte del Módulo 1 del Máster en Data Science & IA en **Evolve**.

La app analiza el índice **EURO STOXX 50** combinando datos **financieros** y de **sostenibilidad ESG**, incorporando también visualizaciones, estadística e interactividad.

---

## 🧠 Contenidos y funcionalidades

### 1. Top 5 Acciones  
Identificación automática de las mejores 5 empresas usando un sistema de puntuación multicriterio (finanzas + ESG).

### 2. Comparativa con el Índice  
Comparación de promedios entre las Top 5 y el total del EURO STOXX 50 con gráficos y diferencias porcentuales.

### 3. Mapa Europeo  
Mapa 3D interactivo por país y sector usando PyDeck. Colores automáticos, altura proporcional y tooltip.

### 4. Análisis Estadístico  
Histogramas, matriz de correlación, regresión lineal y pruebas de hipótesis sobre datos ESG y financieros.

### 5. Sobre mí  
Bio de la autora, imagen y LinkedIn.

---

## 📁 Estructura del proyecto

```
📦 stoxx50-valentina/
├── data/
│   ├── Datos_STOXX50_.xlsx
│   └── empresas_europeas.xlsx
├── images/
│   ├── evolve_logo.png
│   └── valen.png
├── pages/
│   ├── 1_📊_Top_5_Acciones.py
│   ├── 2_📈_Comparativa_Index.py
│   ├── 3_🗺️_Mapa_Europeo.py
│   ├── 4_📉_Análisis_Estadístico.py
│   └── 5_🙋‍♀️_Sobre_mí.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Instalación y ejecución

```bash
# Clonar el repositorio
git clone https://github.com/valentinabailon/stoxx50-valentina.git
cd stoxx50-valentina

# Crear entorno virtual (opcional)
python -m venv env
source env/bin/activate  # o .\env\Scripts\activate en Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la app
streamlit run main.py
```

---

## 🔗 Autora

**Valentina Bailón Cano**  
[LinkedIn](https://www.linkedin.com/in/valentina-bailon-2653b22b7)

---

## 🧾 Licencia
Este proyecto es de uso académico y personal. No se permite su redistribución comercial sin autorización.
