import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
import base64
from news_chatbot import news_chatbot_component
import json


# Configuración de página
st.set_page_config(
    page_title="Monitor EEUU-LATAM | CEPAL Lab",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="collapsed"
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

# Función para codificar la imagen en base64
def get_base64_of_bin_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Cargar CSS desde un archivo externo
with open("style.css", "r") as f:
    css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Codificar la imagen
img_base64 = get_base64_of_bin_file("assets/22130.jpg")
st.markdown(f"""
    <style>
    .header-banner {{
        background-image: url("data:image/jpeg;base64,{img_base64}");
    }}
    </style>
""", unsafe_allow_html=True)

periodo = "Análisis de Noticias: Impacto de la Administración Trump en América Latina, el Caribe y el Mundo (3-16 de marzo de 2025)"

# Encabezado
# CSS personalizado para el encabezado
st.markdown("""

<div class="header-banner">
    <div class="header-content">
        <h1 class="header-title">Monitor de tendencias: guerra comercial</h1>
        <p class="header-subtitle">Análisis estratégico de los principales sucesos de la nueva política comercial de Estados Unidos y sus implicaciones en América Latina y El Caribe.</p>
        <a href="#resumen" class="header-link">Ver resumen &rarr;</a>
    </div>
</div>

<div class="trending-bar">
        <div class="trending-title">PRINCIPALES<br>SUCESOS  </div>
        <div class="trending-item"><span class="trending-number">1</span> <a href="/medidas" target="_self"> Últimas decisiones y amenazas en la guerra comercial</a></div>
        <div class="trending-item"><span class="trending-number">2</span> <a href="/base" target="_self">Reacciones en Latinoamérica y El Caribe</a></div>
        <div class="trending-item"><span class="trending-number">3</span> <a href="/mundo" target="_self"> Reacciones en Estados Unidos y en el mundo</a></div>
        <div class="trending-item"><span class="trending-number">4</span> <a href="/datos" target="_self">La guerra comercial en datos</div>
</div>
""", unsafe_allow_html=True)

# Contenido de la aplicación

# Cargar la imagen como base64 para incrustarla directamente
with open("assets/cars-exports.jpg", "rb") as f:
    data = f.read()
    imagen = base64.b64encode(data).decode()

st.markdown(f"""
<div class="news-grid">
    <!-- Fila 1 -->
    <div class="news-block">
        <iframe width="100%" height="110%" src="https://www.youtube.com/embed/xlNun19KbVw?si=-0XklfEgp-Y0LwkN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Trump anuncia aranceles el 'Día de la Liberación' que afectarán a más de 150 países</div>
        <div class="news-description">Países enfrentarán un arancel de EE.UU. equivalente a la mitad de la tasa que ellos imponen a los productos estadounidenses, según lo determine la Casa Blanca, con un mínimo del 10%. Trump señaló que este cálculo incluye barreras comerciales no monetarias y la manipulación cambiaria.</div>
        <a class="news-link" href="#">Ver más →</a>
    </div>  
    <!-- Fila 1 -->
    <div class="news-block news-text">
        <div class="news-title">Así es como los países planean responder a los aranceles de Trump</div>
        <div class="news-description">Gobiernos de todo el mundo reaccionaron después de que las amplias medidas comerciales del presidente Trump afectaran a los principales socios comerciales de Estados Unidos con fuertes aranceles adicionales. Esto es lo que prometen hacer o no, según Reuters.</div>
        <a class="news-link" href="https://finance.yahoo.com/news/factbox-trump-tariffs-draw-global-024705290.html">Ver más →</a>
    </div>
    <div class="news-block">
        <img class="news-image" src="https://static01.nyt.com/images/2025/04/02/multimedia/02int-tariffs-diplo-lgchESP/02int-tariffs-diplo-lgch-mediumThreeByTwo440.jpg" />
    </div>
</div>
            
""", unsafe_allow_html=True)

# Ajustamos separación entre filas
st.markdown("<div style='margin-top: 0px'></div>", unsafe_allow_html=True)

# Segunda fila (texto + gráfico con columnas de Streamlit)
col1, col2 = st.columns(2)

with col2:
    st.markdown("<div style='margin-top: 100px'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="news-text">
        <div class="news-title">Repercusiones en los principales medios de la América Latina y El Caribe</div>
        <div class="news-description">Este mapa permite visualizar las repercusiones de los últimos eventos en los países de la región durante el período analizado.</div>
        <a class="news-link" href="/base" target="_self">Ver más →</a>
    </div>
    """, unsafe_allow_html=True)

with col1:
    # Datos de ejemplo para países
    paises_data = pd.DataFrame({
        'País': ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Ecuador', 'El Salvador', 'Guatemala', 'Haiti', 'Mexico', 'Nicaragua', 'Panama', 'Peru', 'Dominican Republic', 'Uruguay', 'Venezuela'],
        'Menciones': [11, 2, 9, 7, 12, 4, 2, 5, 4, 4, 1, 6, 1, 3, 4, 4, 2, 8],
        #'Áreas Clave': [['desarrollo económico', 'economía', 'inclusión', 'integración regional', 'resiliencia'], ['gobierno', 'corrupción', 'sanciones', 'política', 'justicia'], ['gobierno', 'noticias de América Latina', 'política exterior', 'política internacional', 'relaciones diplomáticas'], ['Netflix', 'acuerdos comerciales', 'adquisiciones', 'cine', 'cooperación internacional'], ['cooperación internacional', 'desarrollo regional', 'economía', 'gobierno', 'gobierno migratorio'], ['música', 'política', 'economía', 'elecciones', 'gira musical'], ['gobierno', 'OEA', 'accidentes aéreos', 'desastres naturales', 'justicia'], ['migración', 'política migratoria', 'gobierno', 'inmigración', 'refugiados'], ['política', 'gobierno', 'diplomacia', 'elecciones', 'relaciones internacionales'], ['política migratoria', 'deportación', 'migración', 'inmigración', 'gobierno'], ['migración', 'seguridad fronteriza', 'tráfico de personas', 'conflicto comercial', 'corrupción'], ['economía', 'política migratoria', 'remesas', 'finanzas internacionales', 'migración'], ['economía', 'migración', 'aranceles', 'comercio internacional', 'moneda'], ['gobiernos autoritarios', 'libertad de prensa', 'medio ambiente', 'minería ilegal', 'periodismo'], ['relaciones internacionales', 'fútbol', 'política exterior', 'política internacional', 'comercio internacional'], ['política exterior', 'relaciones internacionales', 'conflicto internacional', 'guerra', 'historia'], ['aranceles', 'billetera digital', 'comercio internacional', 'criptomoneda', 'desastres naturales'], ['arte', 'autonomía', 'comunidad puertorriqueña', 'cultura', 'diáspora'], ['economía', 'espionaje', 'gobierno', 'inflación', 'moneda'], ['gobierno', 'organizaciones internacionales', 'OEA', 'deportación', 'política de la región'], ['Netflix', 'ataques cibernéticos', 'ciberataque', 'cine', 'confidencialidad'], ['petróleo', 'migración', 'gobierno', 'política migratoria', 'política energética']]
        })

    # Mapa interactivo de Latinoamérica
    
    # Crear un mapa de calor para visualizar impacto por país
    impact_map = pd.DataFrame({
        'País': paises_data['País'],
        'Menciones': paises_data['Menciones'],
        #'Temas': paises_data['Áreas Clave']
    })

    fig = px.choropleth(
        impact_map,
        locations='País',
        locationmode='country names',
        color='Menciones',
        color_continuous_scale='Blues',
        height=700,
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

# Fila 1 (ahora también usando st.columns)
col3, col4 = st.columns(2)

with col4:
    # Datos de aranceles para países de Latinoamérica y el Caribe de la lista original
    data = {
        "PAÍS": [
            "ARGENTINA", "BRASIL", "BOLIVIA", "CHILE", "COLOMBIA", "COSTA RICA", 
            "REPÚBLICA DOMINICANA", "ECUADOR", "EL SALVADOR", "GUATEMALA", 
            "HONDURAS", "NICARAGUA", "PERÚ", "PANAMÁ", "TRINIDAD Y TOBAGO", "URUGUAY", "VENEZUELA"
        ],
        "TARIFA ESTIMADA CONTRA EE.UU. (%)": [
            10, 10, 20, 10, 10, 17, 
            10, 12, 10, 10, 
            10, 36, 10, 10, 12, 10, 29
        ],
        "TARIFA RECÍPROCA DE EE.UU. (%)": [
            10, 10, 10, 10, 10, 10, 
            10, 10, 10, 10, 
            10, 18, 10, 10, 10, 10, 15
        ]
    }

    # Creación del dataframe
    df = pd.DataFrame(data)

    # Usando método de Streamlit para estilizar la tabla

    # Agregar CSS personalizado
    st.markdown("""
    <style>
        .stDataFrame {
            font-family: 'Helvetica Neue', Arial, sans-serif;
        }
        .stDataFrame thead tr th {
            background-color: #1A476F !important;
            color: white !important;
        }
        .stDataFrame tbody tr:nth-child(even) {
            background-color: #f5f5f5;
        }
    </style>
    """, unsafe_allow_html=True)

    # Mostrar la tabla
    st.dataframe(
        df, 
        use_container_width=True,
        hide_index=True,
        column_config={
            "PAÍS": st.column_config.TextColumn(
                "PAÍS",
                width="medium"
            ),
            "TARIFA ESTIMADA CONTRA EE.UU. (%)": st.column_config.NumberColumn(
                "TARIFA ESTIMADA CONTRA EE.UU. (%)",
                format="%d%%",
                width="medium"
            ),
            "TARIFA RECÍPROCA DE EE.UU. (%)": st.column_config.NumberColumn(
                "TARIFA RECÍPROCA DE EE.UU. (%)",
                format="%d%%",
                width="medium"
            )
        }
    )


with col3:
    st.markdown("""
    <div class="news-text">
        <div class="news-title">Guerra comercial en Datos: Países de la región afectados por aranceles recíprocos</div>
        <div class="news-description">Aranceles anunciados el 2 de abril. La Casa Blanca informó más tarde que para México y Canadá, las órdenes ejecutivas anteriores siguen vigentes, lo que significa que los productos incluidos en el tratado de libre comercio "seguirá sujetos a un arancel del 0%, los que no lo cumplen, a un arancel del 25%, y los productos de energía y potasa que no lo cumplen, a un arancel del 10%".</div>
        <a class="news-link" href="https://www.elobservador.com.uy/estados-unidos/bbc-news-mundo/que-aranceles-les-ha-impuesto-trump-los-paises-america-latina-y-que-no-incluyen-mexico-n5992631">Ver más →</a>
    </div>
    """, unsafe_allow_html=True)



###### SECCIÓN 2: DETALLE DE IMPLICANCIAS ######


st.header("💬 Asistente IA")
st.write("Asistente conversacional basado en inteligencia artificial para hacer consultas a la base de datos de noticias")

with st.expander("Haz clic aquí para abrir"):
    with open('noticias_abr_03.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    news_chatbot_component(
        news_data=data,
        title="Asistente de Noticias CEPAL",
        height=250
    )

# Pie de página
st.markdown("---")
st.markdown("""
*Este reporte analiza las noticias de la semana centrándose en el impacto de las decisiones de la administración Trump en América Latina, el Caribe y el mundo. 
Se utiliza un enfoque basado en la frecuencia de las noticias y su potencial impacto, prestando atención a los últimos desenlaces como indicadores de tendencias futuras.
La clasificación de noticias, análisis y reportes automatizados asistidos por Inteligencia Artificial se encuentran en un proceso de desarrollo experimental en el cual
es fundamental la validación experta humana. Por lo tanto los resultados de los análisis deben tomarse con la debida cautela.*"

""")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown('<p class="small-text">Reporte preparado por CEPAL Lab para el Trade Emergency Team</p>', unsafe_allow_html=True)
with col2:
    st.markdown('<p class="small-text">Datos actualizados al 17 de marzo, 2025</p>', unsafe_allow_html=True)
with col3:
    st.markdown('<p class="small-text" text-align="right">©2025 Cepal Lab - Versión de prueba </p>', unsafe_allow_html=True)
