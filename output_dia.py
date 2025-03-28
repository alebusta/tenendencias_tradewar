import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
import base64


# Configuración de página
st.set_page_config(
    page_title="Monitor EEUU-LATAM | CEPAL Lab",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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
        <div class="trending-item"><span class="trending-number">1</span> Últimas decisiones y amenazas en la guerra comercial</div>
        <div class="trending-item"><span class="trending-number">2</span> Reacciones en EEUU, Mundo, Latinoamérica y El Caribe</div>
        <div class="trending-item"><span class="trending-number">3</span> Potenciales implicaciones: Impacto de las decisiones en las economías de la región</div>
        <div class="trending-item"><span class="trending-number">4</span> La guerra comercial en datos</div>
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
        <iframe width="100%" height="100%" src="https://www.youtube.com/embed/hVmn9mw3Zo4?si=eyHuqGDGmpR71w8J" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
    <div class="news-block news-text">
        <div class="news-title">Trump impone aranceles del 25% a autos importados</div>
        <div class="news-description">El arancel entrará en vigor el 2 de abril, fecha que ha llamado “Día de la Liberación”. Advirtió que la UE y Canadá enfrentarán represalias aún mayores si fortalecen sus alianzas contra Estados Unidos.</div>
        <a class="news-link" href="#">Ver más →</a>
    </div>  
    <!-- Fila 1 -->
    <div class="news-block news-text">
        <div class="news-title">Los aranceles de Trump conmocionan a los aliados de EE. UU. que fabrican automóviles</div>
        <div class="news-description">Reacciones desde México, Canadá y Japón a las nuevas medidas para vehículos y respuestos que entran en vigor el 3 de abril.</div>
        <a class="news-link" href="#">Ver más →</a>
    </div>
    <div class="news-block">
        <img class="news-image" src="data:image/jpeg;base64,{imagen}" />
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
        <div class="news-description">Este mapa permite visualizar las repercusiones de los últimos eventos en los países de la región durante la semana. A través del selector por país puede verse en detalle hechos relevantes
                y áreas clave de seguimiento respecto a los países con mayores menciones en los artículos seleccionados.</div>
        <a class="news-link" href="#">Ver más →</a>
    </div>
    """, unsafe_allow_html=True)

with col1:
    # Datos de ejemplo para países
    paises_data = pd.DataFrame({
        'País': ['Antigua y Barbuda', 'Argentina', 'Belize', 'Brazil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Ecuador', 'El Salvador', 'Guatemala', 'Honduras', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'Puerto Rico', 'República Dominicana', 'Surinam', 'Uruguay', 'Venezuela'],
        'Menciones': [1, 32, 1, 3, 8, 18, 2, 15, 17, 28, 4, 7, 91, 1, 36, 4, 3, 3, 8, 2, 3, 30],
        'Áreas Clave': [['desarrollo económico', 'economía', 'inclusión', 'integración regional', 'resiliencia'], ['gobierno', 'corrupción', 'sanciones', 'política', 'justicia'], ['gobierno', 'noticias de América Latina', 'política exterior', 'política internacional', 'relaciones diplomáticas'], ['Netflix', 'acuerdos comerciales', 'adquisiciones', 'cine', 'cooperación internacional'], ['cooperación internacional', 'desarrollo regional', 'economía', 'gobierno', 'gobierno migratorio'], ['música', 'política', 'economía', 'elecciones', 'gira musical'], ['gobierno', 'OEA', 'accidentes aéreos', 'desastres naturales', 'justicia'], ['migración', 'política migratoria', 'gobierno', 'inmigración', 'refugiados'], ['política', 'gobierno', 'diplomacia', 'elecciones', 'relaciones internacionales'], ['política migratoria', 'deportación', 'migración', 'inmigración', 'gobierno'], ['migración', 'seguridad fronteriza', 'tráfico de personas', 'conflicto comercial', 'corrupción'], ['economía', 'política migratoria', 'remesas', 'finanzas internacionales', 'migración'], ['economía', 'migración', 'aranceles', 'comercio internacional', 'moneda'], ['gobiernos autoritarios', 'libertad de prensa', 'medio ambiente', 'minería ilegal', 'periodismo'], ['relaciones internacionales', 'fútbol', 'política exterior', 'política internacional', 'comercio internacional'], ['política exterior', 'relaciones internacionales', 'conflicto internacional', 'guerra', 'historia'], ['aranceles', 'billetera digital', 'comercio internacional', 'criptomoneda', 'desastres naturales'], ['arte', 'autonomía', 'comunidad puertorriqueña', 'cultura', 'diáspora'], ['economía', 'espionaje', 'gobierno', 'inflación', 'moneda'], ['gobierno', 'organizaciones internacionales', 'OEA', 'deportación', 'política de la región'], ['Netflix', 'ataques cibernéticos', 'ciberataque', 'cine', 'confidencialidad'], ['petróleo', 'migración', 'gobierno', 'política migratoria', 'política energética']]
        })

    # Mapa interactivo de Latinoamérica
    
    # Crear un mapa de calor para visualizar impacto por país
    impact_map = pd.DataFrame({
        'País': paises_data['País'],
        'Menciones': paises_data['Menciones'],
        'Temas': paises_data['Áreas Clave']
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
        hover_data={'País': False, 'Menciones': True, 'Temas':True}
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
    data = {
        "Country": [
            "México", "Eslovaquia", "S.Corea", "Canadá", "Japón", "Hungría",
            "Suecia", "Alemania", "Austria", "S. África", "Reino Unido", "Brasil", "China", "India", "Rusia"
        ],
        "Automobiles": [5.5, 5.0, 2.3, 1.8, 1.3, 1.1, 0.9, 0.7, 0.5, 0.3, 0.2, 0.1, 0.05, 0.03, 0.02],
        "Parts":       [6.0, 5.3, 2.6, 2.0, 1.5, 1.3, 1.1, 0.9, 0.7, 0.4, 0.3, 0.2, 0.1, 0.05, 0.03]
    }

    df = pd.DataFrame(data)

    # Crear gráfico
    fig2 = go.Figure(data=[
        go.Bar(name='Automóviles', x=df["Country"], y=df["Automobiles"], marker_color='blue'),
        go.Bar(name='Autopartes', x=df["Country"], y=df["Parts"], marker_color='mediumturquoise')
    ])

    # Línea divisoria entre Top 10 y el resto
    fig2.add_shape(
        type="line",
        x0=9.5, x1=9.5, y0=0, y1=7,
        line=dict(color="black", width=2, dash="dash")
    )

    # Anotaciones
    fig2.add_annotation(x=4.5, y=6.8, text="Top 10 más expuestos", showarrow=False, font=dict(size=12))
    fig2.add_annotation(x=12.5, y=6.8, text="Otros", showarrow=False, font=dict(size=12))

    # Layout
    fig2.update_layout(
        title="Exportaciones de automóviles y respuestos como % de su respectivo PIB (2024)",
        barmode='group',
        yaxis_title="% del PIB",
        xaxis_tickangle=-45,
        height=500
    )

    st.plotly_chart(fig2, use_container_width=True)
    # Nota de fuente
    st.markdown("<p style='font-size: 0.9rem; color: gray;'>Adaptado de Capital Economics</p>", unsafe_allow_html=True)

    #st.image("https://images.unsplash.com/5/unsplash-kitsune-4.jpg?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max", use_column_width=True)

with col3:
    st.markdown("""
    <div class="news-text">
        <div class="news-title">Guerra comercial en Datos: Países más afectados por aranceles a los automóviles</div>
        <div class="news-description">De acuerdo a Capital Economics, México, Eslovaquia y Corea del Sur tienen la más alta exposició a estos aranceles, con hasta el 1,6% de su PIB en juego.</div>
        <a class="news-link" href="#">Ver más →</a>
    </div>
    """, unsafe_allow_html=True)



###### SECCIÓN 2: DETALLE DE IMPLICANCIAS ######
st.markdown("""
    <style>
        .chat-container {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 12px;
            max-width: 800px;
            margin: auto;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }

        .chat-bubble-user {
            background-color: #DCF8C6;
            padding: 10px 15px;
            border-radius: 12px;
            margin-bottom: 10px;
            align-self: flex-end;
            max-width: 70%;
        }

        .chat-bubble-bot {
            background-color: #fff;
            padding: 10px 15px;
            border-radius: 12px;
            margin-bottom: 10px;
            align-self: flex-start;
            max-width: 70%;
            border: 1px solid #ddd;
        }

        .chat-box {
            display: flex;
            flex-direction: column;
        }
    </style>
""", unsafe_allow_html=True)

st.header("💬 Asistente IA")
st.write("Asistente conversacional basado en inteligencia artificial para hacer consultas a la base de datos de noticias")
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input del usuario
with st.form(key="chat_form"):
    user_input = st.text_input("Escribe tu consulta:", placeholder="Ej: ¿Qué noticias hay sobre México esta semana?")
    submitted = st.form_submit_button("Enviar")

if submitted and user_input:
    # Agregar mensaje del usuario
    st.session_state.chat_history.append(("user", user_input))

    # Simular una respuesta genérica (placeholder)
    fake_response = "Esta es una respuesta simulada. Pronto podrás consultar la base de datos real de noticias."
    st.session_state.chat_history.append(("bot", fake_response))

# Mostrar historial de mensajes
for role, message in st.session_state.chat_history:
    bubble_class = "chat-bubble-user" if role == "user" else "chat-bubble-bot"
    st.markdown(f"<div class='chat-box'><div class='{bubble_class}'>{message}</div></div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

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
    st.markdown('<p class="small-text">© Cepal Lab - Versión de prueba </p>', unsafe_allow_html=True)
