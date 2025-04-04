import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import ast

# Configuración de la página con estilo The Economist
st.set_page_config(
    page_title="Aranceles de Trump - The Economist Style",
    page_icon="📊",
    layout="wide"
)

# Ocultar la sidebar con CSS
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Encabezado
# CSS personalizado para el encabezado
st.markdown("""

<div class="trending-bar">
        <div class="trending-title"><a href="https://tradewar-monitor.streamlit.app/" target="_blank"> < Volver al inicio  </a></div>
        
</div>
""", unsafe_allow_html=True)



# Título y descripción con estilo The Economist
st.markdown("<h1 style='font-family: Georgia; font-weight: bold; margin-bottom: 5px'>Repercusiones en América Latina y El Caribe</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Georgia; font-style: italic; margin-bottom: 25px'>Listado de noticias en medios en español</p>", unsafe_allow_html=True)
st.markdown('---')

df = pd.read_csv('aranceles_2025-04-02.csv')
df = df[['title','url','country']]

# Opción 1: Convertir la lista a string separado por comas
# Función para manejar correctamente la conversión de listas a texto
def format_list(x):
    if isinstance(x, list):
        return ', '.join(x)
    elif isinstance(x, str):
        try:
            # Intenta evaluar si es una cadena que representa una lista
            lista = ast.literal_eval(x)
            if isinstance(lista, list):
                return ', '.join(lista)
        except:
            pass
    # Si no es lista ni cadena que representa lista, devolver como está
    return str(x)

# Aplicar la función de formateo
df['pais'] = df['country'].apply(format_list)

show = ['title', 'url', 'pais']
st.dataframe(
    df[show],
    column_config={
        "title": "Titular",
        "url": st.column_config.LinkColumn("Enlace"),
        "pais": "Países"
    },
    hide_index=True,
    height=600,
    )



# Firma de The Economist
st.markdown("""
<div style='font-family: Georgia; font-style: italic; text-align: right; margin-top: 40px; color: #666666;'>
© 2025 CEPAL Lab.
</div>
""", unsafe_allow_html=True)
