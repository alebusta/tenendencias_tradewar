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
    <!-- Fila 2 -->
    <div class="news-block">
        <img class="news-image" src="https://static01.nyt.com/images/2025/05/06/multimedia/06dc-trade-fpvc/06dc-trade-fpvc-jumbo.jpg?quality=75&auto=webp" />
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Funcionarios de Trump se reunirán con sus homólogos chinos en medio del estancamiento comercial</div>
        <div class="news-date">Publicado el 06 de mayo de 2025</div>
        <div class="news-description">Scott Bessent, secretario del Tesoro, y Jamieson Greer, representante comercial de Estados Unidos, discutirán asuntos comerciales y económicos con los funcionarios esta semana.</div>
        <a class="news-link" href="https://www.nytimes.com/2025/05/06/business/economy/us-china-trade-talks.html">Ver más →</a>
    </div>        
    <!-- Fila 1 -->
    <div class="news-block news-text">
        <div class="news-title">EEUU impondrá casi un 21% de aranceles a la mayoría de los tomates mexicanos</div>
        <div class="news-date">Publicado el 05 de mayo de 2025</div>
        <div class="news-description">El gobierno del presidente estadounidense Donald Trump anunció este lunes que impondrá tarifas aduaneras del 20,91% sobre la mayoría de las importaciones de tomates mexicanos</div>
        <a class="news-link" href="https://www.rfi.fr/es/m%C3%A1s-noticias/20250415-eeuu-impondr%C3%A1-casi-un-21-de-aranceles-a-la-mayor%C3%ADa-de-los-tomates-mexicanos">Ver más →</a>
        </div>   
    <div class="news-block">
        <img class="news-image" src="https://s.rfi.fr/media/display/043bf16e-19e6-11f0-b4cb-005056bf30b7/w:980/p:16x9/15248f8203b511812c4b2d6b3fcd5460be434102.webp" />
    </div>    
    <!-- Fila 2 -->
    <div class="news-block">
        <img class="news-image" src="https://static01.nyt.com/images/2025/05/05/multimedia/05int-elections-trump-02-pjhl/05int-elections-trump-02-pjhl-superJumbo.jpg?quality=75&auto=webp" />
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Una nueva tendencia en las elecciones mundiales: el impulso anti-Trump</div>
        <div class="news-date">Publicado el 04 de mayo de 2025</div>
        <div class="news-description">En las elecciones de Canadá y Australia, los partidos de derecha que imitaron el manual de MAGA fueron castigados. En otros países, el presidente Trump está teniendo un impacto más complejo.</div>
        <a class="news-link" href="https://www.nytimes.com/2025/05/04/world/canada/global-elections-trump.html">Ver más →</a>
    </div>        
    <!-- Fila 3 -->
    <div class="news-block news-text">
        <div class="news-title">Impactos arancelarios en el triángulo de la soya entre Estados Unidos, Brasil y China.</div>
        <div class="news-date">Publicado el 01 de mayo de 2025</div>
        <div class="news-description">China trasladó una parte importante de sus compras de soya a Brasil cuando comenzó la guerra comercial de 2018. ¿Qué podrían implicar nuevos aranceles?</div>
        <a class="news-link" href="https://www.agrinews-pubs.com/business/2025/05/01/tariff-impacts-on-us-brazil-china-soybean-triangle/">Ver más →</a>
        </div>
    <div class="news-block">
        <img class="news-image" src="https://www.agrinews-pubs.com/resizer/8kq6uvIHjjNU25p4d2i6ZKmLUf4=/800x0/filters:format(jpg):quality(70)/cloudfront-us-east-1.images.arcpublishing.com/shawmedia/WLBWZSEQ75HHHCVT2EHZTCK3RQ.jpg" />
    </div>
    <!-- Fila 4 -->
    <div class="news-block">
        <img class="news-image" src="https://images-tools.cadena3.com/tools/r/e64d9f61-9e44-4217-9809-1cfa0de9a93d.jpg?width=1200&height=646" />
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Trump promulga medida que reduce aranceles sobre autos ensamblados en Estados Unidos por dos años</div>
        <div class="news-date">Publicado el 30 de abril de 2025</div>
        <div class="news-description">El presidente Trump firmó un decreto que permitirá una disminución del 15% en los aranceles sobre vehículos ensamblados en Estados Unidos durante el primer año. Esta medida busca fomentar la producción local.</div>
        <a class="news-link" href="https://www.cadena3.com/noticia/internacionales/trump-promulga-medida-que-reduce-aranceles-sobre-autos-ensamblados-en-estados-unidos-por-dos-anos_418768">Ver más →</a>
    </div>    
    <!-- Fila 5 -->
    <div class="news-block news-text">
        <div class="news-title">Los primeros 100 días de Trump: el presidente de "Estados Unidos Primero" está trastocando el orden mundial</div>
        <div class="news-date">Publicado el 29 de abril de 2025</div>
        <div class="news-description">En los caóticos primeros 100 días desde que el presidente estadounidense Donald Trump regresó al poder, ha llevado a cabo una campaña a menudo impredecible que ha alterado partes del orden mundial basado en reglas que Estados Unidos ayudó a construir.</div>
        <a class="news-link" href="https://www.rte.ie/news/world/2025/0429/1510018-trump-100-days/">Ver más →</a>
        </div>
    <div class="news-block">
        <img class="news-image" src="https://img.rasset.ie/00226317-800.jpg" />
    https://img.rasset.ie/00226317-800.jpg
    </div>
    <!-- Fila 6 -->
    <div class="news-block">
        <img class="news-image" src="https://imagenes.elpais.com/resizer/v2/KYM6WPM7E2SWYLJQN655ERPBXE.jpg?auth=407f003f1762af940440d383c4b2d5ee868345e0e3d71c10959635bb0b12c772&width=1200" />
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Los BRICS debaten en Brasil su respuesta a la guerra arancelaria declarada por Trump</div>
        <div class="news-date">Publicado el 28 de abril de 2025</div>
        <div class="news-description">El canciller Vieira, el anfitrión, insta al bloque del sur global a centrarse en la defensa del multilateralismo sin ser “un bloque de enfrentamiento”.</div>
        <a class="news-link" href="https://elpais.com/america/2025-04-28/los-brics-debaten-en-brasil-su-respuesta-a-la-guerra-arancelaria-declarada-por-trump.html">Ver más →</a>
    </div>    
    <!-- Fila 7 -->
    <div class="news-block news-text">
        <div class="news-title">Aranceles, aunque bajos tienden a ser más nocivos para la región</div>
        <div class="news-date">Publicado el 27 de abril de 2025</div>
        <div class="news-description">El FMI advierte que una desaceleración del crecimiento mundial podría afectar a la demanda de productos básicos.</div>
        <a class="news-link" href="https://www.expreso.ec/actualidad/economia/aranceles-bajos-tienden-nocivos-region-240508.html">Ver más →</a>
        </div>
    <div class="news-block">
        <img class="news-image" src="https://imagenes.expreso.ec/files/image_780_477/uploads/2025/04/27/680eba744a9fe.jpeg" />
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
st.markdown('<p class="small-text" text-center="right">©2025 Cepal Lab - versión demo v0.1.0</p>', unsafe_allow_html=True)
