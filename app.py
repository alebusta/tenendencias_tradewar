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
        <img class="news-image" src="https://www.swissinfo.ch/content/wp-content/uploads/sites/13/2025/04/cc4cebbe3922faad5d22a2fc52c49349-89198880.jpg?crop=8px,0px,1009px,673px&w=880&ver=d0310119" />
    </div>
    <div class="news-block news-text">  
        <div class="news-title">La guerra comercial golpea a México y castiga a América Latina</div>
        <div class="news-date">Publicado el 22 de abril de 2025</div>
        <div class="news-description">México será la única gran economía mundial en contracción este año debido a la guerra comercial abierta por Estados Unidos, que tira a la baja el crecimiento del resto de América Latina con la excepción de Argentina, según el Fondo Monetario Internacional.</div>
        <a class="news-link" href="https://www.swissinfo.ch/spa/la-guerra-comercial-golpea-a-m%c3%a9xico-y-castiga-a-am%c3%a9rica-latina/89198919">Ver más →</a>
    </div>    
    <!-- Fila 2 -->
    <div class="news-block news-text">
        <div class="news-title">Sheinbaum detalla que aún no se han logrado acuerdos sobre acero, aluminio y autos con Trump</div>
        <div class="news-date">Publicado el 21 de abril de 2025</div>
        <div class="news-description">La presidenta de México, Claudia Sheinbaum, informó que en la llamada que realizó con el presidente de Estados Unidos, Donald Trump, el pasado miércoles 16 de abril, se abordó la imposición de aranceles a las exportaciones mexicanas de acero, aluminio y productos automotrices. Detalló que, aunque no se alcanzaron acuerdos definitivos, se presentaron argumentos sólidos en defensa de la industria mexicana.</div>
        <a class="news-link" href="https://www.eleconomista.com.mx/politica/sheinbaum-logrado-acuerdo-sobre-acero-aluminio-industria-automotriz-trump-20250421-755676.html">Ver más →</a>
        </div>
   <div class="news-block">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
               <iframe 
            style="position:absolute;top:0;left:0;width:100%;height:100%;" 
            src="https://www.youtube.com/embed/755qWbp6yYs" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
        </iframe>
        </div>
    </div>
    <!-- Fila 3 -->
    <div class="news-block">
        <img class="news-image" src="https://static01.nyt.com/images/2025/04/18/multimedia/00biz-trade-soybean-wzfp/00biz-trade-soybean-wzfp-superJumbo.jpg?quality=75&auto=webp" />
    </div>
    <div class="news-block news-text">  
        <div class="news-title">China está buscando alternativas para reemplazar a los agricultores estadounidenses</div>
        <div class="news-date">Publicado el 20 de abril de 2025</div>
        <div class="news-description">Durante mucho tiempo, China ha dependido de Estados Unidos para el suministro de soya. Pero con los nuevos aranceles elevados, es probable que aumente aún más su dependencia de Brasil y Argentina.</div>
        <a class="news-link" href="https://www.nytimes.com/2025/04/20/business/tariffs-china-us-farmers.html">Ver más →</a>
    </div>
    <!-- Fila 4 -->
    <div class="news-block news-text">
        <div class="news-title">La mayor víctima de una guerra comercial con China, temen los expertos, podría ser el lugar de Estados Unidos en el mundo</div>
        <div class="news-date">Publicado el 18 de abril de 2025</div>
        <div class="news-description">La guerra arancelaria de la administración Trump con China suele verse principalmente desde la perspectiva económica. Pero para muchos economistas, la amenaza más grande es que la apuesta comercial global de Trump podría erosionar la principal fuente de autoridad mundial de Estados Unidos: las relaciones geopolíticas a largo plazo que ha cultivado durante casi un siglo.</div>
        <a class="news-link" href="https://www.msn.com/en-us/money/markets/the-biggest-casualty-of-a-china-trade-war-americas-place-in-the-world-experts-fear/ar-AA1DbwFI">Ver más →</a>
        </div>
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1DbFnA.img?w=768&h=612&m=6&x=222&y=247&s=600&d=158" />
    </div>
    <!-- Fila 5 -->
    <div class="news-block">
        <img class="news-image" src="https://i0.wp.com/efe.com/wp-content/uploads/2025/04/choque-de-Estados-Unidos-y-China-en-Latinoamerica.webp?w=900&ssl=1" />
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Los aranceles de Trump abren oportunidades en Latinoamérica a UE o India, según expertos</div>
        <div class="news-date">Publicado el 17 de abril de 2025</div>
        <div class="news-description">La agresiva política arancelaria de Donald Trump va dirigida principalmente a China, por ello los países latinoamericanos, cuyos principales socios comerciales son las dos potencias enfrentadas, buscan reducir su dependencia de ambas y diversificar, en una dinámica que abre oportunidades a potencias intermedias.</div>
        <a class="news-link" href="https://efe.com/euro-efe/2025-04-17/aranceles-trump-oportunidades-latinoamerica-ue/">Ver más →</a>
    </div>
    <!-- Fila 6 -->
    <div class="news-block news-text">
        <div class="news-title">La OMC advierte que la guerra comercial entre EE.UU. y China podría llevar al mundo a una recesión</div>
        <div class="news-date">Publicado el 16 de abril de 2025</div>
        <div class="news-description">La Organización Mundial del Comercio (OMC) advirtió este miércoles que las perspectivas para el comercio global se han "deteriorado drásticamente" a raíz de las medidas adoptadas por Estados Unidos.</div>
        <a class="news-link" href="https://www.msn.com/en-us/money/markets/global-trade-outlook-has-deteriorated-sharply-amid-trump-tariff-uncertainty-wto-warns/ar-AA1D29rV">Ver más →</a>
        </div>
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1D25Br.img?w=768&h=402&m=6" />
    </div>
    <!-- Fila 7 -->
    <div class="news-block">
        <img class="news-image" src="https://www.aljazeera.com/wp-content/uploads/2025/04/AP25106223653950-1-1744790356.jpg?resize=770%2C513&quality=80" />
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Xi llega a Malasia con un mensaje: China es un mejor socio que Trump</div>
        <div class="news-date">Publicado el 15 de abril de 2025</div>
        <div class="news-description">La visita del presidente chino Xi Jinping a Malasia es la segunda parada en el sudeste asiático en medio de los aranceles de Trump y la guerra comercial de Estados Unidos.</div>
        <a class="news-link" href="https://www.aljazeera.com/news/2025/4/16/xi-arrives-in-malaysia-with-a-message-chinas-a-better-partner-than-trump">Ver más →</a>
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
