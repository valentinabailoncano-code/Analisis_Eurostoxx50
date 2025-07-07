# 3_🗺️_Mapa_Europeo.py
import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
import os

# Configuración inicial de la página
st.set_page_config(page_title="Mapa Europeo", layout="wide")
st.title("🗺️ Mapa 3D de Empresas del EURO STOXX 50 por País y Sector")

# Explicación inicial
st.markdown("""
En este mapa 3D puedes explorar la distribución de las empresas del índice **EURO STOXX 50** por país y sector.
Cada columna representa un grupo de empresas, con altura proporcional a la cantidad.
""")

# Diccionario de coordenadas por país (puede ser extendido si es necesario)
COORDS = {
    "Alemania": [51.1657, 10.4515],
    "Francia": [46.2276, 2.2137],
    "España": [40.4168, -3.7038],
    "Italia": [41.8719, 12.5674],
    "Países Bajos": [52.1326, 5.2913],
    "Irlanda": [53.1424, -7.6921],
    "Bélgica": [50.5039, 4.4699],
    "Finlandia": [61.9241, 25.7482],
    "Luxemburgo": [49.8153, 6.1296],
    "Portugal": [39.3999, -8.2245],
}

# Cargar datos
@st.cache_data
def load_df():
    try:
        df = pd.read_excel("data/empresas_europeas.xlsx")
        df = df.dropna(subset=['pais', 'sector'])
        df['lat'] = df['pais'].map(lambda x: COORDS.get(x, [None, None])[0])
        df['lon'] = df['pais'].map(lambda x: COORDS.get(x, [None, None])[1])
        df = df.dropna(subset=['lat', 'lon'])
        return df
    except Exception as e:
        st.error(f"Error al cargar datos: {e}")
        return pd.DataFrame()

# Cargar y validar
df = load_df()

if not df.empty:
    # Contar empresas por combinación de país y sector
    grouped = df.groupby(['pais', 'sector', 'lat', 'lon']).agg({'empresa': 'count'}).reset_index()
    grouped = grouped.rename(columns={'empresa': 'n_empresas'})

    # Generar colores automáticos por sector
    sectores = grouped['sector'].unique()
    colores = {
        sector: [int((i * 50) % 255), int((i * 80) % 255), int((i * 110) % 255), 200]
        for i, sector in enumerate(sectores)
    }
    grouped['color'] = grouped['sector'].map(colores)

    # Ajuste de altura para visualización
    grouped['height'] = grouped['n_empresas'] * 10000

    # Mostrar controles
    with st.sidebar:
        st.header("Opciones de visualización")
        scale = st.slider("Altura de columnas", 0.5, 5.0, 1.0, step=0.1)
        radius = st.slider("Radio de agrupación", 5000, 25000, 10000, step=1000)

    # Definir capa
    layer = pdk.Layer(
        "ColumnLayer",
        data=grouped,
        get_position='[lon, lat]',
        get_elevation='height',
        elevation_scale=scale,
        radius=radius,
        get_fill_color='color',
        pickable=True,
        auto_highlight=True,
        extruded=True
    )

    # Vista inicial
    view_state = pdk.ViewState(
        latitude=50,
        longitude=10,
        zoom=3.5,
        pitch=45
    )

    # Tooltip para mostrar detalle al pasar el cursor
    tooltip = {
        "html": "<b>País:</b> {pais}<br/><b>Sector:</b> {sector}<br/><b>Empresas:</b> {n_empresas}",
        "style": {"backgroundColor": "#1e1e1e", "color": "white"}
    }

    # Renderizar mapa
    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip=tooltip,
        map_style="mapbox://styles/mapbox/light-v9"
    ))

    # Mostrar tablas de resumen
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏢 Empresas por País")
        st.dataframe(df.groupby('pais').size().reset_index(name='Nº Empresas').sort_values('Nº Empresas', ascending=False))
    with col2:
        st.subheader("🏭 Empresas por Sector")
        st.dataframe(df.groupby('sector').size().reset_index(name='Nº Empresas').sort_values('Nº Empresas', ascending=False))

else:
    st.warning("No se encontraron datos válidos para el mapa.")