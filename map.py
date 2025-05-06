# Script para crear el mapa de menciones de países Latam del front

import pandas as pd
import ast
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

    # Crear el mapa

def impact_map():

    file_id = '1C5w6w3u-pFKv3-l7iLAGhphyO9nn4Xmc'
    url = f'https://drive.google.com/uc?id={file_id}'

    df = pd.read_csv(url)
   

    #df = pd.read_csv('database.csv')

    # Crear un DataFrame con los recuentos de etiquetas países
    df['country'] = df['country'].apply(ast.literal_eval)
    tags_exploded = df.explode('country')
    tag_counts = tags_exploded["country"].value_counts()

    # Lista de países LAC
    paises_alc = [
        # América del Sur
        "Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Ecuador",
        "Guyana", "Paraguay", "Perú", "Surinam", "Uruguay", "Venezuela",

        # América Central
        "Belice", "Costa Rica", "El Salvador", "Guatemala", "Honduras",
        "Nicaragua", "Panamá",

        # Caribe
        "Antigua y Barbuda", "Bahamas", "Barbados", "Cuba", "Dominica",
        "Granada", "Haití", "Jamaica", "República Dominicana",
        "Saint Kitts y Nevis", "San Vicente y las Granadinas", "Santa Lucía",
        "Trinidad y Tobago",

        # México
        "México",

        # Territorios del Caribe frecuentemente incluidos en análisis regionales
        "Puerto Rico", "Guayana Francesa", "Islas Caimán", "Aruba",
        "Curazao", "Martinica", "Guadalupe", "Islas Vírgenes Británicas",
        "Montserrat", "Sint Maarten", "Turks y Caicos"]

    tags_lac = tags_exploded[tags_exploded['country'].isin(paises_alc)]

    tag_counts = tags_lac["country"].value_counts()

    # Orden alfabético por nombre de país:
    cuenta_paises_ordenado = tag_counts.sort_index()

    # Diccionario de mapeo español-inglés
    country_names_mapping = {
        'México': 'Mexico',
        'Argentina': 'Argentina',
        'Belice': 'Belize',
        'Brasil': 'Brazil',
        'Haití': 'Haiti',
        'Panamá': 'Panama',
        'Perú': 'Peru',
        'República Dominicana': 'Dominican Republic',
        'Trinidad y Tobago': 'Trinidad and Tobago'
    }

    # Aplicar el mapeo a los índices
    cuenta_paises_ordenado.index = cuenta_paises_ordenado.index.map(lambda x: country_names_mapping.get(x, x))


    paises = []
    menciones = []
    for pais, mencion in cuenta_paises_ordenado.items():
        paises.append(pais)
        menciones.append(mencion)



   
    impact_map = pd.DataFrame({
        'País': paises,
        'Menciones': menciones,
        #'Temas': paises_data['Áreas Clave']
    })
    fig = px.choropleth(
        impact_map,
        locations='País',
        locationmode='country names',
        color='Menciones',
        color_continuous_scale='Blues',
        height=700 if st.session_state.get('screen_width', 0) > 800 else 400,
        #title='Mapa de impacto potencial en Latinoamérica',
        # Añadir hover_data para mejorar los popups
        hover_name='País',
        hover_data={'País': False, 'Menciones': True} #'Temas':True}
    )

    # Ajustar el mapa para mostrar Latinoamérica correctamente
    fig.update_geos(
        visible=False,  # Quita el fondo de océanos/tierra
        lataxis_range=[-60, 35],
        lonaxis_range=[-120, -30],
        showcoastlines=True,
        coastlinecolor="darkgray",
        showland=True,
        landcolor="lightgray",
        showcountries=True,
        countrycolor="darkgray",
        framewidth=0  # Elimina el borde alrededor del mapa
    )

    fig.update_layout(
        margin=dict(t=50, b=0, l=0, r=0),
        coloraxis_colorbar_title='Cantidad de<br>artículos',
        geo=dict(
            showframe=False,  # Elimina el marco
            projection_type='equirectangular'  # Proyección que funciona bien para mostrar países
        ),
        dragmode = False
    )

    st.plotly_chart(fig, use_container_width=True)

