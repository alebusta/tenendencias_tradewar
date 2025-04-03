import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

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
            display: none !important;
        }
        [data-testid="collapsedControl"] {
            display: none !important;
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

# Aplicar estilo The Economist
st.markdown("""
<style>
    .main {
        background-color: #ffffff;
        color: #121212;
        font-family: 'Georgia', serif;
    }
    h1, h2, h3, h4 {
        font-family: 'Georgia', serif;
        font-weight: bold;
        color: #121212;
    }
    .stDataFrame {
        font-family: 'Georgia', serif;
    }
    .st-bc {
        background-color: #ffffff;
    }
    footer {
        font-family: 'Georgia', serif;
        font-size: 12px;
        color: #666666;
    }
</style>
""", unsafe_allow_html=True)

# Título y descripción con estilo The Economist
st.markdown("<h1 style='font-family: Georgia; font-weight: bold; margin-bottom: 5px'>Guerra Comercial: Cronología de Aranceles Trump</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Georgia; font-style: italic; margin-bottom: 25px'>Una visión detallada de las medidas arancelarias de la administración Trump en 2025</p>", unsafe_allow_html=True)

# Función para convertir fechas textuales a objetos datetime
def parse_spanish_date(date_string):
    months_dict = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
        'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }
    
    # Extraer componentes
    parts = date_string.split()
    if len(parts) >= 4 and parts[0].isdigit() and parts[1] == 'de' and parts[3] == '2025':
        day = int(parts[0])
        month = months_dict.get(parts[2].lower(), 1)
        year = 2025
        return datetime(year, month, day)
    elif date_string.lower() == 'esta semana (abril)':
        return datetime(2025, 4, 5)  # Aproximación para "esta semana"
    elif 'mediados de abril' in date_string.lower():
        return datetime(2025, 4, 15)  # Aproximación para "mediados de abril"
    else:
        return datetime(2025, 4, 1)  # Fecha por defecto si no se puede parsear

# Datos de las medidas arancelarias con soporte para ordenamiento
data = {
    'Medida': [
        'Aranceles del 25% a todos los productos de Canadá y México',
        'Contraranceles de China de hasta 15% a productos agrícolas de EE.UU.',
        'Aranceles del 25% a importaciones de acero y aluminio a nivel global',
        'Contraranceles de la UE en $28 mil millones de productos estadounidenses',
        'Fin de la pausa de aranceles sobre bienes no conformes con USMCA',
        'Aranceles recíprocos a todos los socios comerciales ("Día de Liberación")',
        'Arancel del 50% al whisky americano por parte de la UE',
        'Arancel secundario del 25% a países que comercien con Venezuela',
        'Aranceles del 25% a todos los vehículos fabricados en el extranjero'
    ],
    'Fecha de Anuncio': [
        '1 de marzo de 2025',
        '5 de marzo de 2025',
        '1 de marzo de 2025',
        '15 de marzo de 2025',        
        '4 de marzo de 2025',
        '30 de marzo de 2025',
        '15 de marzo de 2025',
        '15 de marzo de 2025',
        '26 de marzo de 2025'
    ],
    'Fecha de Entrada en Vigor': [
        '4 de marzo de 2025',
        '10 de marzo de 2025',
        '12 de marzo de 2025',
        '1 de abril de 2025',
        '2 de abril de 2025',
        '2 de abril de 2025',
        'Mediados de abril de 2025',
        '2 de abril de 2025',
        '2 de abril de 2025',
    ],
    'Países/Regiones Afectados': [
        'Canadá y México',
        'Estados Unidos',
        'Global',
        'Estados Unidos',        
        'Canadá y México',
        'Global',
        'Estados Unidos',
        'Socios comerciales de Venezuela',
        'Global',
    ],
    'Arancel': [
        '25%',
        'Hasta 15%',
        '25%',
        'Varios',        
        'Aranceles existentes',
        '~20%',
        '50%',
        '25%',
        '25%',
    ],
    'Productos Principales': [
        'Todos los productos',
        'Pollo, cerdo y otros productos agrícolas',
        'Acero y aluminio',
        'Diversos productos estadounidenses',        
        'Productos no conformes con USMCA',
        'La mayoría de las importaciones',
        'Whisky americano',
        'Todos los productos de países que compren petróleo/gas venezolano',
        'Todos los vehículos extranjeros',
    ],
    'Tipo': [
        '🔴 EE.UU. impone',
        '🔵 Respuesta a EE.UU.',
        '🔴 EE.UU. impone',
        '🔵 Respuesta a EE.UU.',        
        '🔴 EE.UU. impone',
        '🔴 EE.UU. impone',
        '🔵 Respuesta a EE.UU.',
        '🔴 EE.UU. impone',
        '🔴 EE.UU. impone'
    ]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Agregar columnas de fecha parseadas para ordenamiento
df['Anuncio_fecha'] = df['Fecha de Anuncio'].apply(parse_spanish_date)
df['Vigor_fecha'] = df['Fecha de Entrada en Vigor'].apply(parse_spanish_date)

# Ordenar por fecha de entrada en vigor
df = df.sort_values(by='Vigor_fecha')

# Crear versión para mostrar (sin columnas de fecha parseadas y sin índice)
display_df = df.drop(columns=['Anuncio_fecha', 'Vigor_fecha'])

# Crear tabla Plotly para más control sobre el estilo (estilo The Economist)
fig = go.Figure(data=[go.Table(
    header=dict(
        values=list(display_df.columns),
        fill_color='#121212',
        font=dict(color='white', size=13, family='Georgia'),
        align='left',
        height=40
    ),
    cells=dict(
        values=[display_df[col] for col in display_df.columns],
        fill_color=[['#e6e6e6' if i % 2 == 0 else 'white' for i in range(len(display_df))]],
        font=dict(color= '#121212', 
                  size=14, family='Georgia'),
        align='left',
        height=35
    )
)])

# Ajustar diseño de la tabla
fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    height=700,
    width=1200
)

# Mostrar tabla
st.plotly_chart(fig, use_container_width=True)

# Leyenda con estilo The Economist
st.markdown("""
<div style='background-color: #f8f8f8; padding: 15px; border-left: 5px solid #121212; margin-top: 20px; font-family: Georgia;'>
<strong>Leyenda:</strong><br>
🔴 <span style='color: #990000; font-weight: bold;'>EE.UU. impone</span>: Aranceles impuestos por Estados Unidos a otros países<br>
🔵 <span style='color: #000099; font-weight: bold;'>Respuesta a EE.UU.</span>: Contramedidas impuestas por otros países en respuesta a los aranceles de EE.UU.
</div>
""", unsafe_allow_html=True)

# Nota metodológica con estilo The Economist
st.markdown("""
<div style='font-family: Georgia; font-size: 12px; color: #666666; margin-top: 30px;'>
<strong>Metodología:</strong> Los datos presentados han sido compilados a partir de información de Yahoo Finance publicada el 2 de abril de 2025. 
Las fechas aproximadas ("Esta semana", "Mediados de abril") se han incluido tal como aparecen en la fuente original.
</div>
""", unsafe_allow_html=True)

# Firma de The Economist
st.markdown("""
<div style='font-family: Georgia; font-style: italic; text-align: right; margin-top: 40px; color: #666666;'>
© 2025 CEPAL Lab.
</div>
""", unsafe_allow_html=True)
