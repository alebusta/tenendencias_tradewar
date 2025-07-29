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
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1Ji4JX.img?w=768&h=432&m=6&x=118&y=223&s=866&d=96"/>
        </div> 
    <div class="news-block news-text">
        <div class="news-title">Trump y la UE logran acuerdo arancelario; incluye tarifa del 15% a productos europeos</div>
        <div class="news-date">Publicado el 27 de julio de 2025</div>
        <div class="news-description">Trump dijo que EE.UU. y la UE acordaron un arancel del 15% a productos de la UE y compras significativas de energía y equipo militar de EE.UU.</div>
        <a class="news-link" href="https://www.msn.com/es-mx/noticias/mundo/trump-y-la-ue-logran-acuerdo-arancelario-incluye-tarifa-del-15-a-productos-europeos/ar-AA1JofjO">Ver más →</a>
        </div>      
  <!-- Fila 2 -->
    <div class="news-block news-text">
        <div class="news-title">Sheinbaum y Lula acuerdan ampliar relación comercial ante aranceles de Trump</div>
        <div class="news-date">Publicado el 24 de julio de 2025</div>
        <div class="news-description">La presidenta mexicana y el mandatario brasileño acordaron la visita a México de una delegación de empresarios y ministros de Brasil encabezada por el vicepresidente Geraldo Alckmin, el 27 y el 28 de julio.</div>
        <a class="news-link" href="https://www.msn.com/es-mx/noticias/mundo/sheinbaum-y-lula-acuerdan-ampliar-relaci%C3%B3n-comercial-ante-aranceles-de-trump/ar-AA1Jb3ft">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://editorial.aristeguinoticias.com/wp-content/uploads/2025/07/sheinbaum-lula-profundizar-relacion-comercial-aranceles-trump-2-23072025.jpg"/>
        </div>    
  <!-- Fila 3 -->
      <div class="news-block">
        <img class="news-image" src="https://uscdn.eltribuno.com/072025/1753065946394.webp?cw=1155&ch=650&extw=jpg"/>
        </div> 
    <div class="news-block news-text">
        <div class="news-title">Argentina y EEUU van por un acuerdo</div>
        <div class="news-date">Publicado el 20 de julio de 2025</div>
        <div class="news-description">Mientras el presidente Donald Trump avanza con sus amenazas tarifarias a socios comerciales a partir del 1° de agosto, los gobiernos de la Argentina y Estados Unidos ya trabajan en una comunicación conjunta para anunciar el nuevo acuerdo arancelario entre los dos países.</div>
        <a class="news-link" href="https://www.eltribuno.com/nacionales/2025-7-20-23-45-0-argentina-y-eeuu-van-por-un-acuerdo">Ver más →</a>
        </div>      
  <!-- Fila 4 -->
    <div class="news-block news-text">
        <div class="news-title">Trump exige más concesiones mientras la UE posterga las contramedidas arancelarias estadounidenses</div>
        <div class="news-date">Publicado el 13 de julio de 2025</div>
        <div class="news-description">La Unión Europea dijo el domingo que extenderá su suspensión de contramedidas a los aranceles estadounidenses hasta principios de agosto y continuará presionando para un acuerdo negociado, mientras el gobierno del presidente estadounidense Donald Trump exige más concesiones de sus socios comerciales.</div>
        <a class="news-link" href="https://www.msn.com/en-gb/news/world/trump-demands-more-concessions-as-eu-holds-off-on-us-tariff-countermeasures/ar-AA1IwGs7">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1Iw2m3.img?w=768&h=511&m=6&x=258&y=200&s=235&d=235"/>
        </div>    
    <!-- Fila 5 -->
    <div class="news-block">
        <img class="news-image" src="https://imagenes.elpais.com/resizer/v2/https%3A%2F%2Fvdmedia.elpais.com%2Felpaistop%2F20257%2F10%2F1752109347_still.jpg?auth=7c953f2247295d4fd31f1a7fc92c0b8ddda6699aa6f2dc5973e5e18f1f94c0d0&width=1200&height=675&smart=true"/>
    </div>
    <div class="news-block news-text">
        <div class="news-title">Brasil responde con aranceles recíprocos al alza de aranceles de Trump por el juicio a Bolsonaro</div>
        <div class="news-date">Publicado el 10 de julio de 2025</div>
        <div class="news-description">Estados Unidos impuso al país un impuesto del 50%, más que cualquier otra nación, mientras el presidente republicano califica el juicio del exlíder como una "caza de brujas".</div>
        <a class="news-link" href="https://english.elpais.com/economy-and-business/2025-07-10/brazil-responds-with-reciprocal-tariffs-to-trumps-tariff-hike-over-bolsonaro-trial.html">Ver más →</a>
        </div>
   <!-- Fila 6 -->
    <div class="news-block news-text">
        <div class="news-title">Trump promete aranceles del 50% contra Brasil, alegando una "caza de brujas" contra Bolsonaro</div>
        <div class="news-date">Publicado el 9 de julio de 2025</div>
        <div class="news-description">Las tensiones entre Estados Unidos y Brasil han estallado repentinamente. En respuesta a las críticas del presidente Trump, el presidente brasileño declaró: «No queremos un emperador».</div>
        <a class="news-link" href="https://www.nytimes.com/2025/07/09/world/americas/brazil-trump-bolsonaro-lula-coup-tariff.html">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://static01.nyt.com/images/2025/07/09/multimedia/09int-brazil-trump-qthb/09int-brazil-trump-qthb-superJumbo.jpg?quality=75&auto=webp"
            style="width: 100%; height: 100%; object-fit: contain;"/>
        </div>    
    <!-- Fila 7 -->
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1Ie8D5.img?w=768&h=405&m=6&x=852&y=111&s=152&d=152"/>
    </div>
    <div class="news-block news-text">
        <div class="news-title">Llegó el día: Trump anuncia arancel al cobre y en Chile el sector minero llama a la prudencia</div>
        <div class="news-date">Publicado el 8 de julio de 2025</div>
        <div class="news-description">En abril el escenario mundial era de incertidumbre, cuando el presidente de los Estados Unidos, Donald Trump, salió a exponer acompañado de una icónica tabla en donde anunciaba aranceles generales a una lista de más de 100 países, entre los que destacaba Chile casi al final, con un arancel del 10%.</div>
        <a class="news-link" href="https://www.msn.com/es-cl/noticias/otras/lleg%C3%B3-el-d%C3%ADa-trump-anuncia-arancel-al-cobre-y-en-chile-el-sector-minero-llama-a-la-prudencia/ar-AA1Ie1XI">Ver más →</a>
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
