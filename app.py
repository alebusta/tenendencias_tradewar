import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
import base64
from news_chatbot import news_chatbot_component
import json


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

# Encabezado
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

# Sección 1: Noticias destacadas
#https://static01.nyt.com/images/2025/05/06/multimedia/06dc-tariffs-qmbv/06dc-tariffs-qmbv-superJumbo.jpg?quality=75&auto=webp
st.markdown(f"""

    <div class="news-grid">
    <div class="news-block news-text">
            <div class="news-title">Trump suspende los aranceles recíprocos por 90 días, excepto los que afectan a China</div>
            <div class="news-date">Publicado el 10 de abril de 2025</div>
            <div class="news-description">Se mantienen aranceles base de 10%, se incrementa aranceles a China hasta 125%, Europa responde postponiendo los aranceles anunciados a EEUU.</div>
            <a class="news-link" href="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1CDrp0.img?w=768&h=514&m=6&x=568&y=126&s=137&d=137">Ver más →</a>
        </div>
        <div class="news-block">
            <img class="news-image" src="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1Czfv1.img?w=534&h=300&m=6" />
        </div>
    <!-- Fila 1 -->
    <div class="news-block">
        <img class="news-image" src="https://static01.nyt.com/images/2025/04/06/multimedia/06trump-news-tariffs1-pfjc/06trump-news-tariffs1-pfjc-jumbo.jpg?quality=75&auto=webp" />
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Trump dice que los aranceles se mantendrán hasta que desaparezca el déficit comercial</div>
        <div class="news-date">Publicado el 6 de abril de 2025</div>
        <div class="news-description">El presidente dijo que no revertirá rápidamente los fuertes aranceles impuestos la semana pasada, los cuales han generado resistencia y sacudido los mercados.</div>
        <a class="news-link" href="https://www.nytimes.com/2025/04/06/us/politics/trump-tariffs-aides-recession.html">Ver más →</a>
    </div>            
    <!-- Fila 2 -->
    <div class="news-block news-text">
        <div class="news-title">Las tensiones comerciales entre EE. UU. y China se intensifican con una nueva ronda de aranceles</div>
        <div class="news-date">Publicado el 5 de abril de 2025</div>
        <div class="news-description">China responde a los recientes aranceles de EE. UU. imponiendo un impuesto del 34% a las importaciones estadounidenses, aplicando nuevos controles a la exportación de minerales raros e iniciando una demanda ante la OMC. Las tensiones comerciales reflejan disputas anteriores</div>
        <a class="news-link" href="https://www.devdiscourse.com/article/business/3335504-us-china-trade-tensions-escalate-with-new-round-of-tariffs">Ver más →</a>
    </div>
    <div class="news-block">
        <img class="news-image" src="https://www.devdiscourse.com/remote.axd?https://devdiscourse.blob.core.windows.net/devnews/16_01_2024_15_39_34_3730227.jpg?width=920&format=webp" />
    </div>
    <!-- Fila 3 -->   
    <div class="news-block">
        <iframe width="100%" height="110%" src="https://www.youtube.com/embed/xlNun19KbVw?si=-0XklfEgp-Y0LwkN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
    <div class="news-block news-text">  
        <div class="news-title">Trump anuncia aranceles el 'Día de la Liberación' que afectarán a más de 150 países</div>
        <div class="news-date">Publicado el 2 de abril de 2025</div>
        <div class="news-description">Países enfrentarán un arancel de EE.UU. equivalente a la mitad de la tasa que ellos imponen a los productos estadounidenses, según lo determine la Casa Blanca, con un mínimo del 10%. Trump señaló que este cálculo incluye barreras comerciales no monetarias y la manipulación cambiaria.</div>
        <a class="news-link" href="#">Ver más →</a>
    </div>  
    <!-- Fila 4 -->
    <div class="news-block news-text">
        <div class="news-title">Así es como los países planean responder a los aranceles de Trump</div>
        <div class="news-date">Publicado el 2 de abril de 2025</div>
        <div class="news-description">Gobiernos de todo el mundo reaccionaron después de que las amplias medidas comerciales del presidente Trump afectaran a los principales socios comerciales de Estados Unidos con fuertes aranceles adicionales. Esto es lo que prometen hacer o no, según Reuters.</div>
        <a class="news-link" href="https://finance.yahoo.com/news/factbox-trump-tariffs-draw-global-024705290.html">Ver más →</a>
    </div>
    <div class="news-block">
        <img class="news-image" src="https://static01.nyt.com/images/2025/04/02/multimedia/02int-tariffs-diplo-lgchESP/02int-tariffs-diplo-lgch-mediumThreeByTwo440.jpg" />
    </div>
</div>
            
""", unsafe_allow_html=True)

# Sección 2: Mapa de impacto potencial en Latinoamérica
col1, col2 = st.columns(2)

with col2:
    st.markdown("""
    <div class="news-text">
        <div class="news-title">Repercusiones en los principales medios de la América Latina y El Caribe</div>
        <div class="news-description">Este mapa permite visualizar las repercusiones de los últimos eventos en los países de la región durante el período analizado.</div>
        <a class="news-link" href="/base" target="_self">Ver más →</a>
    </div>
    """, unsafe_allow_html=True)

with col1:
    # Datos  países traer de DataFrame
    paises_data = pd.DataFrame({
        'País': ['Antigua y Barbuda', 'Argentina', 'Bahamas', 'Barbados', 'Belice', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'Ecuador', 'El Salvador', 'Granada', 'Guatemala', 'Guyana', 'Haití', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'Dominican Republic', 'Surinam', 'Trinidad y Tobago', 'Uruguay', 'Venezuela'],
        'Menciones': [4, 40, 2, 4, 7, 14, 30, 26, 42, 6, 13, 2, 13, 11, 2, 16, 2, 6, 25, 1, 29, 5, 12, 8, 19, 22, 2, 2, 16, 23],
        #'Áreas Clave': [['desarrollo económico', 'economía', 'inclusión', 'integración regional', 'resiliencia'], ['gobierno', 'corrupción', 'sanciones', 'política', 'justicia'], ['gobierno', 'noticias de América Latina', 'política exterior', 'política internacional', 'relaciones diplomáticas'], ['Netflix', 'acuerdos comerciales', 'adquisiciones', 'cine', 'cooperación internacional'], ['cooperación internacional', 'desarrollo regional', 'economía', 'gobierno', 'gobierno migratorio'], ['música', 'política', 'economía', 'elecciones', 'gira musical'], ['gobierno', 'OEA', 'accidentes aéreos', 'desastres naturales', 'justicia'], ['migración', 'política migratoria', 'gobierno', 'inmigración', 'refugiados'], ['política', 'gobierno', 'diplomacia', 'elecciones', 'relaciones internacionales'], ['política migratoria', 'deportación', 'migración', 'inmigración', 'gobierno'], ['migración', 'seguridad fronteriza', 'tráfico de personas', 'conflicto comercial', 'corrupción'], ['economía', 'política migratoria', 'remesas', 'finanzas internacionales', 'migración'], ['economía', 'migración', 'aranceles', 'comercio internacional', 'moneda'], ['gobiernos autoritarios', 'libertad de prensa', 'medio ambiente', 'minería ilegal', 'periodismo'], ['relaciones internacionales', 'fútbol', 'política exterior', 'política internacional', 'comercio internacional'], ['política exterior', 'relaciones internacionales', 'conflicto internacional', 'guerra', 'historia'], ['aranceles', 'billetera digital', 'comercio internacional', 'criptomoneda', 'desastres naturales'], ['arte', 'autonomía', 'comunidad puertorriqueña', 'cultura', 'diáspora'], ['economía', 'espionaje', 'gobierno', 'inflación', 'moneda'], ['gobierno', 'organizaciones internacionales', 'OEA', 'deportación', 'política de la región'], ['Netflix', 'ataques cibernéticos', 'ciberataque', 'cine', 'confidencialidad'], ['petróleo', 'migración', 'gobierno', 'política migratoria', 'política energética']]
        })

    # Mapa interactivo de Latinoamérica
    
    impact_map = pd.DataFrame({
        'País': paises_data['País'],
        'Menciones': paises_data['Menciones'],
        #'Temas': paises_data['Áreas Clave']
    })

    fig = px.choropleth(
        impact_map,
        locations='País',
        locationmode='country names',
        color='Menciones',
        color_continuous_scale='Blues',
        height=700 if st.session_state.get('screen_width',0) > 800 else 400,
        #title='Mapa de impacto potencial en Latinoamérica',
        # Añadir hover_data para mejorar los popups
        hover_name='País',
        hover_data={'País': False, 'Menciones': True} #'Temas':True}
    )

    # Ajustar el mapa para mostrar Latinoamérica correctamente
    fig.update_geos(
        visible=False,  # Quita el fondo de océanos/tierra
        lataxis_range=[-60, 35],
        lonaxis_range=[-120, -30],
        showcoastlines=True,
        coastlinecolor="darkgray",
        showland=True,
        landcolor="lightgray",
        showcountries=True,
        countrycolor="darkgray",
        framewidth=0  # Elimina el borde alrededor del mapa
    )

    fig.update_layout(
        margin=dict(t=50, b=0, l=0, r=0),
        coloraxis_colorbar_title='Cantidad de<br>artículos',
        geo=dict(
            showframe=False,  # Elimina el marco
            projection_type='equirectangular'  # Proyección que funciona bien para mostrar países
        ),
        dragmode = False
    )

    st.plotly_chart(fig, use_container_width=True)

# Sección 3: Tabla de aranceles
col3, col4 = st.columns(2)

with col4:
    # Datos de aranceles para países de Latinoamérica y el Caribe de la lista original
    # Datos
    fechas = ['Feb 1', 'Feb 27', 'Abril 2', 'Abril 7']
    aumentos = [10, 10, 34, 50]

    # Colores similares a los del gráfico original
    colores = ['#7a0c0a', '#d22c1e', '#ef4c48', '#ffa2a2']

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

    # Configuración de diseño
    fig.update_layout(
        barmode='stack',
        title="Desglose del 104% de Aranceles a China",
        title_font=dict(size=22, family="Arial Black"),
        xaxis_title="Gráfico adaptado de Yahoo Finance 9 de abril de 2025",
        yaxis_title="Valor (%)",
        yaxis=dict(range=[0, 110], ticksuffix="%"),
        legend_title_text="Fecha de anuncio",
        height=500
    )

    # Mostrar en Streamlit
    st.plotly_chart(fig)


with col3:
    st.markdown("""
    <div class="news-text">
        <div class="news-title">Guerra comercial en Datos: Escalada de aranceles de EEUU a China</div>
        <div class="news-description">En un periodo de poco más de dos meses, Estados Unidos implementó un aumento acumulado del 104% en aranceles sobre importaciones chinas. Este incremento se dio en cuatro etapas: dos aumentos iniciales de 10% en febrero, seguidos por un alza significativa del 34% en abril 2 y un último salto del 50% apenas cinco días después. La secuencia y magnitud de estas medidas reflejan una escalada rápida en la política comercial, marcando un endurecimiento en la estrategia estadounidense hacia China y represalias de parte del gobierno chino.</div>
        <a class="news-link" href="https://www.elobservador.com.uy/estados-unidos/bbc-news-mundo/que-aranceles-les-ha-impuesto-trump-los-paises-america-latina-y-que-no-incluyen-mexico-n5992631">Ver más →</a>
    </div>
    """, unsafe_allow_html=True)



###### SECCIÓN 2: DETALLE DE IMPLICANCIAS ######


st.header("💬 Asistente IA")
st.write("Asistente conversacional basado en inteligencia artificial para hacer consultas a la base de datos de noticias")

with st.expander("Haz clic aquí para abrir"):
    with open('noticias_2025-04-09.json', 'r', encoding='utf-8') as file:
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
