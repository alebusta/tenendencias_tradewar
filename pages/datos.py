import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
import base64


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

# Cargar CSS desde un archivo externo
with open("style.css", "r") as f:
    css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


if st.button("Ir a Inicio"):
    st.switch_page("app.py")

# Título y descripción con estilo The Economist
st.markdown("<h1 style='font-family: Georgia; font-weight: bold; margin-bottom: 5px'>La Guerra Comercial en Datos</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Georgia; font-style: italic; margin-bottom: 25px'>Datos relevantes de interés extraídos de la base de noticias</p>", unsafe_allow_html=True)
st.markdown('---')

# Contenido de la aplicación

# Cargar la imagen como base64 para incrustarla directamente
with open("assets/cars-exports.jpg", "rb") as f:
    data = f.read()
    imagen = base64.b64encode(data).decode()



# Fila 1 (ahora también usando st.columns)
col1, col2 = st.columns(2)

with col2:
    # Datos de aranceles para países de Latinoamérica y el Caribe de la lista original
    # Datos de aranceles para países de Latinoamérica y el Caribe de la lista original
    data = {
        "PAÍS": [
            "ARGENTINA", "BRASIL", "BOLIVIA", "CHILE", "COLOMBIA", "COSTA RICA", 
            "REPÚBLICA DOMINICANA", "ECUADOR", "EL SALVADOR", "GUATEMALA", 
            "HONDURAS", "NICARAGUA", "PERÚ", "PANAMÁ", "TRINIDAD Y TOBAGO", "URUGUAY", "VENEZUELA"
        ],
        "TARIFA ESTIMADA CONTRA EE.UU. (%)": [
            10, 10, 20, 10, 10, 17, 
            10, 12, 10, 10, 
            10, 36, 10, 10, 12, 10, 29
        ],
        "TARIFA RECÍPROCA DE EE.UU. (%)": [
            10, 10, 10, 10, 10, 10, 
            10, 10, 10, 10, 
            10, 18, 10, 10, 10, 10, 15
        ]
    }

    # Creación del dataframe
    df = pd.DataFrame(data)

    # Usando método de Streamlit para estilizar la tabla

    # Agregar CSS personalizado
    st.markdown("""
    <style>
        .stDataFrame {
            font-family: 'Helvetica Neue', Arial, sans-serif;
        }
        .stDataFrame thead tr th {
            background-color: #1A476F !important;
            color: white !important;
        }
        .stDataFrame tbody tr:nth-child(even) {
            background-color: #f5f5f5;
        }
    </style>
    """, unsafe_allow_html=True)

    # Mostrar la tabla
    st.dataframe(
        df, 
        use_container_width=True,
        hide_index=True,
        column_config={
            "PAÍS": st.column_config.TextColumn(
                "PAÍS",
                width="medium"
            ),
            "TARIFA ESTIMADA CONTRA EE.UU. (%)": st.column_config.NumberColumn(
                "TARIFA ESTIMADA CONTRA EE.UU. (%)",
                format="%d%%",
                width="medium"
            ),
            "TARIFA RECÍPROCA DE EE.UU. (%)": st.column_config.NumberColumn(
                "TARIFA RECÍPROCA DE EE.UU. (%)",
                format="%d%%",
                width="medium"
            )
        }
    )

st.markdown("---")
# Fila 2 (ahora también usando st.columns)
col3, col4 = st.columns(2)
with col1:
    st.markdown("""
    <div class="news-text">
        <div class="news-title">Guerra comercial en Datos: Países de la región afectados por aranceles recíprocos</div>
        <div class="news-description">Aranceles anunciados el 2 de abril. La Casa Blanca informó más tarde que para México y Canadá, las órdenes ejecutivas anteriores siguen vigentes, lo que significa que los productos incluidos en el tratado de libre comercio "seguirá sujetos a un arancel del 0%, los que no lo cumplen, a un arancel del 25%, y los productos de energía y potasa que no lo cumplen, a un arancel del 10%".</div>
        <a class="news-link" href="https://www.elobservador.com.uy/estados-unidos/bbc-news-mundo/que-aranceles-les-ha-impuesto-trump-los-paises-america-latina-y-que-no-incluyen-mexico-n5992631">Ver más →</a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    data = {
        "Country": [
            "México", "Eslovaquia", "S.Corea", "Canadá", "Japón", "Hungría",
            "Suecia", "Alemania", "Austria", "S. África", "Reino Unido", "Brasil", "China", "India", "Rusia"
        ],
        "Automobiles": [5.5, 5.0, 2.3, 1.8, 1.3, 1.1, 0.9, 0.7, 0.5, 0.3, 0.2, 0.1, 0.05, 0.03, 0.02],
        "Parts":       [6.0, 5.3, 2.6, 2.0, 1.5, 1.3, 1.1, 0.9, 0.7, 0.4, 0.3, 0.2, 0.1, 0.05, 0.03]
    }

    df = pd.DataFrame(data)

    # Crear gráfico
    fig2 = go.Figure(data=[
        go.Bar(name='Automóviles', x=df["Country"], y=df["Automobiles"], marker_color='blue'),
        go.Bar(name='Autopartes', x=df["Country"], y=df["Parts"], marker_color='mediumturquoise')
    ])

    # Línea divisoria entre Top 10 y el resto
    fig2.add_shape(
        type="line",
        x0=9.5, x1=9.5, y0=0, y1=7,
        line=dict(color="black", width=2, dash="dash")
    )

    # Anotaciones
    fig2.add_annotation(x=4.5, y=6.8, text="Top 10 más expuestos", showarrow=False, font=dict(size=12))
    fig2.add_annotation(x=12.5, y=6.8, text="Otros", showarrow=False, font=dict(size=12))

    # Layout
    fig2.update_layout(
        title="Exportaciones de automóviles y respuestos como % de su respectivo PIB (2024)",
        barmode='group',
        yaxis_title="% del PIB",
        xaxis_tickangle=-45,
        height=500
    )

    st.plotly_chart(fig2, use_container_width=True)
    # Nota de fuente
    st.markdown("<p style='font-size: 0.9rem; color: gray;'>Adaptado de Capital Economics</p>", unsafe_allow_html=True)

    #st.image("https://images.unsplash.com/5/unsplash-kitsune-4.jpg?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max", use_column_width=True)

with col4:
    st.markdown("""
    <div class="news-text">
        <div class="news-title">Guerra comercial en Datos: Países más afectados por aranceles a los automóviles</div>
        <div class="news-description">De acuerdo a Capital Economics, México, Eslovaquia y Corea del Sur tienen la más alta exposició a estos aranceles, con hasta el 1,6% de su PIB en juego.</div>
        <a class="news-link" href="https://www.independent.co.uk/politics/trump-motor-car-auto-tariff-impact-world-global-b2723371.html">Ver más →</a>
    </div>
    """, unsafe_allow_html=True)



st.markdown("</div>", unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown("""

""")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown('<p class="small-text">Reporte preparado por CEPAL Lab para el Trade Emergency Team</p>', unsafe_allow_html=True)
with col2:
    st.markdown('<p class="small-text">Datos actualizados al 3 de abril de 2025</p>', unsafe_allow_html=True)
with col3:
    st.markdown('<p class="small-text">© Cepal Lab - Versión de prueba </p>', unsafe_allow_html=True)
