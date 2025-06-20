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
        <img class="news-image" src="https://static01.nyt.com/images/2025/06/13/espanol/00Biz-New-China-Shock-02-wfvl-ES-copy1/00Biz-New-China-Shock-02-wfvl-jumbo.jpg?quality=75&auto=webp"/>
    </div>
    <div class="news-block news-text">
        <div class="news-title">China desata una nueva avalancha de exportaciones que está reconfigurando al mundo</div>
        <div class="news-date">Publicado el 17 de junio de 2025</div>
        <div class="news-description">A medida que los aranceles del presidente Trump cierran el mercado estadounidense, los productos chinos inundan países desde el Sudeste Asiático hasta Europa y Latinoamérica.</div>
        <a class="news-link" href="https://www.nytimes.com/es/2025/06/17/espanol/negocios/exportaciones-chinas-aranceles.html">Ver más →</a>
        </div>   
    <!-- Fila 2 -->
    <div class="news-block news-text">
        <div class="news-title">Trump y Starmer acuerdan implementar partes del acuerdo comercial sobre automóviles, acero y aviones</div>
        <div class="news-date">Publicado el 16 de junio de 2025</div>
        <div class="news-description">Los líderes de Gran Bretaña y Estados Unidos anunciaron un acuerdo el mes pasado, pero no estaba claro cuándo entraría en vigor. Gran Bretaña celebró el anuncio como "una gran victoria".</div>
        <a class="news-link" href="https://www.nytimes.com/2025/06/16/us/uk-trade-trump-starmer-tariffs.html">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://static01.nyt.com/images/2025/05/09/multimedia/16trump-news-uk-trade1/16trump-news-uk-trade1-jumbo.jpg?quality=75&auto=webp"/>
        </div>
    <!-- Fila 3 -->
        <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1GM9l9.img?w=768&h=512&m=6"/>
    </div>
    <div class="news-block news-text">
        <div class="news-title">Los líderes del G7 se reúnen en Canadá para una cumbre ensombrecida por la crisis entre Israel e Irán y las guerras comerciales</div>
        <div class="news-date">Publicado el 15 de junio de 2025</div>
        <div class="news-description">Los líderes de algunas de las mayores potencias económicas del mundo llegaron el domingo a las Montañas Rocosas canadienses para una cumbre del Grupo de los Siete , ensombrecida por un creciente conflicto entre Israel e Irán y la guerra comercial no resuelta del presidente estadounidense Donald Trump.</div>
        <a class="news-link" href="https://www.msn.com/en-us/money/companies/g7-leaders-gather-in-canada-for-summit-overshadowed-by-middle-east-crisis-and-trump-s-tariffs/ar-AA1GJs5W">Ver más →</a>
        </div>   
    <!-- Fila 4 -->
    <div class="news-block news-text">
        <div class="news-title">Caída histórica en puertos de EE. UU.: Importaciones Chinas se desploman 28.5% en mayo por aranceles de Trump</div>
        <div class="news-date">Publicado el 12 de junio de 2025</div>
        <div class="news-description">En mayo, las importaciones en varios de los puertos más concurridos de Estados Unidos cayeron drásticamente. Este fenómeno se produjo en respuesta a la imposición temporal de aranceles del 145% por parte del presidente Donald Trump sobre numerosos productos provenientes de China.</div>
        <a class="news-link" href="https:/https://es-us.noticias.yahoo.com/ca%C3%ADda-hist%C3%B3rica-puertos-ee-uu-155018871.html">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://media.zenfs.com/es/el_tiempo_latino_378/1c5d2fd2db866326826cd44afddd3517??w=534&h=334&m=6"/>
        </div>
    <!-- Fila 5 -->
        <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1GvE6Z.img?w=768&h=432&m=6&x=130&y=115&s=770&d=328"/>
    </div>
    <div class="news-block news-text">
        <div class="news-title">Trump afirma que el acuerdo con China recoge que EEUU imponga aranceles del 55% y Pekín, del 10%</div>
        <div class="news-date">Publicado el 11 de junio de 2025</div>
        <div class="news-description">El presidente de EEUU da algunos detalles del acuerdo comercial alcanzado para desescalar las tensiones con China, que incluye también levantar restricciones para la matriculación de estudiantes chinos en EEUU</div>
        <a class="news-link" href="https://www.msn.com/es-es/noticias/internacional/trump-afirma-que-el-acuerdo-con-china-recoge-que-eeuu-imponga-aranceles-del-55-y-pek%C3%ADn-del-10/ar-AA1GvGyZ">Ver más →</a>
        </div>   
    <!-- Fila 6 -->
    <div class="news-block news-text">
        <div class="news-title">Latinoamérica se beneficiará de los cambios en el mercado estadounidense, aseguran inversores</div>
        <div class="news-date">Publicado el 09 de junio de 2025</div>
        <div class="news-description">Latinoamérica ha emergido como un importante destino de inversión en momentos en que las guerras en curso, tanto de tipo militar como comercial, hacen que los inversores busquen opciones en una región que consideran refrescantemente libre de aranceles y grandes conflictos.</div>
        <a class="news-link" href="https://www.msn.com/es-mx/dinero/econom%C3%ADa/latinoam%C3%A9rica-se-beneficiar%C3%A1-de-los-cambios-en-el-mercado-estadounidense-aseguran-inversores/ar-AA1Gov16">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1oaZFU.img?w=300&h=200&m=6"/>
    </div>    
    <!-- Fila 7 -->
        <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1GmdaE.img?w=768&h=512&m=6"/>
    </div>
    <div class="news-block news-text">
        <div class="news-title">Estados Unidos y China mantienen conversaciones comerciales en Londres tras la llamada telefónica entre Trump y Xi</div>
        <div class="news-date">Publicado el 8 de junio de 2025</div>
        <div class="news-description">Delegaciones de alto nivel de Estados Unidos y China se reunirán el lunes en Londres para intentar apuntalar una frágil tregua en una disputa comercial que ha sacudido la economía global.</div>
        <a class="news-link" href="https://www.msn.com/en-us/money/markets/us-and-china-hold-trade-talks-in-london-after-trump-xi-phone-call/ar-AA1Gm4ly">Ver más →</a>
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
