import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import ast
from shared_data import get_dataframe

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

if st.button("Ir a Inicio"):
    st.switch_page("app.py")
    
# Título y descripción con estilo The Economist
st.markdown("<h1 style='font-family: Georgia; font-weight: bold; margin-bottom: 5px'>Repercusiones en América Latina y El Caribe</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Georgia; font-style: italic; margin-bottom: 25px'>Listado de noticias en medios en español</p>", unsafe_allow_html=True)

df = get_dataframe()
df = df[df['geo'] == 'latam']
df = df[['date_process','title','content','url','country']]

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

show = ['date_process','title','content','url', 'pais']

# Función para restablecer filtros
def reset_filters():
    st.session_state.title_filter = ""
    st.session_state.country_filter = []

# Inicializar valores en session_state si no existen
if "title_filter" not in st.session_state:
    st.session_state.title_filter = ""
if "country_filter" not in st.session_state:
    st.session_state.country_filter = []

# Agregar filtros interactivos dentro de un desplegable
with st.expander("### Filtros de búsqueda (haz clic para expandir)"):

    col1, col2= st.columns(2)

    with col1:
        # Campo de texto para buscar por título
        title_filter = st.text_input("Buscar por título:", value="", key="title_filter")

        # Separar y obtener valores únicos de países
        all_countries = set()
        for paises in df['pais'].dropna():
            if isinstance(paises, str):
                all_countries.update(paises.split(', '))

    with col2:
        # Campo de selección múltiple para buscar por país
        country_filter = st.multiselect(
            "Filtrar por país:",
            options=sorted(all_countries),
            default=[],
            key="country_filter"
        )

# Botón para restablecer filtros
if st.button("Mostrar todo", on_click=reset_filters):
    pass

# Aplicar filtros
filtered_df = df.copy()

if st.session_state.title_filter:
    filtered_df = filtered_df[filtered_df['title'].str.contains(st.session_state.title_filter, case=False, na=False)]

if st.session_state.country_filter:
    filtered_df = filtered_df[filtered_df['pais'].apply(lambda x: any(country in x for country in st.session_state.country_filter))]

# Mostrar resultados filtrados
st.markdown(f"### Total registros: {len(filtered_df)}")

st.dataframe(
    filtered_df[show],
    column_config={
        "date_process": st.column_config.DateColumn("Fecha"),
        "title": "Titular",
        "content": "Avance",
        "url": st.column_config.LinkColumn("Enlace"),
        "pais": "Países"
    },
    hide_index=True,

)




# footer
st.markdown("""
<div style='font-family: Georgia; font-style: italic; text-align: right; margin-top: 40px; color: #666666;'>
© 2025 Lab.
</div>
""", unsafe_allow_html=True)

