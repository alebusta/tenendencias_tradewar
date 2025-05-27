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
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1FwUCk.img?w=597&h=523&m=6"/>
    </div>
    <div class="news-block news-text">  
        <div class="news-title">BMI: Latinoamérica no se ha visto golpeada por aranceles de Trump; economía colombiana se recuperaría</div>
        <div class="news-date">Publicado el 26 de mayo de 2025</div>
        <div class="news-description">Sus cálculos anticipan una recuperación del Producto Interno Bruto (PIB) este año alrededor del 3 % y el siguiente, gracias, principalmente, al aporte del consumo y las exportaciones.</div>
        <a class="news-link" href="https://www.msn.com/es-co/noticias/other/bmi-latinoam%C3%A9rica-no-se-ha-visto-golpeada-por-aranceles-de-trump-econom%C3%ADa-colombiana-se-recuperar%C3%ADa/ar-AA1FwUCM">Ver más →</a>
    </div>          
    <!-- Fila 2 -->
    <div class="news-block news-text">
        <div class="news-title">Trump anuncia que retrasará un arancel del 50 % a la Unión Europea hasta julio</div>
        <div class="news-date">Publicado el 25 de mayo de 2025</div>
        <div class="news-description">El presidente Donald Trump anunció el domingo que Estados Unidos retrasará la implementación de un arancel del 50% sobre productos de la Unión Europea del 1 de junio al 9 de julio.</div>
        <a class="news-link" href="https://www.msn.com/es-ar/noticias/other/trump-anuncia-que-retrasar%C3%A1-un-arancel-del-50-a-la-uni%C3%B3n-europea-hasta-julio/ar-AA1FsCtG">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1FsCtD.img?w=614&h=409&m=6"/>
    </div>        
     <!-- Fila 3 -->
    <div class="news-block">
        <img class="news-image" src="https://admin.gfmreview.com/images/custom_content/1747911948.png"/>
    </div>
    <div class="news-block news-text">  
        <div class="news-title">El acto de equilibrio de Brasil entre EE. UU. y China</div>
        <div class="news-date">Publicado el 22 de mayo de 2025</div>
        <div class="news-description">La diplomacia de doble vía de Brasil —favoreciendo los lazos políticos con Pekín y los vínculos comerciales con Estados Unidos— puede ser su única ruta viable.</div>
        <a class="news-link" href="https://www.gfmreview.com/breaking/brazil-s-balancing-act-between-us-china">Ver más →</a>
    </div>          
    <!-- Fila 4 -->
    <div class="news-block news-text">
        <div class="news-title">La UE envía una propuesta comercial a EE.UU. para cerrar un acuerdo</div>
        <div class="news-date">Publicado el 21 de mayo de 2025</div>
        <div class="news-description">Se esperaba que la Unión Europea compartiera una propuesta comercial revisada con Estados Unidos, con el objetivo de dar nuevo impulso a las negociaciones con el gobierno del presidente Donald Trump en medio de un persistente escepticismo.</div>
        <a class="news-link" href="https://www.bloomberg.com/news/articles/2025-05-21/eu-prepares-trade-proposal-for-us-to-steer-momentum-into-talks">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://assets.bwbx.io/images/users/iqjWHBFdfxIU/irWxnkl3wBxg/v1/1200x800.webp"/>
    </div>     
     <!-- Fila 5 -->
    <div class="news-block">
        <img class="news-image" src="https://imgmedia.larepublica.pe/640x371/larepublica/original/2025/05/20/682ca61ccb9d4fa2b60d7709.webp"/>
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Exportaciones de iPhone desde China a EE.UU. caen 72% y Apple lanza agresivos descuentos</div>
        <div class="news-date">Publicado el 20 de mayo de 2025</div>
        <div class="news-description">Apple ha intensificado su producción en India, mientras el presidente de los Estados Unidos, Donald Trump, critica esta estrategia. Las caídas de exportación reflejan la fragilidad de las cadenas de suministro.</div>
        <a class="news-link" href="https://larepublica.pe/economia/2025/05/20/exportaciones-de-iphone-desde-china-a-eeuu-caen-72-en-abril-por-aranceles-hnews-1762880">Ver más →</a>
    </div>          
    <!-- Fila 6 -->
    <div class="news-block news-text">
        <div class="news-title">Costa Rica negocia con Estados Unidos para suspender arancel impuesto por Trump</div>
        <div class="news-date">Publicado el 19 de mayo de 2025</div>
        <div class="news-description">Jerarca de Comex confirmó que en junio habrá dos reuniones más con la participación de la viceministra Indiana Trejos.</div>
        <a class="news-link" href="https://www.nacion.com/economia/costa-rica-tuvo-primera-reunion-en-estados-unidos/RUSWHFI47NF3XBY2RZIZF27PZU/story/">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://www.nacion.com/resizer/v2/OCIK3GTS2ZFNDOPSSI6WP3REOQ.png?smart=true&auth=a15d112d8239367bba32c74d49122ff20cd1121ff4555ecd67603ba6e815af4e&width=1440&height=753" />
    </div>     
     <!-- Fila 7 -->
    <div class="news-block">
        <img class="news-image" src="https://prensa.com/resizer/v2/POWLAF6KYZCOJE2DSWXIUU6BPY.jpg?auth=0b49f6e0201eec0fefd958f09e51dba6ef4be7b587c97beb816cbbbe4af7782f&width=1200"/>
    </div>
    <div class="news-block news-text">  
        <div class="news-title">El Gobierno de Estados Unidos contempla llegar a acuerdos arancelarios regionales</div>
        <div class="news-date">Publicado el 18 de mayo de 2025</div>
        <div class="news-description">El secretario del Tesoro de Estados Unidos, Scott Bessent, señaló este domingo que su Gobierno contempla llegar a acuerdos arancelarios por regiones en la actual negociación</div>
        <a class="news-link" href="https://www.prensa.com/mundo/el-gobierno-de-estados-unidos-contempla-llegar-a-acuerdos-arancelarios-regionales/">Ver más →</a>
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
