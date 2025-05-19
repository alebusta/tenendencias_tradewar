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
        <img class="news-image" src="https://prensa.com/resizer/v2/POWLAF6KYZCOJE2DSWXIUU6BPY.jpg?auth=0b49f6e0201eec0fefd958f09e51dba6ef4be7b587c97beb816cbbbe4af7782f&width=1200"/>
    </div>
    <div class="news-block news-text">  
        <div class="news-title">El Gobierno de Estados Unidos contempla llegar a acuerdos arancelarios regionales</div>
        <div class="news-date">Publicado el 18 de mayo de 2025</div>
        <div class="news-description">El secretario del Tesoro de Estados Unidos, Scott Bessent, señaló este domingo que su Gobierno contempla llegar a acuerdos arancelarios por regiones en la actual negociación</div>
        <a class="news-link" href="https://www.prensa.com/mundo/el-gobierno-de-estados-unidos-contempla-llegar-a-acuerdos-arancelarios-regionales/">Ver más →</a>
    </div>            
    <!-- Fila 2 -->
    <div class="news-block news-text">
        <div class="news-title">Ruta de la Seda “calentó” a Colombia con Estados Unidos: ¿qué esperar tras dura advertencia del gobierno Trump?</div>
        <div class="news-date">Publicado el 15 de mayo de 2025</div>
        <div class="news-description">Mientras Washington dijo que bloqueará a bancos multilaterales que financien proyectos chinos en el país, persiste el estancamiento en las negociaciones sobre el arancel del 10% para productos colombianos.</div>
        <a class="news-link" href="https://www.elcolombiano.com/negocios/estados-unidos-bloqueo-bancos-empresas-chinas-en-colombia-aranceles-EA27413227">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://estaticos.elcolombiano.com/binrepository/780x565/0c0/780d565/none/11101/TSCH/petro-trump-y-xian_47877334_20250515174621.jpg" />
    </div>     
     <!-- Fila 3 -->
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1EKMct.img?"/>
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Las empresas chinas ven la pausa arancelaria con cautela e incertidumbre</div>
        <div class="news-date">Publicado el 14 de mayo de 2025</div>
        <div class="news-description">Aunque el presidente estadounidense Donald Trump ha hablado de victoria tras alcanzar un acuerdo el fin de semana con China para reducir los altísimos aranceles impuestos a los productos de ambos países, las empresas en China están reaccionando al acuerdo temporal con cautela.</div>
        <a class="news-link" href="https://www.msn.com/en-us/money/markets/chinese-businesses-view-tariff-pause-with-caution-and-uncertainty/ar-AA1EKTcR">Ver más →</a>
    </div>            
    <!-- Fila 4 -->
    <div class="news-block news-text">
        <div class="news-title">China busca contrarrestar influencia de EE.UU. con alianza latinoamericana y línea de crédito de 9.200 millones de dólares</div>
        <div class="news-date">Publicado el 13 de mayo de 2025</div>
        <div class="news-description">China está tomando medidas para fortalecer sus alianzas con otros países como contrapeso a la guerra comercial del presidente Donald Trump, presentando un frente unido con los líderes latinoamericanos un día después de que China y Estados Unidos acordaron una tregua de 90 días en su estancamiento arancelario.</div>
        <a class="news-link" href="https://businessmirror.com.ph/2025/05/13/china-seeks-to-counter-us-influence-with-latin-american-alliance-and-9-2-billion-credit-line/">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://businessmirror.com.ph/wp-content/uploads/2025/05/world04-051425.jpg" />
    </div>     
     <!-- Fila 5 -->
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1EEa9m.img?"/>
    </div>
    <div class="news-block news-text">  
        <div class="news-title">China se acerca a Brasil y América Latina en medio de crisis por aranceles</div>
        <div class="news-date">Publicado el 12 de mayo de 2025</div>
        <div class="news-description">Lula da Silva está de visita en Beijing esta semana, y se espera un foro China-CELAC en el que habrá altos funcionarios de países como Colombia, Chile y México.</div>
        <a class="news-link" href="https://www.msn.com/es-cl/noticias/other/china-se-acerca-a-brasil-y-am%C3%A9rica-latina-en-medio-de-crisis-por-aranceles/ar-AA1EEeYh">Ver más →</a>
    </div>        
    <!-- Fila 6 -->
    <div class="news-block news-text">
        <div class="news-title">EE UU anuncia “progresos sustanciales” tras la primera reunión sobre aranceles con China desde el inicio de la guerra comercial</div>
        <div class="news-date">Publicado el 11 de mayo de 2025</div>
        <div class="news-description">El secretario del Tesoro califica de “productivo” el encuentro de dos días, celebrado en Ginebra, y aplaza al lunes los detalles sobre lo acordado</div>
        <a class="news-link" href="https://elpais.com/internacional/2025-05-11/ee-uu-califica-de-productivas-sus-primeras-conversaciones-arancelarias-con-china-desde-el-inicio-de-la-guerra-comercial.html">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://imagenes.elpais.com/resizer/v2/3Q4CCGTT3VNDBF33VMA5UB4U2M.jpg?auth=541b7af5b845bfdc04264b6c5130b7cd2f414d920b10a16714b79f1e0e59f55e&width=1200" />
    </div>     
    <!-- Fila 7 -->
    <div class="news-block">
        <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1Er3k7.img?"/>
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Trump anuncia acuerdo comercial “histórico” con Reino Unido: bajan aranceles y se eliminan barreras</div>
        <div class="news-date">Publicado el 08 de mayo de 2025</div>
        <div class="news-description">El presidente estadunidense, Donald Trump, anunció este jueves que, como parte del acuerdo comercial recién alcanzado con Reino Unido, Londres eliminará "numerosas barreras no arancelarias" que permitirán un mayor acceso al mercado británico de productos agrícolas y químicos estadunidenses.</div>
        <a class="news-link" href="https://www.msn.com/es-mx/pol%C3%ADtica/gobierno/trump-anuncia-acuerdo-comercial-hist%C3%B3rico-con-reino-unido-bajan-aranceles-y-se-eliminan-barreras/ar-AA1Er7TM">Ver más →</a>
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
