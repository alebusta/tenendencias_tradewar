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
with open("style.css", "r") as f:
    css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


if st.button("Ir a Inicio"):
    st.switch_page("app.py")


# Contenido de la aplicación
st.markdown("""	
            
    <div class="news-text">
        <div class="div-news-description">
            
    # Tensiones comerciales y repercusiones regionales: 145% para China, 125% para EE.UU.: La incertidumbre se intensifica y sacude la economía mundial
    *Segunda semana de abril de 2025*
            
    ## Diagnóstico

    El principal hecho noticioso de la semana es la escalada en la guerra comercial liderada por la administración Trump, caracterizada por la imposición y posterior modificación de aranceles a nivel global, con un foco particular en China. Esta situación ha generado una gran incertidumbre en los mercados financieros, con fuertes caídas en las bolsas y fluctuaciones en los precios de materias primas como el petróleo.

    La evolución de este conflicto se puede observar en los siguientes puntos:

    *   **Anuncio inicial de aranceles:** Trump anuncia aranceles "recíprocos" a más de 180 países, con un mínimo del 10% y hasta 104% para China, luego de medidas retaliatorias del país asiático.
    *   **Reacciones globales:** La Unión Europea anuncia contramedidas pero mantiene una pausa en esta decisión, mientras que líderes de América Latina expresan preocupación y prometen unidad.
    *   **Países exentos y afectados:** Se genera confusión sobre qué países están exentos de los aranceles, con cambios y aclaraciones constantes por parte de la administración Trump. México y Canadá inicialmente exentos, luego incluidos.
    *   **Pausa temporal y aumento a China:** Trump anuncia una pausa de 90 días en los aranceles para la mayoría de los países, pero aumenta los aranceles a China hasta el 145%. China por su parte aumenta hasta
        el 125% a las importaciones de productos estadounidenses, y suma restricciones a inversiones de empresas de EE.UU. en su territorio.
    *   **Reacciones de los mercados:** Los mercados experimentan fuertes fluctuaciones, con caídas iniciales seguidas de repuntes tras el anuncio de la pausa, pero luego vuelven a caer ante la persistente incertidumbre.
    *   **Preocupación por la recesión:** Economistas y líderes empresariales advierten sobre el riesgo de una recesión global como consecuencia de la guerra comercial.
    *   **Búsqueda de alternativas:** Varios países hablan de fortalecer lazos comerciales con otras regiones, como Asia y la Unión Europea, para mitigar el impacto de los aranceles estadounidenses.
    *   **Reacción en Latinoamérica:** La CELAC se reúne para discutir la situación y buscar una postura común, aunque persisten divisiones internas sobre cómo responder a las políticas de Trump.

    ## Tendencias

    1.  **Fragmentación del comercio global:** La imposición de aranceles por parte de Estados Unidos está generando una fragmentación del comercio global, con países buscando acuerdos bilaterales y regionales en lugar de un sistema multilateral.
    2.  **Aumento de la incertidumbre:** La volatilidad en las políticas comerciales de la administración Trump está generando una gran incertidumbre para las empresas y los inversores, lo que dificulta la toma de decisiones a largo plazo.
    3.  **Desplazamiento del poder económico:** La guerra comercial está acelerando el desplazamiento del poder económico hacia China, que busca fortalecer sus lazos con otros países y promover su propio modelo de desarrollo.

    ## Implicaciones estratégicas
             
    *   **Para la región:**
        *   **Corto plazo:** Impacto negativo en las exportaciones de algunos países, especialmente aquellos que dependen del mercado estadounidense.
        *   **Mediano plazo:** Necesidad de diversificar mercados y fortalecer la integración regional para reducir la dependencia de Estados Unidos.
        *   **Largo plazo:** Oportunidad para construir un modelo de desarrollo más autónomo y sostenible, basado en la cooperación regional y la diversificación económica.
    *   **Para Estados Unidos:**
        *   **Corto plazo:** Posible aumento de la inflación y desaceleración del crecimiento económico.
        *   **Mediano plazo:** Riesgo de perder competitividad en el mercado global y de dañar sus relaciones con aliados tradicionales.
        *   **Largo plazo:** Aislamiento económico y pérdida de influencia en el sistema internacional.
    *   **Para el mundo:**
        *   **Corto plazo:** Mayor volatilidad en los mercados financieros y aumento del riesgo de recesión global.
        *   **Mediano plazo:** Reconfiguración de las cadenas de suministro y surgimiento de nuevos bloques comerciales.
        *   **Largo plazo:** Debilitamiento del sistema multilateral de comercio y aumento de la inestabilidad geopolítica.

    ## Factores clave a vigilar

    *   La evolución de las negociaciones comerciales entre Estados Unidos y China.
    *   La respuesta de la Unión Europea y otros socios comerciales a las políticas de Trump.
    *   La capacidad de los países de América Latina y El Caribe para coordinar una respuesta conjunta.
    *   El impacto de la guerra comercial en el crecimiento económico global y en los precios de las materias primas.
    *   La evolución de la situación política en Estados Unidos y la posibilidad de un cambio de gobierno en las próximas elecciones.
            
    ---
     ## Datos relevantes de la guerra comercial

    ### *Ámbito global*
    La economía global se ve impactada por la guerra comercial entre EEUU y China, con aranceles que alcanzan el 145% para productos chinos y el 125% para productos estadounidenses. Esta situación genera volatilidad en los mercados, con el S&P 500 experimentando fuertes fluctuaciones y el Dow Jones Industrial Average mostrando un comportamiento similar. El rendimiento del bono del Tesoro a 10 años ha subido a su nivel más alto desde febrero, situándose alrededor del 4.5%, mientras que el oro ha superado los USD 3.200 por onza. Organismos como la Reserva Federal están preparados para estabilizar el mercado si es necesario, aunque se anticipa que los aranceles de Trump arrastrarán el crecimiento del PIB por debajo del 1% y elevarán la inflación hasta el 4%.         
    
    ### *Latinoamérica y el Caribe*
        
    *   **47%** de las exportaciones de Costa Rica destinadas a Estados Unidos, por un valor de USD 9.411,9 millones (2024).
    *   **USD 271 millones** es el valor de los 263 productos exportados por Bolivia a EEUU (2024).
    *   **30%** de las exportaciones de Colombia tienen como destino el mercado de EEUU (2024).
    *   **70%** de las exportaciones peruanas se ven afectadas por aranceles de EEUU.
            </div>

 """, unsafe_allow_html=True)

st.markdown("""---""")	
st.header("Resúmenes anteriores")    

with st.expander("Primera semana de abril de 2025", expanded=False):
    st.markdown("""
    <div class="news-text">
        <div class="div-news-description">
                
    # Tensiones comerciales y repercusiones regionales: implicancias del nuevo proteccionismo estadounidense
    *Primera semana de abril de 2025*

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
es fundamental la validación experta humana. Por lo tanto los resultados de los análisis deben tomarse con la debida cautela.*

""")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown('<p class="small-text">Reporte preparado por CEPAL Lab para el Trade Emergency Team</p>', unsafe_allow_html=True)
with col2:
    st.markdown('<p class="small-text"> </p>', unsafe_allow_html=True)
with col3:
    st.markdown('<p class="small-text">©2025 Cepal Lab</p>', unsafe_allow_html=True)
