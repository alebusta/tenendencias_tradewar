import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

# Configuración de la página con estilo The Economist
st.set_page_config(
    page_title="Aranceles de Trump",
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
        <div class="trending-title"><a href="https://tradewar-monitor.streamlit.app/" target="_self"> < Volver al inicio  </a></div>
        
</div>
""", unsafe_allow_html=True)


# Título y descripción con estilo The Economist
st.markdown("<h1 style='font-family: Georgia; font-weight: bold; margin-bottom: 5px'>Repercusiones en Estados Unidos y en el mundo</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Georgia; font-style: italic; margin-bottom: 25px'>Listado de noticias en medios de Estados Unidos y de habla inglesa</p>", unsafe_allow_html=True)
st.markdown('---')
df = pd.read_csv('../mundo_2025-04-02.csv')
df = df[['title','url']]

st.dataframe(df,
             column_config={
        "title": "Titular",
        "url": st.column_config.LinkColumn("Enlace"),
        
    },
    hide_index=True,
    height=600,
    width=1200
    
             )



# Firma de The Economist
st.markdown("""
<div style='font-family: Georgia; font-style: italic; text-align: right; margin-top: 40px; color: #666666;'>
© 2025 CEPAL Lab.
</div>
""", unsafe_allow_html=True)
