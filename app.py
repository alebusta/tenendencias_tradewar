import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
import base64
from news_chatbot import news_chatbot_component
import json
from map import impact_map


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

###### SECCIÓN 1: ENCABEZADO ####### 
# CSS personalizado para el encabezado
st.markdown("""

<div class="header-banner">
    <div class="header-content">
        <h1 class="header-title">Monitor de tendencias: guerra comercial</h1>
        <p class="header-subtitle">Análisis estratégico de los principales sucesos de la nueva política comercial de Estados Unidos y sus implicaciones en América Latina y El Caribe.</p>
        <a href="/resumen" target="_self" class="header-link">Ver resumen &rarr;</a>
    </div>
</div>

<div class="trending-container">
    <div class="trending-bar">
        <div class="trending-title">PRINCIPALES SUCESOS</div>
        <div class="trending-item"><span class="trending-number">1</span> <a href="/medidas" target="_self">Últimas decisiones y amenazas en la guerra comercial</a></div>
        <div class="trending-item"><span class="trending-number">2</span> <a href="/base" target="_self">Reacciones en Latinoamérica y El Caribe</a></div>
        <div class="trending-item"><span class="trending-number">3</span> <a href="/mundo" target="_self">Reacciones en Estados Unidos y en el mundo</a></div>
        <div class="trending-item"><span class="trending-number">4</span> <a href="/datos" target="_self">La guerra comercial en datos</a></div>
    </div>
</div>


""", unsafe_allow_html=True)

###### SECCIÓN 2: NOTICIAS DESTACADAS #######

st.markdown(f"""
    <div class="news-grid">
    <!-- Fila 1 -->
    <div class="news-block">
        <img class="news-image" src="https://www.aljazeera.com/wp-content/uploads/2025/04/AP25106223653950-1-1744790356.jpg?resize=770%2C513&quality=80" />
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Xi llega a Malasia con un mensaje: China es un mejor socio que Trump</div>
        <div class="news-date">Publicado el 15 de abril de 2025</div>
        <div class="news-description">La visita del presidente chino Xi Jinping a Malasia es la segunda parada en el sudeste asiático en medio de los aranceles de Trump y la guerra comercial de Estados Unidos.</div>
        <a class="news-link" href="https://www.aljazeera.com/news/2025/4/16/xi-arrives-in-malaysia-with-a-message-chinas-a-better-partner-than-trump">Ver más →</a>
    </div>
    <!-- Fila 2 -->
    <div class="news-block news-text">
        <div class="news-title">Trump ordena una investigación arancelaria sobre todas las importaciones de minerales críticos a Estados Unidos</div>
        <div class="news-date">Publicado el 15 de abril de 2025</div>
        <div class="news-description">El presidente de Estados Unidos, Donald Trump, ordenó el martes una investigación sobre posibles nuevos aranceles a todas las importaciones de minerales críticos del país, una importante escalada en su disputa con los socios comerciales globales.</div>
        <a class="news-link" href="https://www.msn.com/en-gb/news/world/trump-orders-tariff-probe-on-all-us-critical-mineral-imports/ar-AA1CZtkX">Ver más →</a>
        </div>
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1CZhmB.img?w=768&h=510&m=6" />
    </div>
    <div class="news-grid">
    <!-- Fila 3 -->
    <div class="news-block">
        <img class="news-image" src="https://thewashingtoninquirer.com/wp-content/uploads/2025/04/Trump-Tarrifs-2048x1365.webp" />
    </div>
    <div class="news-block news-text">  
        <div class="news-title">La guerra comercial de Trump con China se intensifica, amenazando la estabilidad económica global.</div>
        <div class="news-date">Publicado el 14 de abril de 2025</div>
        <div class="news-description">La creciente guerra comercial del presidente Donald Trump con China se ha convertido en un enfrentamiento de alto riesgo, con profundas implicancias para las economías de Estados Unidos y del mundo. Los aranceles se elevan a niveles sin precedentes.</div>
        <a class="news-link" href="https://thewashingtoninquirer.com/trumps-trade-war-with-china-intensifies-threatening-global-economic-stability/">Ver más →</a>
    </div>
    <!-- Fila 4 -->
    <div class="news-block news-text">
            <div class="news-title">China y Vietnam firman decenas de nuevos acuerdos para fortalecer lazos mientras Trump intenta renegociar el comercio</div>
            <div class="news-date">Publicado el 14 de abril de 2025</div>
            <div class="news-description">El presidente chino Xi Jinping firmó el lunes decenas de acuerdos de cooperación con Vietnam en un intento por profundizar los lazos económicos regionales.</div>
            <a class="news-link" href="https://ijr.com/china-vietnam-sign-dozens-of-new-deals-strengthening-ties-as-trump-works-to-renegotiate-trade/">Ver más →</a>
        </div>
        <div class="news-block">
            <img class="news-image" src="https://ijr.com/wp-content/uploads/2025/04/china-vietnam-sign-dozens-of-new-deals-strengthening-ties-as-trump-works-to-renegotiate-trade-750x375.jpg" />
        </div>
</div>
            
""", unsafe_allow_html=True)

###### SECCIÓN 3: MAPAS Y DATOS #######
# Mapa
col1, col2 = st.columns(2)

with col2:
    st.markdown("""
    <div class="news-text">
        <div class="news-title">Repercusiones en los medios de América Latina y El Caribe</div>
        <div class="news-description">Este mapa permite visualizar las repercusiones de los últimos eventos en los países de la región durante el período analizado.</div>
        <a class="news-link" href="/base" target="_self">Ver más →</a>
    </div>
    """, unsafe_allow_html=True)

with col1:
    impact_map()


# Datos
col3, col4 = st.columns(2)

with col4:
    # Datos de aranceles para países de Latinoamérica y el Caribe de la lista original
    # Datos
    fechas = ['Feb 1', 'Feb 27', 'Abril 2', 'Abril 7','Abril 9']
    aumentos = [10, 10, 34, 50, 41]

    # Colores similares a los del gráfico original
    colores = ['#7a0c0a', '#d22c1e', '#ef4c48', '#ffa2a2', '#ffc4c4']

    # Crear figura con barras apiladas
    fig = go.Figure()

    for i in range(len(fechas)):
        fig.add_trace(go.Bar(
            x=["Aranceles a China"],
            y=[aumentos[i]],
            name=fechas[i],
            marker=dict(color=colores[i]),
            text=[f"{aumentos[i]}%"],
            textposition="inside"
        ))

    # Calcular el total
    total = sum(aumentos)

    # Agregar anotación del total
    fig.add_annotation(
        x="Aranceles a China",
        y=total,
        text=f"<b>Total: {total}%</b>",
        showarrow=False,
        yshift=10,  # Ajusta la distancia vertical sobre la barra
        font=dict(size=16),
    )

    # Configuración de diseño
    fig.update_layout(
        barmode='stack',
        title="Desglose de Aranceles de EEUU a China",
        title_font=dict(size=22, family="Arial Black"),
        xaxis_title="Gráfico adaptado de Yahoo Finance del 9 de abril de 2025 y actualizado con nuevos datos",
        yaxis_title="Valor (%)",
        yaxis=dict(range=[0, 150], ticksuffix="%"),
        legend_title_text="Fecha de anuncio",
        height=600
    )

    # Mostrar en Streamlit
    st.plotly_chart(fig)


with col3:
    st.markdown("""
    <div class="news-text">
        <div class="news-title">Guerra comercial en Datos: Lo último en la escalada de aranceles</div>
        <div class="news-date">Actualizado al 11 de abril de 2025</div>
        <div class="news-description">EE.UU. a China: Los aranceles totales base de EE.UU. sobre las importaciones chinas son del 145%. Esto incluye un arancel recíproco del 125% más aranceles adicionales del 20% impuestos previamente por cuestiones de fentanilo e inmigración ilegal.
        China a EE.UU.:China ha respondido elevando sus aranceles sobre bienes estadounidenses al 125%.<br>
        <gr>
        Global:<br>
        - Trump había autorizado una pausa de 90 días en sus planes de aranceles recíprocos para todos los países excepto China.<br>
        - El arancel base del 10% que entró en vigor el 5 de abril permanece en vigor para todas las importaciones afectadas a EE.UU.<br>
        - China ha indicado que no tiene intención de seguir subiendo los aranceles, incluso si EE.UU. continúa con sus escaladas, a menos que EE.UU. persista en infligir daño real a los intereses de China.<br>
        </div>
        <a class="news-link" href="/medidas">Ver más →</a>
    </div>
    """, unsafe_allow_html=True)



###### SECCIÓN 4: CHATBOT ######


st.header("💬 Asistente IA")
st.write("Asistente conversacional basado en inteligencia artificial para hacer consultas a la base de datos de noticias")

with st.expander("Haz clic aquí para abrir"):
    with open('noticias.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    news_chatbot_component(
        news_data=data,
        title="Asistente de Noticias CEPAL",
        height=400
    )

# Pie de página
st.markdown("---")
st.markdown("""
*Este reporte analiza las noticias de la semana centrándose en el impacto de las decisiones de la administración Trump en América Latina, el Caribe y el mundo. 
Se utiliza un enfoque basado en la frecuencia de las noticias y su potencial impacto, prestando atención a los últimos desenlaces como indicadores de tendencias futuras.
La clasificación de noticias, análisis y reportes automatizados asistidos por Inteligencia Artificial se encuentran en un proceso de desarrollo experimental en el cual
es fundamental la validación experta humana. Por lo tanto los resultados de los análisis deben tomarse con la debida cautela.*

""")
st.markdown('<p class="small-text" text-align="right">©2025 Cepal Lab</p>', unsafe_allow_html=True)
