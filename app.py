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
from grafico import crear_grafico_fmi, X_latam_china
from babel.dates import format_date
from shared_data import get_dataframe


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
        <a href="/resumen" target="_self" class="header-link">Ver resúmenes semanales &rarr;</a>
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

df = get_dataframe()

# Primero, calcula los valores necesarios del DataFrame

df['date_process'] = pd.to_datetime(df['date_process'])
# Usar babel para formatear las fechas en español
fecha_min = format_date(df['date_process'].min(), format="d 'de' MMMM 'de' y", locale='es').lower()
fecha_max = format_date(df['date_process'].max(), format="d 'de' MMMM 'de' y", locale='es').lower()
total_noticias = len(df)

st.markdown(f"""
<div class="news-ticker">
    <div class="ticker-content">
        Base de datos con {total_noticias} noticias relacionadas con la guerra comercial registradas entre el {fecha_min} y el {fecha_max} 
    </div>
</div>           
""", unsafe_allow_html=True)


###### SECCIÓN 2: NOTICIAS DESTACADAS #######

st.markdown(f"""
    <div class="news-grid">
     <!-- Fila 1 -->
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1G0OxP.img?w=768&h=512&m=6"/>
    </div>
    <div class="news-block news-text">  
        <div class="news-title">La OCDE rebaja las perspectivas económicas de EE. UU. mientras los aranceles de Trump afectan el crecimiento mundial</div>
        <div class="news-date">Publicado el 03 de junio de 2025</div>
        <div class="news-description">El pronóstico de crecimiento económico de Estados Unidos fue recortado drásticamente el martes por la Organización para la Cooperación y el Desarrollo Económicos, u OCDE, que atribuyó el sombrío panorama en parte a los aranceles emitidos por el presidente Donald Trump.</div>
        <a class="news-link" href="https://www.msn.com/en-us/money/markets/us-economic-outlook-slashed-by-oecd-as-trumps-tariffs-upend-global-growth/ar-AA1G0D1b">Ver más →</a>
    </div>  
    <!-- Fila 2 -->
    <div class="news-block news-text">
        <div class="news-title">Trump duplica aranceles al acero y aluminio: alerta en la industria argentina</div>
        <div class="news-date">Publicado el 2 de junio de 2025</div>
        <div class="news-description">La duplicación de aranceles al acero y aluminio por parte de Trump pone en jaque a la industria metalúrgica argentina, afectando exportaciones por US$600 millones y generando incertidumbre en el sector</div>
        <a class="news-link" href="https://aceroyroca.com/2025/06/02/trump-duplica-aranceles-al-acero-y-aluminio-alerta-en-la-industria-argentina/">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://aceroyroca.com/wp-content/uploads/2025/06/ACERO-Y-ROCA.TRUMP_.avif"/>
    </div>           
     <!-- Fila 3 -->
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1FU1S7.img"/>
    </div>
    <div class="news-block news-text">  
        <div class="news-title">China dice que EE. UU. socavó el acuerdo comercial de Ginebra tras acusaciones de Trump sobre violaciones por parte de Pekín</div>
        <div class="news-date">Publicado el 01 de junio de 2025</div>
        <div class="news-description">Las fricciones comerciales entre Washington y Pekín se reavivaron después de una pausa que siguió a una reunión entre el Secretario del Tesoro de EE. UU., Scott Bessent, y su homólogo chino.</div>
        <a class="news-link" href="https://www.msn.com/en-us/money/markets/china-says-the-u-s-undermined-geneva-trade-deal-after-trump-accuses-beijing-of-violations/ar-AA1FTXKH">Ver más →</a>
    </div>      
    <!-- Fila 4 -->
    <div class="news-block news-text">
        <div class="news-title">Así quedan los aranceles de Trump tras el fallo judicial: tarifas anuladas y medidas que siguen vigentes</div>
        <div class="news-date">Publicado el 29 de mayo de 2025</div>
        <div class="news-description">El Tribunal de Comercio Internacional declaró ilegales los aranceles generalizados basados en la ley IEEPA, pero se mantienen las tarifas impuestas bajo la Sección 232</div>
        <a class="news-link" href="https://www.antena3.com/noticias/mundo/asi-quedan-aranceles-trump-fallo-judicial-tarifas-anuladas-medidas-que-siguen-vigentes_2025052968389e04812a8f1e6a09309e.html">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://fotografias.antena3.com/clipping/cmsimages02/2025/05/26/21EE7D1A-FBB5-4E26-A54C-273F7CEBDB85/97.jpg?crop=1920,1080,x0,y0&width=1600&height=900&optimize=low&format=webply"/>
    </div>           
     <!-- Fila 5 -->
    <div class="news-block">
        <img class="news-image" src="https://www.nacion.com/resizer/v2/QIEXGH4LOBC2JNELGL2U6WYEQU.jpeg?smart=true&auth=961e267e4beaed86d16720fb0a4e109eb9921b6108a7ca2ce5a3c26d2a007d66&width=720&height=405"/>
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Tribunal de Estados Unidos bloquea la mayoría de los aranceles: ‘Trump se extralimitó’</div>
        <div class="news-date">Publicado el 28 de mayo de 2025</div>
        <div class="news-description">El fallo prohíbe la mayoría de las categorías de nuevos aranceles (aquellos impuestos a países, incluidos China, Canadá y México).</div>
        <a class="news-link" href="https://www.nacion.com/el-mundo/tribunal-de-estados-unidos-bloquea-la-mayoria-de/EGDIR43RNBH6HDB3CDA4TY6NBU/story/">Ver más →</a>
    </div>      
    <!-- Fila 6 -->
    <div class="news-block news-text">
        <div class="news-title">Los líderes de la ASEAN coinciden en que los acuerdos arancelarios con Estados Unidos no deben perjudicar a los demás miembros.</div>
        <div class="news-date">Publicado el 28 de mayo de 2025</div>
        <div class="news-description">Los líderes del Sudeste Asiático llegaron a un entendimiento el martes de que cualquier acuerdo bilateral que puedan alcanzar con Estados Unidos sobre aranceles comerciales no dañará las economías de los demás miembros</div>
        <a class="news-link" href="https://www.bworldonline.com/top-stories/2025/05/28/675435/asean-leaders-agree-tariff-deals-with-us-should-not-harm-fellow-members/">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://www.bworldonline.com/wp-content/uploads/2023/10/ASEAN-logo.jpg"/>
    </div>        
     <!-- Fila 7 -->
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1FwUCk.img? style="width: 200px !important; height: auto !important;"/>
    </div>
    <div class="news-block news-text">  
        <div class="news-title">BMI: Latinoamérica no se ha visto golpeada por aranceles de Trump; economía colombiana se recuperaría</div>
        <div class="news-date">Publicado el 26 de mayo de 2025</div>
        <div class="news-description">Sus cálculos anticipan una recuperación del Producto Interno Bruto (PIB) este año alrededor del 3 % y el siguiente, gracias, principalmente, al aporte del consumo y las exportaciones.</div>
        <a class="news-link" href="https://www.msn.com/es-co/noticias/other/bmi-latinoam%C3%A9rica-no-se-ha-visto-golpeada-por-aranceles-de-trump-econom%C3%ADa-colombiana-se-recuperar%C3%ADa/ar-AA1FwUCM">Ver más →</a>
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

    X_latam_china()


with col3:
    st.markdown("""
    <div class="news-text">
        <div class="news-title">Guerra comercial en Datos: Volumen del comercio con China</div>
        <div class="news-date">Actualizado al 12 de mayo de 2025</div>
        <div class="news-description"> En medio de la guerra comercial de Trump, China y Latinoamérica buscan fortalecer sus lazos económicos, con un intercambio comercial que alcanzó los 500.000 millones de dólares en 2024 y que podría superar a Estados Unidos en el futuro cercano. Esta creciente relación se presenta como una oportunidad para la región, impulsada por la imposición de aranceles que impactan las relaciones comerciales entre Washington y Pekín.
        </div>
        <a class="news-link" href="https://www.elperiodico.com/es/internacional/20250511/china-latinoamerica-profundizar-relaciones-guerra-comercial-trump-117218567">Ver más →</a>
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
st.markdown('<p class="small-text" text-center="right">©2025 Cepal Lab - versión demo v0.1.0</p>', unsafe_allow_html=True)
