import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
import base64
import json


# Configuración de página
st.set_page_config(
    page_title="Monitor EEUU-LATAM | CEPAL Lab",
    page_icon="🌎",
    layout="centered", # o 'wide'
    initial_sidebar_state="collapsed"
)

# Ocultar la sidebar con CSS


# Botón de impresión
#st.markdown("""
#    <div style="text-align: right;">
#        <button onclick="window.print()" style="padding: 6px 12px; font-size: 16px; cursor: pointer;">
#            🖨️ Imprimir
#        </button>
#    </div>
#""", unsafe_allow_html=True)


# Cargar CSS desde un archivo externo
with open("../style.css", "r") as f:
    css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)



# Encabezado
# CSS personalizado para el encabezado
st.markdown("""

<div class="header_short">
        <h1 class="header_short-title">Resumen del período</h1>
        <p class="header_short-subtitle">Síntesis de los principales hechos de la semana. Resumen al 3 de abril de 2025.</p>
</div>


""", unsafe_allow_html=True)

st.markdown("""

<div class="trending-bar">
        <div class="trending-title"><a href="https://tradewar-monitor.streamlit.app/" target="_blank"> < Volver al inicio  </a></div>
        
</div>
""", unsafe_allow_html=True)

# Contenido de la aplicación


st.markdown("""
<div class="news-text">
    <div class="div-news-description">
            
# Tensiones comerciales y repercusiones regionales: implicancias del nuevo proteccionismo estadounidense

</div>
    <div class="div-news-description">

## Diagnóstico

El principal hecho noticioso de la semana es el anuncio del expresidente Donald Trump sobre la imposición de aranceles recíprocos a una amplia gama de países, incluyendo a varios de América Latina. Esta decisión, que Trump denominó el "Día de la Liberación", busca, según sus palabras, equilibrar la balanza comercial de Estados Unidos y proteger a los trabajadores y empresas estadounidenses. La medida ha generado reacciones mixtas a nivel global, con preocupación por las posibles consecuencias económicas y comerciales, así como por el impacto en las relaciones bilaterales.

## Tendencias

1.  **Aranceles Recíprocos como Herramienta Central:** La tendencia más marcada es el uso de aranceles como herramienta principal de la política comercial estadounidense bajo una posible administración Trump. El anuncio inicial del 2 de abril se materializó en una orden ejecutiva, demostrando la intención de implementar estas medidas de manera efectiva. La repetición constante de la noticia en diversos medios, con análisis de los países afectados y las reacciones que generaron, subraya la importancia de esta tendencia.

2.  **Impacto Diferenciado en América Latina:** Si bien la mayoría de los países latinoamericanos enfrentan un arancel base del 10%, la administración Trump ha diferenciado las tarifas para algunos países, como Venezuela (15%) y Nicaragua (18%). Esta diferenciación, junto con la exclusión de México y Canadá (aunque con otras restricciones comerciales), sugiere un enfoque selectivo que podría estar influenciado por factores políticos y de seguridad, además de los puramente comerciales.

3.  **Reacciones Globales y Posibles Contramedidas:** La imposición de aranceles ha provocado reacciones de cautela y preocupación en varios países. Brasil, por ejemplo, ha expresado su intención de responder con reciprocidad, y Canadá ha advertido que tomará contramedidas. La Unión Europea también ha manifestado su intención de actuar. Esto indica una posible escalada de tensiones comerciales y la posibilidad de una guerra comercial global.

## Implicaciones estratégicas

* **Para la Región:**
    * **Corto Plazo:** Aumento de costos para las exportaciones latinoamericanas a Estados Unidos, lo que podría afectar la competitividad de las empresas y reducir el volumen de comercio. Posibles tensiones diplomáticas con Estados Unidos.
    * **Mediano Plazo:** Necesidad de diversificar mercados de exportación para reducir la dependencia de Estados Unidos. Exploración de acuerdos comerciales con otros bloques económicos. Posible reconfiguración de las cadenas de suministro.
    * **Largo Plazo:** Potencial debilitamiento de la integración económica regional si los países se ven obligados a priorizar acuerdos bilaterales con Estados Unidos. Impacto en el crecimiento económico y el desarrollo de los países de la región.

* **Para Estados Unidos:**
    * **Corto Plazo:** Posible aumento de precios para los consumidores estadounidenses debido a los aranceles. Riesgo de represalias comerciales por parte de otros países.
    * **Mediano Plazo:** Potencial relocalización de industrias en Estados Unidos, lo que podría generar empleos. Posible impacto en las relaciones con aliados comerciales.
    * **Largo Plazo:** Posible reconfiguración del comercio global y del papel de Estados Unidos en la economía mundial.

## Factores clave a vigilar

* **La evolución de las relaciones comerciales bilaterales:** Es crucial monitorear cómo los países latinoamericanos afectados por los aranceles negocian con Estados Unidos y si logran obtener exenciones o acuerdos que mitiguen el impacto.
* **Las posibles contramedidas:** Es importante seguir de cerca las acciones que tomen los países afectados, así como la respuesta de Estados Unidos. Una escalada de represalias podría tener consecuencias negativas para la economía global.
* **El impacto en sectores específicos:** Es necesario analizar el impacto de los aranceles en sectores clave de la economía latinoamericana, como la agricultura, la manufactura y la energía.
* **La situación política en Estados Unidos:** El resultado de las elecciones presidenciales de 2024 y la postura del Congreso estadounidense serán determinantes para el futuro de la política comercial del país.
* **La reacción de las organizaciones internacionales:** Es importante observar la postura de la Organización Mundial del Comercio (OMC) y otras organizaciones internacionales ante las medidas proteccionistas de Estados Unidos.
--- 
## Datos relevantes de la guerra comercial

### *Ámbito global*

- **10%**: Impuesto base sobre las importaciones de todos los países impuesto por Estados Unidos.  
- **Tarifas más altas**: Aplicadas a docenas de naciones que tienen superávit comercial con Estados Unidos. Sesenta países y la UE enfrentan impuestos aún más altos que el 10% base.  
- **26%**: Arancel aplicado a las exportaciones de India a Estados Unidos.  
- **25%**: Arancel sobre las importaciones de automóviles.  
- **34%**: Arancel adicional impuesto a China, sumado a los aranceles ya existentes desde enero.  
- **54%**: Aranceles totales que enfrentará China con la nueva orden de Trump (34% + aranceles previos).  
- **20%**: Nuevos aranceles contra la Unión Europea.  
- **67%**: Tasa total de barreras comerciales estimada para China por Estados Unidos, lo que justifica un arancel del 34% en respuesta.  
- **4,000**: Expositores de alrededor de 60 países en la feria de Hannover Messe, en medio de las tensiones arancelarias.  
- **1,595**: Empresas en el área metropolitana de Milwaukee que exportan a Canadá.  
- **7%**: Caída en las acciones de Apple en las operaciones fuera de horario debido a los aranceles.  
- **9 mil millones de dólares**: Industria del bourbon de Kentucky que podría verse afectada por los aranceles de la Unión Europea.  


### *Latinoamérica y el Caribe*

#### Aranceles en la región

- **10%**: Arancel mínimo global impuesto por Trump a numerosos países, incluyendo:  
  Argentina, Brasil, Bolivia, Colombia, Chile, Costa Rica, El Salvador, Ecuador, Guatemala, Panamá, Perú, República Dominicana.  
- **15%**: Arancel impuesto a Venezuela.  
- **18%**: Arancel impuesto a Nicaragua.  

#### Impactos potenciales en cifras

- **Argentina – US$ 6.500 millones**: Valor del universo de las exportaciones argentinas que se verán afectadas.  
- **Colombia – 30%**: Porcentaje de las exportaciones del país que se verían afectadas por los aranceles del 10%.  
- **México – 25%**: Tarifas que aún debe asumir sobre los envíos que no cumplen con el TMEC, así como impuestos sobre exportaciones automotrices, de acero y aluminio.  
- **México**: Es el principal importador de EE. UU. y envía más del 80% de sus exportaciones a ese país, valoradas en más de 500.000 millones de dólares anuales.  

</div>
""", unsafe_allow_html=True)



# Pie de página
st.markdown("---")
st.markdown("""
*Este reporte analiza las noticias de la semana centrándose en el impacto de las decisiones de la administración Trump en América Latina, el Caribe y el mundo. 
Se utiliza un enfoque basado en la frecuencia de las noticias y su potencial impacto, prestando atención a los últimos desenlaces como indicadores de tendencias futuras.
La clasificación de noticias, análisis y reportes automatizados asistidos por Inteligencia Artificial se encuentran en un proceso de desarrollo experimental en el cual
es fundamental la validación experta humana. Por lo tanto los resultados de los análisis deben tomarse con la debida cautela.*"

""")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown('<p class="small-text">Reporte preparado por CEPAL Lab para el Trade Emergency Team</p>', unsafe_allow_html=True)
with col2:
    st.markdown('<p class="small-text">Datos actualizados al 17 de marzo, 2025</p>', unsafe_allow_html=True)
with col3:
    st.markdown('<p class="small-text">© Cepal Lab - Versión de prueba </p>', unsafe_allow_html=True)
