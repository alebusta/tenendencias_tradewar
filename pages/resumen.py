import streamlit as st
import pandas as pd
import numpy as np
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
with open("front/style.css", "r") as f:
    css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


if st.button("Ir a Inicio"):
    st.switch_page("app.py")


# Contenido de la aplicación
st.markdown("""	
            
    <div class="news-text">
        <div class="div-news-description">
            
# Tensiones comerciales y realineamientos geopolíticos: El impacto de la administración Trump en América Latina y el mundo

*Semana del reporte: 20 al 27 de abril de 2025*

## Diagnóstico

Durante la última semana de abril de 2025, el mundo ha sido testigo de la intensificación de las tensiones comerciales lideradas por la administración Trump, con repercusiones significativas en América Latina y a nivel global. La imposición de aranceles, la renegociación de acuerdos comerciales y las amenazas de expansión territorial han generado incertidumbre y volatilidad en los mercados, así como realineamientos geopolíticos.

**Política Comercial y Tensiones Geopolíticas:**

*   **Guerra Comercial EE.UU.-China:** La imposición de aranceles por parte de EE.UU. a productos chinos ha provocado una respuesta recíproca de China, afectando a empresas de ambos países y generando preocupación por una posible paralización de la economía mundial. Economistas españoles como Santiago Niño Becerra advierten sobre una posible "situación Covid" si las negociaciones entre ambas potencias no avanzan.
*   **Impacto en América Latina:** Los aranceles de Trump, aunque bajos para la región, amenazan con afectar la demanda de productos básicos y depreciar los tipos de cambio. El FMI proyecta una moderación del crecimiento en América Latina y el Caribe, con excepción de Argentina y Ecuador, que se espera tengan un repunte importante gracias a programas respaldados por el FMI.
*   **Reacciones Regionales:**
    *   **México:** Se espera una contracción del PIB debido al impacto de los aranceles. La presidenta Claudia Sheinbaum ha expresado su desacuerdo con las políticas de Trump y ha buscado alternativas para mantener la integración a la economía norteamericana.
    *   **Ecuador:** Se espera un crecimiento del 1.7%, impulsado por programas respaldados por el FMI.
    *   **Argentina:** Se espera un repunte importante en su economía, con un crecimiento del 5.5%, también impulsado por programas del FMI.
    *   **Uruguay:** La industria cárnica se adapta a la amenaza de los aranceles, buscando nuevos mercados en China.
    *   **Bolivia:** Se opuso a la iniciativa continental para negociar el Área de Libre Comercio de las Américas (ALCA) y a la posibilidad de negociar un Tratado de Libre Comercio (TLC) bilateral con los EE.UU. y con la Unión Europea.
*   **Demandas y Desafíos Internos en EE.UU.:** Una coalición de estados demócratas ha demandado a la administración Trump por los aranceles, argumentando que son ilegales y afectan las importaciones. Además, empresas estadounidenses enfrentan dificultades para encontrar alternativas a China como proveedor, lo que podría generar escasez y aumento de precios.
*   **Expansión Territorial y Control de Recursos:**
    *   **Canal de Panamá y Suez:** Trump exige paso libre para buques estadounidenses, generando controversia internacional.


**Realineamientos Geopolíticos:**

*   **Acercamiento a China:** Países como España y Uruguay buscan fortalecer lazos económicos con China ante la incertidumbre con EE.UU.
*   **Tensiones con aliados tradicionales:** Alemania y Francia buscan mayor autonomía militar y económica ante la política de "America First". Canadá fortalece lazos con Europa.
*   **Elecciones en Canadá:** La elección de un nuevo primer ministro en Canadá se ve influenciada por la necesidad de "plantar cara" a Trump y su política comercial.
*   **Críticas internas en EE.UU.:** Figuras como Gary Cohn, exasesor económico de Trump, critican los aranceles por ser "altamente regresivos" y afectar a la clase baja.

## Tendencias

1.  **Fragmentación del comercio global:** La imposición de aranceles y el proteccionismo estadounidense están fragmentando el comercio global en bloques regionales, generando ineficiencias y riesgos para el crecimiento.
2.  **Aumento de la incertidumbre geopolítica:** Las acciones unilaterales de la administración Trump, como las amenazas de expansión territorial y el desconocimiento de acuerdos internacionales, están generando desconfianza y volatilidad en las relaciones internacionales.
3.  **Realineamiento de alianzas:** Los países están buscando diversificar sus relaciones económicas y de seguridad, fortaleciendo lazos con otras potencias como China y la Unión Europea, en respuesta a la política de "America First".

## Implicaciones estratégicas

*   **Para América Latina y El Caribe:**
    *   **Corto plazo:** Mayor vulnerabilidad a shocks externos, depreciación de monedas, y posible aumento de la pobreza.
    *   **Mediano plazo:** Necesidad de diversificar mercados, fortalecer la integración regional, y mejorar la competitividad.
    *   **Largo plazo:** Riesgo de quedar atrapada en la disputa entre EE.UU. y China, con limitada capacidad de influir en el nuevo orden global.
*   **Para Estados Unidos:**
    *   **Corto plazo:** Posible recesión, aumento de la inflación, y pérdida de competitividad.
    *   **Mediano plazo:** Aislamiento diplomático, erosión de su liderazgo global, y debilitamiento de su economía.
    *   **Largo plazo:** Riesgo de perder su hegemonía económica y política frente a China y otras potencias.
*   **Para el Mundo:**
    *   **Corto plazo:** Mayor volatilidad en los mercados financieros, disrupciones en las cadenas de suministro, y aumento de la pobreza en países en desarrollo.
    *   **Mediano plazo:** Fragmentación del sistema multilateral de comercio, aumento de las tensiones geopolíticas, y riesgo de conflictos armados.
    *   **Largo plazo:** Un mundo multipolar con reglas menos claras y mayor competencia entre potencias, con consecuencias impredecibles para la paz y la prosperidad global.

## Factores clave a vigilar

*   **Evolución de la guerra comercial EE.UU.-China:** Cualquier señal de escalada o desescalada tendrá un impacto inmediato en los mercados y en las decisiones de inversión.
*   **Reacciones de los países de la región:** Es clave observar si los países de América Latina y el Caribe logran coordinar una respuesta conjunta a los desafíos planteados por la administración Trump.
*   **Elecciones en EE.UU. en 2028:** El resultado de las próximas elecciones presidenciales en EE.UU. podría marcar un cambio radical en la política comercial y exterior del país, con consecuencias significativas para el mundo.
*   **Acuerdos bilaterales y regionales:** Es importante monitorear los acuerdos que EE.UU. logre negociar con otros países, así como los esfuerzos de integración regional en América Latina y otras partes del mundo.
*   **Indicadores económicos clave:** Prestar atención a los datos de crecimiento, inflación, desempleo, y balanza comercial en EE.UU., China, y los principales países de América Latina y el Caribe.
            </div>

 """, unsafe_allow_html=True)

st.markdown("""---""")	
st.header("Resúmenes anteriores")

with st.expander("Tercera semana de abril de 2025", expanded=False):
    st.markdown("""	
                
        <div class="news-text">
            <div class="div-news-description">
                
    # Tensiones comerciales, realineamientos geopolíticos y vulnerabilidades regionales: El impacto de la guerra comercial en América Latina y el mundo

    *Tercera semana de abril: 14 al 20 de abril de 2025*

    ## Diagnóstico

    **Estados Unidos:**
    Durante la semana, Estados Unidos, bajo la administración Trump, intensificó su postura en la guerra comercial, generando una ola de incertidumbre y reacciones a nivel global. Se implementaron aranceles más altos a productos chinos, alcanzando hasta un 145%, lo que provocó una respuesta inmediata de Pekín con aranceles recíprocos. Esta escalada llevó a la [Organización Mundial del Comercio (OMC)](https://www.msn.com/es-mx/dinero/econom%C3%ADa/el-comercio-mundial-caer%C3%A1-entre-0-2-y-1-5-este-a%C3%B1o-se%C3%B1ala-la-omc/ar-AA1D2C3t) a advertir sobre una posible contracción del comercio mundial y a revisar a la baja las previsiones de crecimiento económico. A pesar de este panorama sombrío, la administración Trump mantuvo su postura, argumentando la necesidad de proteger la industria estadounidense y corregir desequilibrios comerciales.

    En el frente interno, la administración Trump buscó mitigar el impacto de los aranceles en algunos sectores, anunciando exenciones temporales para productos tecnológicos y considerando medidas similares para la industria automotriz. Sin embargo, estas acciones no lograron calmar por completo la preocupación de los mercados y de diversos sectores económicos, que temen un aumento de la inflación y una desaceleración del crecimiento. Además, la política comercial de Trump generó tensiones con socios comerciales clave, como la Unión Europea, y provocó que algunos países buscaran alternativas para diversificar sus relaciones comerciales y reducir su dependencia de Estados Unidos.

    **China:**
    China por su parte ha mantenido una postura firme frente a la creciente guerra comercial con Estados Unidos, aunque también ha dejado la puerta abierta a negociaciones bajo ciertas condiciones. El gobierno chino ha criticado las políticas arancelarias de Trump, calificándolas de "[juego de números](https://www.prensa.com/mundo/china-declara-que-ignorara-los-juegos-de-numeros-arancelarios-de-estados-unidos/)" y advirtiendo que tomará contramedidas si Estados Unidos persiste en socavar sus intereses. A pesar de estas tensiones, ha expresado su disposición a dialogar, siempre y cuando se respeten sus intereses y se aborden temas como las sanciones y Taiwán. Además de su postura diplomática, China ha tomado medidas concretas para mitigar el impacto de los aranceles estadounidenses. Ha impulsado la diversificación de sus mercados de exportación, buscando nuevos socios comerciales en Europa, el Sudeste Asiático, África y América Latina. También ha acelerado sus esfuerzos para lograr la autosuficiencia tecnológica, invirtiendo fuertemente en investigación y desarrollo en sectores clave como los semiconductores y la inteligencia artificial. Estas acciones reflejan la determinación de China de resistir la presión de Estados Unidos y mantener su posición como potencia económica global.

    **Organismos Internacionales:**
    Los organismos internacionales han expresado una creciente preocupación por las consecuencias de la guerra comercial global. [El Fondo Monetario Internacional (FMI)](https://www.financialexpress.com/world-news/global-recession-unlikely-even-as-trade-tensions-flare-amid-trump-tariffs-says-imf/3813416/) ha advertido sobre una desaceleración del crecimiento económico mundial y un aumento de la inflación como resultado de las tensiones comerciales y los aranceles impuestos por Estados Unidos. Kristalina Georgieva, directora gerente del FMI, ha señalado que las nuevas proyecciones de crecimiento incluirán reducciones significativas, aunque no se espera una recesión. La Organización Mundial del Comercio (OMC) también ha expresado su inquietud, advirtiendo sobre una posible contracción del comercio mundial debido a las políticas arancelarias y la incertidumbre que generan.

    Además de las preocupaciones económicas, los organismos internacionales también han destacado los riesgos geopolíticos asociados con la guerra comercial. La imposición de aranceles y las represalias comerciales están generando tensiones entre las principales economías del mundo, lo que podría socavar la cooperación multilateral y la estabilidad global. Algunos expertos han advertido sobre la posibilidad de una fragmentación de la economía mundial en bloques comerciales rivales, lo que tendría consecuencias negativas para el crecimiento y el desarrollo a largo plazo.

    **Latinoamérica y El Caribe:**
    El impacto de las políticas de Donald Trump en América Latina y el Caribe es complejo y multifacético. Por un lado, la imposición de aranceles y la retórica proteccionista generan incertidumbre y preocupación en la región, especialmente en países con economías dependientes de las exportaciones a Estados Unidos. Se teme una desaceleración del crecimiento económico, la pérdida de empleos y el aumento de la inflación. Por otro lado, algunos países ven en esta situación una oportunidad para diversificar sus mercados y fortalecer sus lazos comerciales con otras regiones, como Asia y Europa.

    La región enfrenta vulnerabilidades significativas ante la escalada de tensiones comerciales globales. Los aranceles impuestos por Estados Unidos amenazan exportaciones clave como el banano peruano, el vino Malbec argentino y productos agroindustriales colombianos. Al mismo tiempo, existe preocupación por una posible avalancha de productos chinos en mercados como el peruano, ante la búsqueda de nuevos destinos por parte de China. Además, la Zona Libre de Colón en Panamá se ve sometida a crecientes presiones logísticas y comerciales como efecto colateral del conflicto entre las dos principales potencias.

    En respuesta a estas políticas, los países de América Latina y el Caribe están adoptando diversas estrategias. Algunos buscan negociar acuerdos bilaterales con Estados Unidos para mitigar el impacto de los aranceles, mientras que otros apuestan por fortalecer la integración regional y promover el comercio Sur-Sur. Además, se observa un creciente interés en diversificar las relaciones comerciales y buscar nuevos socios estratégicos. Por ejemplo, México, aunque ligado al T-MEC con EE.UU. y Canadá, busca alternativas en Asia. Chile, por su parte, ha expresado su intención de mantener los mejores vínculos con China, así como fortalecer el tratado de libre comercio con Estados Unidos, mientras que Brasil ha activado su "[Ley de Reciprocidad Económica](https://www.nodal.am/2025/04/brasil-el-gobierno-activa-la-ley-de-reciprocidad-economica-en-respuesta-a-los-aranceles-de-trump/)" para responder a las medidas proteccionistas de Trump. Estas acciones reflejan la búsqueda de un equilibrio entre la dependencia de Estados Unidos y la necesidad de adaptarse a un nuevo orden económico mundial.


    ## Tendencias

    1.  **Fragmentación del comercio mundial:** La imposición de aranceles y la búsqueda de acuerdos bilaterales están fragmentando el comercio mundial en bloques, con China y Estados Unidos compitiendo por influencia.Varios países, incluyendo Japón, Reino Unido, Corea del Sur e India, están en negociaciones con Estados Unidos para buscar acuerdos comerciales que mitiguen el impacto de los aranceles.
    2.  **Realineamiento geopolítico:** Ante la imprevisibilidad de las políticas estadounidenses, los países de América Latina están buscando diversificar sus alianzas y fortalecer sus lazos con otras potencias, como China y la Unión Europea.
    3.  **Aumento de la incertidumbre económica:** La guerra comercial y la volatilidad de las políticas estadounidenses están generando incertidumbre en los mercados y afectando las decisiones de inversión de las empresas. Empresas de diversos sectores, como tecnología (Nvidia, ASML), automotriz (Ford), y productos de consumo (e.l.f. Beauty, Shein, Temu), se están viendo afectadas por los aranceles, lo que las está llevando a ajustar sus estrategias de producción, precios y cadenas de suministro.
    4.  **Reconfiguración de las Cadenas de Suministro:** Las empresas están buscando diversificar sus cadenas de suministro para reducir su dependencia de China y mitigar el impacto de los aranceles.
    5.  **Aumento del Proteccionismo:** Se observa una tendencia creciente hacia el proteccionismo en varios países, con medidas que buscan proteger las industrias locales de la competencia extranjera.

    ## Implicaciones estratégicas

    *   **Para la Región:**
        *   **Corto Plazo:** Mayor incertidumbre económica, volatilidad en los mercados financieros, y presión sobre las exportaciones.
        *   **Mediano Plazo:** Necesidad de diversificar las relaciones comerciales, fortalecer la integración regional, y buscar nuevas fuentes de inversión.
        *   **Largo Plazo:** Posible reconfiguración de la economía regional, con un mayor enfoque en la producción local y el desarrollo de nuevas industrias.
    *   **Para Estados Unidos:**
        *   **Corto Plazo:** Aumento de la inflación, disrupción de las cadenas de suministro, y posible desaceleración económica.
        *   **Mediano Plazo:** Erosión de la competitividad, pérdida de influencia en la región, y riesgo de aislamiento comercial.
        *   **Largo Plazo:** Posible declive de su hegemonía económica y política a nivel global.
    *   **Para el Mundo:**
        *   **Corto Plazo:** Mayor volatilidad en los mercados financieros, aumento de la incertidumbre económica, y riesgo de recesión global.
        *   **Mediano Plazo:** Fragmentación del comercio global, reconfiguración de las alianzas geopolíticas, y posible surgimiento de nuevos centros de poder económico.
        *   **Largo Plazo:** Un mundo más multipolar, con un sistema de comercio internacional menos basado en reglas y más en la correlación de fuerzas.

    ## Factores clave a vigilar

    1.  **Impacto de los aranceles de Trump en las exportaciones latinoamericanas:** Monitorear de cerca cómo los aranceles impuestos por la administración Trump afectan a las exportaciones de la región, especialmente en sectores como la agroindustria, textiles y manufacturas. Observar si las empresas latinoamericanas pueden diversificar sus mercados o si se ven obligadas a reducir su producción.

    2.  **Reacciones de los gobiernos latinoamericanos a la política comercial de EE.UU.:** Seguir de cerca las respuestas de los gobiernos de la región a las políticas comerciales de Trump, incluyendo posibles negociaciones bilaterales, acuerdos con otros bloques comerciales (como la UE o China) y medidas de apoyo a los sectores afectados.

    3.  **Tensiones geopolíticas en la región:** Vigilar las tensiones entre Estados Unidos y China en América Latina, incluyendo la competencia por influencia económica y política, y el impacto en la soberanía de los países de la región.

    4.  **Situación económica en Venezuela:** Monitorear la situación económica y política en Venezuela, incluyendo el impacto de las sanciones estadounidenses, la migración y las próximas elecciones.

    5.  **Impacto en la industria tecnológica:** Observar cómo las restricciones comerciales de EE.UU. sobre semiconductores y otras tecnologías afectan a las empresas de la región, incluyendo posibles cambios en las cadenas de suministro y la inversión en innovación.

    ---

    ## Datos relevantes de la guerra comercial

    ### *Ámbito Global* 
    La economía mundial se enfrenta a una creciente incertidumbre debido a las tensiones comerciales impulsadas por las políticas arancelarias de Estados Unidos. Organismos como el FMI y la OMC han advertido sobre una posible desaceleración del crecimiento global y un aumento de la inflación. Los precios de las materias primas, como el petróleo, han experimentado fluctuaciones debido a las tensiones geopolíticas y las sanciones. Las decisiones de política monetaria de los bancos centrales, como el BCE, están siendo influenciadas por la necesidad de mitigar los efectos negativos de la guerra comercial. Las proyecciones de crecimiento económico mundial están siendo revisadas a la baja, reflejando el impacto de las políticas proteccionistas en el comercio y la inversión.

    ### *Latinoamérica y el Caribe*

    *   **Argentina:**
        *   **62%** [Participación del Malbec en las exportaciones de vino fraccionado, poco más de la mitad tiene como destine Estados Unidos](https://www.diariodecuyo.com.ar/economia/aranceles-de-donald-trum-que-puede-pasar-con-las-exportaciones-de-malbec-1723279.html) - 2024
    *   **Brasil:**
        *   **40%** en [Producción mundial de soja](https://www.nytimes.com/2025/04/20/business/tariffs-china-us-farmers.html)
    *   **Panamá:**
        *   **15.1%** [Caída del movimiento comercial (en dólares)](https://www.prensa.com/economia/zona-libre-de-colon-sufre-los-coletazos-del-conflicto-comercial-entre-trump-y-china/) durante el primer trimestre de 2025 en la Zona Libre de Colón producto de las tensiones comerciales EEUU-China
                </div>

    """, unsafe_allow_html=True)

with st.expander("Segunda semana de abril de 2025", expanded=False):
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
