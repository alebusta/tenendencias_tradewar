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

if st.button("Ir a Inicio"):
    st.switch_page("app.py")

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
    """
    Convierte una fecha en español como '4 de marzo de 2025' a un objeto datetime.
    Maneja espacios adicionales, caracteres invisibles y errores de formato.
    """
    # Diccionario de meses en español
    months_dict = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
        'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }
    
    # Limpiar espacios adicionales y caracteres invisibles
    date_string = date_string.strip().replace('\u200b', '').replace('\xa0', ' ')
    
    # Validar que la fecha no esté vacía
    if not date_string:
        raise ValueError("La fecha está vacía o contiene solo caracteres invisibles.")
    
    # Dividir la fecha en partes
    
    parts = date_string.split()
    
    # Validar el formato esperado: "día de mes de año"
    if len(parts) == 5 and parts[1].lower() == 'de' and parts[4].isdigit():
        try:
            # Extraer día, mes y año
            day = int(parts[0])
            month = months_dict.get(parts[2].lower())
            year = int(parts[4])
            
            # Validar que el mes sea válido
            if month is None:
                raise ValueError(f"Mes no reconocido: {parts[2]}")
            
            # Crear y devolver el objeto datetime
            return datetime(year, month, day)
        except Exception as e:
            raise ValueError(f"Error al procesar la fecha: '{date_string}'. Detalles: {e}")
    else:
        raise ValueError(f"Formato de fecha no reconocido: '{date_string}'")

# Leer CSV con medidas arancelarias
df = pd.read_csv('aranceles.csv') #, encoding='utf-8')

# Agregar columnas de fecha parseadas para ordenamiento
df['Anuncio_fecha'] = df['Fecha de Anuncio'].apply(parse_spanish_date)


# Ordenar por fecha de entrada en vigor
df = df.sort_values(by='Anuncio_fecha', ascending=False)

# Crear versión para mostrar (sin columnas de fecha parseadas y sin índice)
display_df = df.drop(columns=['Anuncio_fecha'])

# Crear tabla Plotly para más control sobre el estilo y formato
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
