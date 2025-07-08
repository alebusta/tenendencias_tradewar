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
    <div class="news-block news-text">
        <div class="news-title">Presidente Donald Trump amenazó a 14 países con nuevos aranceles de hasta 40%</div>
        <div class="news-date">Publicado el 8 de julio de 2025</div>
        <div class="news-description">Trump anunció nuevos aranceles de hasta 40% para 12 países, entre ellos Japón, Corea del Sur, Sudáfrica y varios miembros del sudeste asiático.</div>
        <a class="news-link" href="https://www.msn.com/es-co/noticias/other/presidente-donald-trump-amenaz%C3%B3-a-14-pa%C3%ADses-con-nuevos-aranceles-de-hasta-40/ar-AA1IacUS">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1IafdA.img?w=650&h=400&m=2"/>
        </div>    
    <!-- Fila 2 -->
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1I2aFe.img?w=768&h=432&m=6"/>
    </div>
    <div class="news-block news-text">
        <div class="news-title">Guerra comercial escalada: BRICS y otros países rechazan ultimátum de aranceles de Trump</div>
        <div class="news-date">Publicado el 6 de julio de 2025</div>
        <div class="news-description">El influyente grupo intergubernamental BRICS, que reúne a Brasil, India, Rusia, China, Sudáfrica y otros cinco países miembros, se prepara para emitir una declaración formal que critique la actual situación arancelaria de Estados Unidos.</div>
        <a class="news-link" href="https://www.msn.com/es-mx/pol%C3%ADtica/relaciones-internacionales/guerra-comercial-escalada-brics-y-otros-pa%C3%ADses-rechazan-ultim%C3%A1tum-de-aranceles-de-trump/ar-AA1I2k9U">Ver más →</a>
        </div>
   <!-- Fila 3 -->
    <div class="news-block news-text">
        <div class="news-title">México logra pequeños avances en negociaciones con Estados Unidos ante la avalancha de ataques de Trump</div>
        <div class="news-date">Publicado el 2 de julio de 2025</div>
        <div class="news-description">La reapertura a la exportación de ganado o el impuesto del 1% a las remesas son acuerdos concretos, pero la relación bilateral no acaba de encontrar cauces.</div>
        <a class="news-link" href="https://elpais.com/mexico/2025-07-02/mexico-logra-pequenos-avances-en-negociaciones-con-estados-unidos-ante-la-avalancha-de-ataques-de-trump.html">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://imagenes.elpais.com/resizer/v2/EQ3R4AULWSQTVRXZM5FTU3MILE.jpg?auth=19b34b484a703038a929f87314b2de3f9533b447d195812c33ee2e8a986ffebe&width=1200"/>
        </div>
    <!-- Fila 4 -->
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1HEi9k.img?w=768&h=512&m=6&x=262&y=136&s=142&d=142"/>
    </div>
    <div class="news-block news-text">
        <div class="news-title">Trump asegura que no planea extender suspensión de aranceles globales más allá del 9 de julio</div>
        <div class="news-date">Publicado el 29 de junio de 2025</div>
        <div class="news-description">El presidente Donald Trump asegura que no tiene planeado extender una pausa de 90 días a la entrada en vigor de aranceles sobre la mayoría de las naciones más allá del 9 de julio.</div>
        <a class="news-link" href="https://www.msn.com/es-mx/noticias/mundo/trump-asegura-que-no-planea-extender-suspensi%C3%B3n-de-aranceles-globales-m%C3%A1s-all%C3%A1-del-9-de-julio/ar-AA1HExAm">Ver más →</a>
        </div>
   <!-- Fila 5 -->
    <div class="news-block news-text">
        <div class="news-title">Francia recrudece su presión contra el acuerdo UE-Mercosur ante etapa clave</div>
        <div class="news-date">Publicado el 26 de junio de 2025</div>
        <div class="news-description">Francia redobla sus esfuerzos con otros países europeos para intentar bloquear o modificar el acuerdo comercial con el Mercosur, cuando la Comisión Europea se dispone a lanzar.</div>
        <a class="news-link" href="https://www.lanacion.com.ar/agencias/francia-recrudece-su-presion-contra-el-acuerdo-ue-mercosur-ante-etapa-clave-nid26062025/">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://www.lanacion.com.ar/resizer/v2/francia-recrudece-su-presion-contra-el-acuerdo-ue-C4DZYPM2UNGU3DALOAAO6LNTWQ.jpg?auth=fc6b28e5e2300c522eaa917feedb078c9006c0037eab4e0b768a17e3c8c5f5e8&width=880&height=586&quality=70&smart=true"/>
        </div>
    <!-- Fila 6 -->
        <div class="news-block">
        <img class="news-image" src="https://i0.wp.com/efe.com/wp-content/uploads/2025/06/Acero_Fabrica.webp?w=900&ssl=1"/>
    </div>
    <div class="news-block news-text">
        <div class="news-title">México y EEUU, a punto de cerrar un acuerdo sobre los aranceles al acero y aluminio impuestos por Trump</div>
        <div class="news-date">Publicado el 24 de junio de 2025</div>
        <div class="news-description">Marcelo Ebrard confirma que las negociaciones con Washington están en su fase final, tras el aumento de aranceles al 50% decretado por el Gobierno de EEUU a inicios de junio.</div>
        <a class="news-link" href="https://americaeconomica.com/wp-content/uploads/2025/02/Designer-1-1-1024x585.jpeg">Ver más →</a>
        </div>   
   <!-- Fila 7 -->
    <div class="news-block news-text">
        <div class="news-title">Estrecho de Ormuz: EE. UU. insta a China a impedir que Irán bloquee una ruta marítima crucial</div>
        <div class="news-date">Publicado el 22 de junio de 2025</div>
        <div class="news-description">Los analistas han dicho que Irán podría optar por tomar represalias al ataque de Washington del domingo por la mañana cerrando el Estrecho, una vía fluvial por la que pasa una quinta parte de la producción mundial de petróleo.</div>
        <a class="news-link" href="https://www.forbesindia.com/article/news/strait-of-hormuz-us-urges-china-to-stop-iran-from-blocking-critical-shipping-lane/96255/1">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://images.forbesindia.com/media/images/2025/Jun/img_246275_irancapitaleconomy.jpg"/>
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
