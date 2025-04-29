import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, datetime
import base64
from news_chatbot import news_chatbot_component
import json
from map import impact_map
from grafico import crear_grafico_fmi
import locale

# Configurar locale en español
locale.setlocale(locale.LC_TIME, 'es_ES')


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

## Ticker con contador de noticias

df = pd.read_csv('database.csv')

# Primero, calcula los valores necesarios del DataFrame

df['date_process'] = pd.to_datetime(df['date_process'])
fecha_min = df['date_process'].min().strftime('%d de %B de %Y').lower()
fecha_max = df['date_process'].max().strftime('%d de %B de %Y').lower()
total_noticias = len(df)

st.markdown(f"""
<div class="news-ticker">
    <div class="ticker-content">
        Base de datos actual: {total_noticias} noticias registradas entre el {fecha_min} y el {fecha_max} 
    </div>
</div>           
""", unsafe_allow_html=True)


###### SECCIÓN 2: NOTICIAS DESTACADAS #######

st.markdown(f"""
    <div class="news-grid">
    <!-- Fila 1 -->
    <div class="news-block">
        <img class="news-image" src="https://imagenes.elpais.com/resizer/v2/KYM6WPM7E2SWYLJQN655ERPBXE.jpg?auth=407f003f1762af940440d383c4b2d5ee868345e0e3d71c10959635bb0b12c772&width=1200" />
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Los BRICS debaten en Brasil su respuesta a la guerra arancelaria declarada por Trump</div>
        <div class="news-date">Publicado el 28 de abril de 2025</div>
        <div class="news-description">El canciller Vieira, el anfitrión, insta al bloque del sur global a centrarse en la defensa del multilateralismo sin ser “un bloque de enfrentamiento”.</div>
        <a class="news-link" href="https://elpais.com/america/2025-04-28/los-brics-debaten-en-brasil-su-respuesta-a-la-guerra-arancelaria-declarada-por-trump.html">Ver más →</a>
    </div>    
    <!-- Fila 2 -->
    <div class="news-block news-text">
        <div class="news-title">Aranceles, aunque bajos tienden a ser más nocivos para la región</div>
        <div class="news-date">Publicado el 27 de abril de 2025</div>
        <div class="news-description">El FMI advierte que una desaceleración del crecimiento mundial podría afectar a la demanda de productos básicos.</div>
        <a class="news-link" href="https://www.expreso.ec/actualidad/economia/aranceles-bajos-tienden-nocivos-region-240508.html">Ver más →</a>
        </div>
    <div class="news-block">
        <img class="news-image" src="https://imagenes.expreso.ec/files/image_780_477/uploads/2025/04/27/680eba744a9fe.jpeg" />
    </div>
    <!-- Fila 3 -->
    <div class="news-block">
        <img class="news-image" src="https://apicms.thestar.com.my/uploads/images/2025/04/25/thumbs/700/3282854.webp" />
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Funcionarios estadounidenses evalúan reducir las tarifas de importación de automóviles</div>
        <div class="news-date">Publicado el 24 de abril de 2025</div>
        <div class="news-description">La administración Trump está considerando la posibilidad de reducir ciertos aranceles dirigidos a la industria automotriz que, según advirtieron los ejecutivos de los fabricantes de automóviles, supondrían un duro golpe a las ganancias y al empleo.</div>
        <a class="news-link" href="https://www.thestar.com.my/business/business-news/2025/04/25/us-officials-weigh-reducing-auto-import-fees#goog_rewarded">Ver más →</a>
    </div>    
    <!-- Fila 4 -->
    <div class="news-block news-text">
        <div class="news-title">La verdadera amenaza tras la guerra comercial de Trump: la ofensiva monetaria de China</div>
        <div class="news-date">Publicado el 23 de abril de 2025</div>
        <div class="news-description">China ha trabajado incansablemente para elevar el perfil internacional del RMB. Si bien el progreso ha sido gradual, conlleva riesgos reales para el dominio del dólar estadounidense.</div>
        <a class="news-link" href="https://thediplomat.com/2025/04/the-real-threat-behind-trumps-trade-war-chinas-currency-offensive/">Ver más →</a>
        </div>
    <div class="news-block">
        <img class="news-image" src="https://thediplomat.com/wp-content/uploads/2021/04/sizes/medium/thediplomat-2021-04-19-6.jpg" />
    </div>
    <!-- Fila 5 -->
    <div class="news-block">
        <img class="news-image" src="https://www.swissinfo.ch/content/wp-content/uploads/sites/13/2025/04/cc4cebbe3922faad5d22a2fc52c49349-89198880.jpg?crop=8px,0px,1009px,673px&w=880&ver=d0310119" />
    </div>
    <div class="news-block news-text">  
        <div class="news-title">La guerra comercial golpea a México y castiga a América Latina</div>
        <div class="news-date">Publicado el 22 de abril de 2025</div>
        <div class="news-description">México será la única gran economía mundial en contracción este año debido a la guerra comercial abierta por Estados Unidos, que tira a la baja el crecimiento del resto de América Latina con la excepción de Argentina, según el Fondo Monetario Internacional.</div>
        <a class="news-link" href="https://www.swissinfo.ch/spa/la-guerra-comercial-golpea-a-m%c3%a9xico-y-castiga-a-am%c3%a9rica-latina/89198919">Ver más →</a>
    </div>    
    <!-- Fila 6 -->
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
    <!-- Fila 7 -->
    <div class="news-block">
        <img class="news-image" src="https://static01.nyt.com/images/2025/04/18/multimedia/00biz-trade-soybean-wzfp/00biz-trade-soybean-wzfp-superJumbo.jpg?quality=75&auto=webp" />
    </div>
    <div class="news-block news-text">  
        <div class="news-title">China está buscando alternativas para reemplazar a los agricultores estadounidenses</div>
        <div class="news-date">Publicado el 20 de abril de 2025</div>
        <div class="news-description">Durante mucho tiempo, China ha dependido de Estados Unidos para el suministro de soya. Pero con los nuevos aranceles elevados, es probable que aumente aún más su dependencia de Brasil y Argentina.</div>
        <a class="news-link" href="https://www.nytimes.com/2025/04/20/business/tariffs-china-us-farmers.html">Ver más →</a>
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

    crear_grafico_fmi()


with col3:
    st.markdown("""
    <div class="news-text">
        <div class="news-title">Guerra comercial en Datos: Nuevas previsiones del FMI</div>
        <div class="news-date">Publicado el 22 de abril de 2025</div>
        <div class="news-description">   Estos datos representan las previsiones de crecimiento económico del Fondo Monetario Internacional (FMI) 
    para el año 2025, publicados el 22 de abril de 2025. El FMI recortó en medio punto la previsión del crecimiento económico global para 2025, hasta el 2.8%, 
    debido principalmente a la guerra comercial iniciada por el presidente de Estados Unidos.Para América Latina y el Caribe, el FMI pronostica que el crecimiento económico se modere al 2% en 2025, 
    antes de repuntar al 2.4% en 2026.
        </div>
        <a class="news-link" href="https://larepublica.pe/economia/2025/04/22/culpan-a-trump-fmi-alerta-sobre-recesion-en-eeuu-y-menor-crecimiento-global-como-se-traduce-a-peru-hnews-700964">Ver más →</a>
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
Importante:
*Este reporte recopila y analiza noticias relacionadas con la guerra comercial y sus repercusiones en América Latina, el Caribe y el mundo. 
Se utilizan herramientas automatizadas para la captura de noticias y para la generación de reportes. La clasificación de noticias, análisis y reportes automatizados 
asistidos por Inteligencia Artificial se encuentran en un proceso de desarrollo experimental en el cual es fundamental la validación experta humana. 
Por lo tanto los resultados de los análisis deben tomarse con la debida cautela chequeando apropiadamente las fuentes originales que se ponen a disposición antes
de hacer cualquier cita de estos datos.*

""")
st.markdown('<p class="small-text" text-align="right">©2025 Cepal Lab</p>', unsafe_allow_html=True)
