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
with open("style.css", "r") as f:
    css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


if st.button("Ir a Inicio"):
    st.switch_page("app.py")


#========== Contenido de la aplicación ===========


st.markdown("""

<div class="news-text">
        <div class="div-news-description">
# Tensiones comerciales, conflictos geopolíticos y la economía global: Un análisis de la semana

*Semana del reporte*: 22 de junio de 2025

## Diagnóstico

Durante la semana terminada el 22 de junio de 2025, el panorama noticioso estuvo dominado por la persistente tensión comercial impulsada por las políticas de la administración Trump, la escalada del conflicto entre Israel e Irán, y sus consecuentes efectos en la economía global. Se observó una clara división entre las potencias mundiales respecto a cómo abordar estos desafíos, con implicaciones significativas para Latinoamérica y el Caribe.

**Tensiones Comerciales y Aranceles:**

*   **EE.UU. vs. China:** La administración Trump continuó implementando políticas arancelarias agresivas contra China, afectando a exportadores chinos y a gigantes del comercio electrónico. Se mencionó la posibilidad de reducir los aranceles del 145% al 80% antes de una reunión entre funcionarios de ambos países, aunque esto no se concretó de manera unilateral.
*   **Impacto en Vietnam:** Las tarifas "recíprocas" de EE.UU. sobre las exportaciones vietnamitas, aunque pausadas temporalmente, amenazan el objetivo de crecimiento del PIB de Vietnam para 2025.
*   **Desvío de Comercio:** Se observó un desvío de comercio, con empresas chinas buscando nuevos mercados en el Sudeste Asiático, Europa y Latinoamérica debido a las restricciones en EE.UU. Esto generó preocupación en algunos países sobre la competencia desleal y el dumping de productos chinos.
*   **Impacto en Latinoamérica:** Se advirtió que el aumento de los aranceles podría afectar a la región, incrementando los precios y desacelerando el crecimiento global. Se destacó la necesidad de que Latinoamérica refuerce su integración económica para enfrentar la guerra comercial.
*   **Acuerdo EE.UU. y México:** Se anunció un acuerdo entre EE.UU. y México para un pacto global que contemple seguridad, migración y comercio.

**Conflicto Israel-Irán y Repercusiones:**

*   **Escalada del Conflicto:** Los ataques entre Israel e Irán se intensificaron, con EE.UU. involucrándose directamente al bombardear instalaciones nucleares iraníes. Esto generó temores de una guerra más amplia en Medio Oriente.
*   **Impacto Económico:** El conflicto provocó volatilidad en los mercados financieros, aumento de los precios del petróleo y fortalecimiento del dólar como activo refugio. Se temía el cierre del Estrecho de Ormuz, lo que podría causar un shock en el suministro de petróleo y un aumento de la inflación global.
*   **Reacciones Internacionales:** La comunidad internacional se dividió ante los ataques de EE.UU. a Irán. China y Rusia condenaron las acciones, mientras que algunos países europeos llamaron a la desescalada.
*   **Postura de Latinoamérica:** El presidente de Chile, Gabriel Boric, condenó el bombardeo de EE.UU. a Irán, generando un debate entre el oficialismo y la oposición en su país.
*   **Implicaciones para la Política Monetaria:** El conflicto complicó las deliberaciones de la Reserva Federal (Fed) sobre las tasas de interés, ya que añadió incertidumbre a las perspectivas de inflación y crecimiento económico.

**Acercamientos y Medidas en Latinoamérica y El Caribe:**

*   **Colombia y el Nuevo Banco de Desarrollo (NBD):** Colombia fue aceptada como miembro del NBD de los BRICS, buscando diversificar sus alianzas y fortalecer su economía.
*   **República Dominicana:** Se observó un aumento en las remesas recibidas por República Dominicana, lo que podría verse afectado por la crisis global.
*   **Ecuador:** El gobierno de Ecuador impuso un arancel a las compras por Amazon y Temu para proteger la producción nacional.
*   **Chile:** Se destacó que Chile se posicionó como el mayor exportador mundial de 24 productos en 2024.

## Tendencias

1.  **Fragmentación del Comercio Global:** Las políticas proteccionistas de EE.UU. están llevando a una fragmentación del comercio mundial, con la formación de bloques regionales y acuerdos bilaterales.
2.  **Reconfiguración de las Cadenas de Suministro:** Las empresas están buscando diversificar sus cadenas de suministro fuera de China para mitigar los riesgos asociados con la guerra comercial y las tensiones geopolíticas.
3.  **Aumento de la Incertidumbre Económica:** Los conflictos geopolíticos y las políticas comerciales impredecibles están generando incertidumbre en los mercados financieros y afectando las decisiones de inversión.
4.  **Presión Inflacionaria:** Los aranceles y el aumento de los precios del petróleo están ejerciendo presión sobre la inflación global, lo que complica las decisiones de los bancos centrales sobre las tasas de interés.
5.  **Búsqueda de Alternativas al Dólar:** Algunos países están explorando el uso de monedas alternativas en el comercio internacional para reducir su dependencia del dólar estadounidense.

## Implicaciones Estratégicas

*   **Para Latinoamérica y el Caribe:** La región enfrenta el desafío de adaptarse a un entorno global más fragmentado e incierto. Es crucial fortalecer la integración regional, diversificar los mercados de exportación e invertir en sectores estratégicos como la tecnología y la energía renovable.
*   **Para Estados Unidos:** Las políticas proteccionistas de la administración Trump podrían tener consecuencias negativas a largo plazo para la economía estadounidense, incluyendo el aumento de la inflación, la reducción del crecimiento y el aislamiento político.
*   **Para el Mundo:** La escalada de las tensiones comerciales y geopolíticas amenaza la estabilidad del sistema multilateral y podría conducir a una mayor fragmentación del orden internacional.

## Factores Clave a Vigilar

*   **Evolución del Conflicto Israel-Irán:** La escalada o desescalada del conflicto tendrá un impacto significativo en los precios del petróleo y la estabilidad de la región.
*   **Decisiones de la Reserva Federal:** Las decisiones de la Fed sobre las tasas de interés influirán en la inflación y el crecimiento económico global.
*   **Negociaciones Comerciales:** El resultado de las negociaciones comerciales entre EE.UU. y sus socios comerciales determinará el futuro del comercio global y la estabilidad de las cadenas de suministro.
*   **Reacciones de China:** La respuesta de China a las políticas comerciales de EE.UU. y su estrategia para contrarrestar la presión económica serán cruciales para el futuro del comercio global.


</div>
 """, unsafe_allow_html=True)

#### Resúmenes anteriores

st.markdown("""---""")	
st.header("Resúmenes anteriores")

with st.expander("tercera semana de junio de 2025", expanded=False):

    st.markdown("""
    <div class="news-text">
        <div class="div-news-description">

# Reconfiguración del Comercio Global: Tensiones, Adaptaciones y Nuevas Alianzas en la Era Trump

*Semana del reporte: 15 de junio de 2025*

## Diagnóstico

Durante la semana del 15 de junio de 2025, el panorama económico global se caracterizó por la persistencia de tensiones comerciales, principalmente impulsadas por las políticas de la administración Trump, y la búsqueda de nuevas estrategias por parte de los países para mitigar sus efectos. Los principales hechos noticiosos se centraron en:

1.  **Tensiones Comerciales y Aranceles:** La administración Trump continuó aplicando aranceles unilaterales, generando incertidumbre y volatilidad en los mercados. Se observó una fuerte presión sobre la Unión Europea y China, con amenazas de aumentar los aranceles existentes. Por ejemplo, Trump amenazó con imponer aranceles del 50% a las importaciones de acero y aluminio de la UE, lo que provocó una respuesta de la presidenta de la Comisión Europea, Ursula von der Leyen, quien reiteró el compromiso de la UE de alcanzar un acuerdo comercial con Estados Unidos antes del 9 de julio.
2.  **Reacciones y Adaptaciones Regionales:** Los países de América Latina y el Caribe, así como otras economías emergentes, están adaptando sus estrategias comerciales para enfrentar el proteccionismo estadounidense. México, por ejemplo, ha visto una disminución en sus exportaciones a Estados Unidos debido a los aranceles, pero está buscando diversificar sus mercados y fortalecer su competitividad. Perú también está explorando nuevos mercados en Asia, aprovechando la infraestructura del Puerto de Chancay.
3.  **Conflictos Geopolíticos y su Impacto Económico:** La crisis en Medio Oriente, particularmente las tensiones entre Israel e Irán, añadió otra capa de complejidad al panorama económico. Estos conflictos provocaron un aumento en los precios del petróleo y mayores costos logísticos, afectando el comercio global. Los líderes del G7 se reunieron en Canadá para discutir estas tensiones y buscar una desescalada.
4.  **China y su Estrategia Comercial:** China, enfrentada a las políticas proteccionistas de Estados Unidos, está fortaleciendo sus lazos comerciales con otros países, especialmente en África y Asia. China ofreció acceso libre de aranceles a 53 países africanos y está promoviendo el uso del yuan digital en transacciones internacionales. Vietnam, como miembro del BRICS, se ha convertido en un aliado clave de China para eludir los aranceles estadounidenses.
5.  **Impacto en la Migración y el Trabajo:** Las políticas migratorias restrictivas de la administración Trump están generando temor e inseguridad en las comunidades inmigrantes en Estados Unidos, afectando a sectores como la agricultura, la hostelería y la construcción. Las redadas del ICE en Los Ángeles provocaron protestas y una disminución en las ventas de restaurantes y supermercados latinos.

## Tendencias

1.  **Fragmentación del Comercio Global:** Las políticas proteccionistas de Estados Unidos están llevando a una fragmentación del comercio global, con países buscando acuerdos bilaterales y regionales en lugar de depender de un sistema multilateral.
2.  **Desdolarización:** Algunos países están explorando alternativas al dólar estadounidense en el comercio internacional, como el uso del yuan digital o acuerdos bilaterales en monedas locales.
3.  **Regionalización de las Cadenas de Suministro:** Las empresas están reevaluando sus cadenas de suministro para reducir su dependencia de un solo país o región, buscando diversificar sus fuentes de producción y distribución.
4.  **Aumento de la Inversión en Infraestructura Regional:** Países como Perú están invirtiendo en infraestructura portuaria para facilitar el comercio con nuevos mercados, especialmente en Asia.
5.  **Mayor Intervención Estatal en la Economía:** Los gobiernos están adoptando un papel más activo en la economía, implementando políticas industriales, ofreciendo subsidios y regulando el comercio para proteger sus industrias nacionales.

## Implicaciones Estratégicas

*   **Para la Región:** América Latina y el Caribe enfrentan el desafío de adaptarse a un entorno comercial global más fragmentado e incierto. La diversificación de mercados, la promoción de la integración regional y la inversión en infraestructura son estrategias clave para mitigar los riesgos y aprovechar las oportunidades.
*   **Para Estados Unidos:** Las políticas proteccionistas de la administración Trump pueden generar beneficios a corto plazo para algunas industrias nacionales, pero también conllevan riesgos de inflación, disrupción de las cadenas de suministro y pérdida de competitividad a largo plazo.
*   **Para el Mundo:** El auge del proteccionismo y la fragmentación del comercio global pueden llevar a una menor eficiencia económica, mayores precios y un aumento de las tensiones geopolíticas. La cooperación internacional y la búsqueda de soluciones multilaterales son esenciales para evitar una escalada de conflictos comerciales.

## Factores Clave a Vigilar

1.  **Decisiones de la Reserva Federal:** Las decisiones de la Reserva Federal sobre las tasas de interés tendrán un impacto significativo en la economía estadounidense y en los flujos de capital hacia los mercados emergentes.
2.  **Negociaciones Comerciales:** El resultado de las negociaciones comerciales entre Estados Unidos y la Unión Europea, China y otros países será determinante para el futuro del comercio global.
3.  **Conflictos Geopolíticos:** La evolución de los conflictos en Medio Oriente y Ucrania, así como las tensiones entre China y Taiwán, pueden tener un impacto significativo en los precios de la energía, las cadenas de suministro y la estabilidad financiera.
4.  **Políticas Migratorias:** Las políticas migratorias de Estados Unidos y su impacto en la disponibilidad de mano de obra y en las remesas hacia América Latina y el Caribe.

</div>
 """, unsafe_allow_html=True)


with st.expander("Segunda semana de junio de 2025", expanded=False):

    st.markdown("""

<div class="news-text">
        <div class="div-news-description">
        
# Reconfiguración del Comercio Global: Tensiones Arancelarias y Adaptación Regional en América Latina y El Caribe

*Semana del reporte: Semana del 02 al 08 de junio de 2025*

## Diagnóstico

Durante la semana analizada, la administración Trump intensificó su política comercial proteccionista, generando una onda expansiva de incertidumbre y adaptación en la economía global, con particular énfasis en América Latina y El Caribe. Los principales hechos noticiosos se centran en:

1.  **Escalada de Tensiones Arancelarias:** Trump duplicó los aranceles sobre las importaciones de acero y aluminio al 50% (04 de junio), afectando a socios comerciales clave como México, Canadá, Brasil, Corea del Sur y Vietnam. Esta medida, justificada bajo la premisa de seguridad nacional, provocó fuertes críticas y promesas de represalias.
2.  **Negociaciones Comerciales en Juego:** En medio de la escalada arancelaria, se llevaron a cabo negociaciones comerciales entre Estados Unidos y China en Londres (08 y 09 de junio). Si bien se buscaba una tregua, las tensiones persistieron debido a desacuerdos sobre el cumplimiento de acuerdos previos y restricciones en el comercio de tierras raras y semiconductores.
3.  **Impacto en la Región:** Los aranceles estadounidenses generaron preocupación en América Latina y El Caribe, con advertencias sobre posibles efectos negativos en el crecimiento económico, el empleo y la estabilidad social. Costa Rica, por ejemplo, alertó sobre los efectos en sus zonas francas (08 de junio), mientras que la Coparmex en México condenó el aumento de aranceles (08 de junio).
4.  **Búsqueda de Alternativas:** Ante la incertidumbre generada por las políticas de Trump, países de la región exploraron alternativas para diversificar sus relaciones comerciales y fortalecer la cooperación regional. Se destacó la importancia de acuerdos como el Mercosur-UE y la necesidad de generar certezas jurídicas para atraer inversión extranjera (08 de junio).
5.  **Reacciones y Adaptación:** Los países de la región tomaron diversas medidas para mitigar el impacto de las políticas estadounidenses. México y Canadá expresaron su rechazo a los aranceles y buscaron revertir la medida (09 de junio), mientras que Uruguay impulsó la firma del acuerdo Mercosur-UE (08 de junio). En España, la agencia gubernamental ICEX lanzó un paquete de medidas para contrarrestar el impacto de la guerra arancelaria (08 de junio).

## Tendencias

1.  **Aumento del Proteccionismo:** La administración Trump reafirmó su política proteccionista, priorizando los intereses nacionales y utilizando aranceles como herramienta de presión en las negociaciones comerciales.
2.  **Fragmentación del Comercio Global:** Las tensiones comerciales y la imposición de aranceles generaron una fragmentación del comercio global, con países buscando acuerdos bilaterales y regionales en lugar de soluciones multilaterales.
3.  **Reconfiguración de las Cadenas de Suministro:** Las empresas se vieron obligadas a reevaluar sus cadenas de suministro, buscando proveedores alternativos y relocalizando la producción para mitigar el impacto de los aranceles.
4.  **Mayor Incertidumbre Económica:** La incertidumbre generada por las políticas comerciales de Trump afectó la confianza de los inversores y las perspectivas de crecimiento económico, tanto a nivel global como regional.
5.  **Fortalecimiento de la Cooperación Regional:** Los países de América Latina y El Caribe buscaron fortalecer la cooperación regional y diversificar sus relaciones comerciales para hacer frente a los desafíos del nuevo orden comercial global.

## Implicaciones estratégicas

*   **Para la región:** En el corto plazo, los países de América Latina y El Caribe enfrentan el desafío de adaptarse a un entorno comercial más volátil e incierto. A mediano y largo plazo, la región podría beneficiarse de la reconfiguración de las cadenas de suministro y el aumento de la cooperación regional, siempre y cuando logre generar certezas jurídicas y reglas claras para atraer inversión extranjera.
*   **Para Estados Unidos:** La política proteccionista de Trump podría generar beneficios a corto plazo para algunas industrias nacionales, pero a largo plazo podría perjudicar la competitividad de la economía estadounidense y su liderazgo en el comercio global.
*   **Para el mundo:** La intensificación de las tensiones comerciales y la fragmentación del comercio global podrían tener efectos negativos en el crecimiento económico mundial y la estabilidad geopolítica.

## Factores clave a vigilar

1.  **Evolución de las negociaciones comerciales entre Estados Unidos y China:** El resultado de estas negociaciones será determinante para el futuro del comercio global y las perspectivas económicas de la región.
2.  **Reacciones de los países afectados por los aranceles estadounidenses:** Las medidas que tomen estos países en respuesta a los aranceles podrían intensificar las tensiones comerciales o abrir la puerta a nuevas negociaciones.
3.  **Impacto de las políticas estadounidenses en la inversión extranjera directa en la región:** La incertidumbre generada por las políticas de Trump podría desincentivar la inversión extranjera directa en América Latina y El Caribe, afectando su crecimiento económico.
4.  **Avances en la integración regional y la diversificación comercial:** Los esfuerzos de los países de la región por fortalecer la cooperación regional y diversificar sus relaciones comerciales serán clave para mitigar el impacto de las políticas estadounidenses.
5.  **Decisiones de la Reserva Federal de Estados Unidos sobre las tasas de interés:** Las decisiones de la Reserva Federal sobre las tasas de interés podrían tener un impacto significativo en los flujos de capitales hacia las economías emergentes, incluyendo las de América Latina y El Caribe.


</div>
 """, unsafe_allow_html=True)
        

with st.expander("Primera semana de junio de 2025", expanded=False):

    st.markdown("""

<div class="news-text">
        <div class="div-news-description">
        
# Repercusiones Globales de la Política Comercial de Trump: Tensiones y Adaptaciones

*Semana del reporte: Última semana de mayo*

## Diagnóstico

Durante la semana del 25 al 1 de junio de 2025, la política comercial de la administración Trump continuó generando tensiones y reacciones a nivel global. Los principales hechos noticiosos se centraron en la imposición y posterior suspensión de aranceles, las negociaciones comerciales en curso y las respuestas de diversos países y bloques económicos a las políticas proteccionistas de Estados Unidos.

*   **Escalada y distensión en la guerra comercial EEUU-China:** Se destacan las acusaciones mutuas entre Estados Unidos y China sobre el incumplimiento de acuerdos comerciales previos. Trump acusó a China de "violar totalmente" el acuerdo arancelario de mayo, mientras que China rechazó estas acusaciones y acusó a EE. UU. de "socavar gravemente" la tregua arancelaria de Ginebra (01 de junio). Sin embargo, funcionarios de la Casa Blanca sugirieron que una conversación entre Trump y Xi Jinping podría ocurrir pronto para resolver las tensiones comerciales (01 de junio).
*   **Aumento de aranceles al acero y aluminio:** Trump anunció un aumento del 25% al 50% en los aranceles al acero y aluminio, efectivo a partir del 4 de junio (01 de junio). Esta medida generó preocupación en Japón, que vigila de cerca la situación (02 de junio), y provocó que el secretario del Tesoro de EE. UU., Scott Bessent, defendiera los aranceles como necesarios para la seguridad nacional y la estabilidad laboral en la industria siderúrgica estadounidense (01 de junio).
*   **Tensiones comerciales con Europa:** La administración Trump también mantuvo la presión sobre Europa, con el secretario de Comercio, Howard Lutnick, afirmando que "los aranceles no van a desaparecer" (01 de junio). Esto ocurrió a pesar de un fallo judicial que declaraba ilegales muchos de los aranceles de la administración Trump, aunque este fallo fue apelado (01 de junio). La Unión Europea amenazó con contramedidas ante la subida arancelaria del acero y el aluminio (01 de junio). Finalmente, Trump acordó extender el plazo para un posible acuerdo con la UE hasta el 9 de julio (01 de junio).
*   **Acercamientos y negociaciones bilaterales:** En medio de las tensiones comerciales, Argentina buscó profundizar su relación con Estados Unidos, con la probable visita del secretario de Energía, Chris Wright, para discutir inversiones en Vaca Muerta (01 de junio). Argentina también negocia con Estados Unidos un acuerdo para atenuar el impacto de los aranceles recíprocos.


## Tendencias

1.  **Volatilidad en la política comercial estadounidense:** La administración Trump muestra una tendencia a tomar decisiones comerciales drásticas e impredecibles, generando incertidumbre en los mercados y entre los socios comerciales.
2.  **Énfasis en la seguridad nacional como justificación para el proteccionismo:** La administración Trump utiliza la seguridad nacional como argumento para justificar medidas proteccionistas, como los aranceles al acero y aluminio.
3.  **Búsqueda de acuerdos bilaterales en detrimento del multilateralismo:** Estados Unidos prioriza las negociaciones bilaterales sobre los acuerdos multilaterales, buscando obtener ventajas específicas en cada negociación.
4.  **Reconfiguración de las relaciones comerciales globales:** Las tensiones comerciales impulsadas por Estados Unidos están llevando a otros países a buscar nuevos socios comerciales y a fortalecer la integración regional.
5.  **Impacto diferenciado en América Latina:** La política comercial de Trump afecta de manera desigual a los países de América Latina, generando tanto oportunidades como desafíos para la región.

## Implicaciones estratégicas

*   **Para la región:** Los países de América Latina y el Caribe deben diversificar sus socios comerciales y fortalecer la integración regional para reducir su dependencia de Estados Unidos y mitigar el impacto de las políticas proteccionistas.
*   **Para Estados Unidos:** La política comercial de Trump podría dañar la reputación de Estados Unidos como un socio comercial confiable y socavar su influencia en la región.
*   **Para el mundo:** La persistente incertidumbre en la política comercial global podría frenar el crecimiento económico mundial y aumentar la volatilidad en los mercados financieros.

## Factores clave a vigilar

*   **Evolución de las negociaciones comerciales entre Estados Unidos y China:** Un acuerdo entre las dos potencias podría aliviar las tensiones comerciales globales, mientras que un fracaso en las negociaciones podría intensificarlas.
*   **Decisiones judiciales sobre los aranceles de Trump:** Los fallos judiciales podrían limitar la capacidad de la administración Trump para imponer aranceles y afectar su estrategia comercial.
*   **Reacciones de los países de América Latina y el Caribe:** Es importante observar cómo los países de la región responden a las políticas comerciales de Estados Unidos y qué medidas toman para proteger sus economías.

</div>
 """, unsafe_allow_html=True)


with st.expander("Cuarta semana de mayo de 2025", expanded=False):

    st.markdown("""

<div class="news-text">
        <div class="div-news-description">

# Tensiones comerciales y migratorias: El impacto de las políticas de Trump en Latinoamérica y el mundo

*Semana del reporte:* Semana del 25 de mayo de 2025

## Diagnóstico

Durante la semana del 18 al 25 de mayo de 2025, las noticias estuvieron marcadas por la persistente incertidumbre en torno a las políticas comerciales y migratorias de la administración Trump, con un impacto notable en Latinoamérica y el Caribe, así como en las relaciones globales.

**1. Aranceles y Guerra Comercial:**

*   **Prórroga de aranceles a la UE:** La noticia más recurrente fue la decisión de Trump de prorrogar hasta el 9 de julio la aplicación de aranceles del 50% a productos de la Unión Europea, tras una conversación con Ursula von der Leyen. Este anuncio generó reacciones mixtas, con algunos celebrando la pausa en la escalada comercial y otros expresando escepticismo sobre la duración y el propósito de la tregua.
*   **Impacto en la industria francesa:** Se reportó cómo las industrias francesas se están adaptando a los aranceles estadounidenses, buscando absorber los costos adicionales o reestructurando sus cadenas de valor.
*   **Consecuencias para Florida:** Los aranceles de Trump ya están impactando a Florida, elevando los precios de productos importados como café y materiales de construcción, afectando a pequeñas empresas y consumidores.
*   **Reacción de ASEAN:** Malasia, en nombre de la ASEAN, instó a una mayor integración económica regional para enfrentar las consecuencias de las interrupciones del comercio global y los aranceles de EE.UU.
*   **Tensiones con China:** Persisten las tensiones comerciales y tecnológicas entre EE.UU. y China, con advertencias sobre el uso de chips de Huawei y restricciones a proveedores de Apple.
*   **Efecto en el precio del café:** Se anticipa que el precio del café seguirá subiendo debido a la sequía y los aranceles.
*   **Postura de Colombia:** Se analiza si Colombia podría adoptar medidas fiscales y monetarias agresivas para impulsar oportunidades ante la guerra comercial.
*   **Paraguay:** Se destaca que el país debe priorizar sus relaciones con los países de la región, específicamente con el Mercosur y muy especialmente con Brasil.

**2. Impacto en Remesas:**

*   **Impuesto a las remesas:** Se destaca la preocupación en Honduras por el posible impuesto a las remesas aprobado en primera instancia por el gobierno de Donald Trump, que podría reducir significativamente los ingresos del país.
*   **Análisis en Colombia:** Se menciona que el dólar en Colombia está en una fase de consolidación estructurada, influenciado por la guerra arancelaria de Trump.
*   **Efectos en El Salvador:** Periodistas de El Salvador denuncian una "escalada autoritaria" de Bukele, mientras activistas lo acusan de crear un "clima de terror" en el país.

**3. Hegemonía y Relaciones Geopolíticas:**

*   **Hegemonía de EE.UU.:** Se cuestiona la hegemonía de EE.UU. y se analiza cómo las políticas de Trump podrían fracturarla, beneficiando a otros países como China.
*   **Relaciones con China:** Indonesia y China amplían la cooperación económica y defienden el libre comercio, mientras que México se ofrece como puente para reforzar los lazos de Europa con América.
*   **Interés en Mercosur:** Indonesia centra su atención en el Mercosur, buscando nuevos socios comerciales.
*   **Neutralidad en guerra comercial:** El canciller de Perú destaca la dificultad de mantener la neutralidad en la guerra comercial.
*   **Paraguay y Emiratos Árabes Unidos:** El Presidente de Paraguay se reúne con el presidente de DP World para discutir proyectos portuarios y logísticos.

**4. Crisis en Haití e Inmigración:**

*   **Crisis haitiana:** Se menciona un diálogo en República Dominicana sobre la crisis de Haití y la inmigración indocumentada.

**5. Otros temas relevantes:**

*   **Aprobación de Trump:** El índice de aprobación de Trump se sitúa en el 47%, según una encuesta.
*   **Críticas a la Fed:** El presidente de la Fed, Jerome Powell, defiende la integridad y el servicio público en medio de los ataques de Trump.
*   **Reunión ASEAN:** Malasia se prepara para la cumbre de la ASEAN con énfasis en la guerra comercial, Gaza y Birmania.

## Tendencias

1.  **Proteccionismo selectivo:** La administración Trump continúa aplicando políticas proteccionistas, pero de manera selectiva, priorizando acuerdos bilaterales y ejerciendo presión sobre socios comerciales clave.
2.  **Desglobalización regionalizada:** Se observa una tendencia hacia la regionalización del comercio, con países buscando fortalecer lazos dentro de sus regiones geográficas para mitigar los riesgos de la guerra comercial.
3.  **Debilitamiento de instituciones multilaterales:** La falta de consenso en foros como el G7 y la crítica a organismos internacionales como la OEA sugieren un debilitamiento del multilateralismo y un enfoque más unilateral por parte de EE.UU.
4.  **Reconfiguración de cadenas de suministro:** Las empresas están reevaluando sus cadenas de suministro para reducir la dependencia de China y diversificar sus fuentes de producción.
5.  **Aumento de la inestabilidad económica:** La incertidumbre generada por las políticas de Trump está afectando la confianza de los inversores y generando volatilidad en los mercados financieros.

## Implicaciones estratégicas

*   **Para la región:** Los países de Latinoamérica y el Caribe enfrentan el desafío de diversificar sus socios comerciales y fortalecer la integración regional para reducir su dependencia de EE.UU. y China.
*   **Para Estados Unidos:** Las políticas proteccionistas de Trump podrían generar un aislamiento económico y una pérdida de influencia en la región, así como un aumento de la inflación y una desaceleración del crecimiento.
*   **Para el mundo:** La guerra comercial y la crisis migratoria podrían desestabilizar la economía global y generar tensiones geopolíticas.

## Factores clave a vigilar

1.  **Negociaciones comerciales entre EE.UU. y la UE:** La evolución de estas negociaciones será determinante para el futuro del comercio global.
2.  **Relaciones entre EE.UU. y China:** La escalada o desescalada de las tensiones comerciales y tecnológicas entre estas dos potencias tendrá un impacto significativo en la economía mundial.
3.  **Situación en Haití:** La crisis humanitaria y política en Haití podría generar una mayor presión migratoria en la región y requerir una respuesta coordinada de la comunidad internacional.
4.  **Reacciones de los países de la región:** Es clave observar las medidas que tomen los países de Latinoamérica y el Caribe para mitigar los riesgos y aprovechar las oportunidades generadas por el nuevo contexto global.

</div>

 """, unsafe_allow_html=True)



with st.expander("Tercera semana de mayo de 2025", expanded=False):
    
    st.markdown("""

<div class="news-text">
        <div class="div-news-description">
        
# Tensiones comerciales y reconfiguración geopolítica: América Latina en la mira de EE.UU. y China

*Semana del reporte: 18 de mayo de 2025*

## Diagnóstico

Durante la semana del 18 de mayo de 2025, el panorama noticioso se centró en las tensiones comerciales impulsadas por la administración Trump y la creciente influencia de China en América Latina y el mundo. Los hechos más relevantes incluyen la evaluación de Estados Unidos de acuerdos arancelarios regionales, la reacción de Trump ante el aumento de precios de Walmart debido a los aranceles, y la intensificación de la competencia entre China y Estados Unidos por el liderazgo global, especialmente en América Latina.

**Hechos Noticiosos Clave y su Evolución:**

1.  **Evaluación de Acuerdos Arancelarios Regionales por EE.UU.:** El secretario del Tesoro de EE. UU., Scott Bessent, confirmó que el Gobierno evalúa acuerdos arancelarios regionales como parte de su estrategia de reforma comercial, incluyendo a América Central. Guatemala busca ser incluida en estos acuerdos para revertir el arancel del 10% impuesto desde abril. Se espera una reunión clave en Washington D.C. el 27 de mayo para discutir posibles ajustes arancelarios y la inclusión de Guatemala en un acuerdo regional. Esta noticia se repite varias veces a lo largo de la semana, lo que indica su importancia.
2.  **Reacción de Trump ante el Aumento de Precios de Walmart:** Trump arremetió contra Walmart por subir los precios debido a los aranceles impuestos a China, acusando a la cadena de usar las tarifas como excusa. Trump exigió que Walmart y China absorbieran el costo de los aranceles en lugar de trasladarlo a los consumidores. El secretario del Tesoro de EE. UU., Scott Bessent, dialogó con el CEO de Walmart, Doug McMillon, sobre el impacto de los aranceles. Esta disputa destaca la presión sobre las empresas estadounidenses y el posible impacto inflacionario de las políticas comerciales de Trump.
3.  **Foro Celac-China y la Influencia China en América Latina:** El Foro Celac-China es una muestra de los avances de la influencia de China en el continente americano. China compite con Norteamérica, sin interferir en asuntos políticos, enfocándose en comercio e inversión. Xi Jinping destacó la importancia de la cooperación, la inversión y la Ruta de la Seda en Latinoamérica que asciende a los 500.000 millones de dólares, comprometiéndose a importar más productos de calidad de la región y animar a sus empresas a aumentar las inversiones en América Latina, la implementación de 100 proyectos de cooperación en 3 años, y anunció 20 medidas para apoyar el desarrollo de América Latina. Estados Unidos observa con preocupación la presencia económica, diplomática y tecnológica de China a través de la Celac y advierte a los gobiernos del continente los riesgos de endeudarse con China.
4.  **Tregua Comercial EE.UU.-China y sus Consecuencias:** Se anuncia una tregua de 90 días en la guerra comercial entre EE.UU. y China, con una reducción de aranceles de 145% a 30% por parte de EE.UU. y de 125% a 10% por parte de China. A pesar de la tregua, analistas advierten que la incertidumbre persiste y que los efectos inflacionarios podrían continuar. Algunos sectores, como el de vehículos eléctricos, siguen afectados por los aranceles.
5.  **Acercamiento de China a los Aliados de EE.UU.:** China está cortejando a los aliados de Estados Unidos, como la Unión Europea, Japón, Corea del Sur y países de América Latina, ofreciendo cooperación y ocupando espacios dejados por Estados Unidos. China ha intensificado su presencia en el Indo-Pacífico y ha intentado posicionarse como defensor del multilateralismo.

**Movimientos de los Principales Actores del Comercio Global:**

*   **China:** Fortalecimiento de lazos con América Latina a través del Foro Celac-China, ofreciendo inversiones y cooperación. Expansión de su influencia en el Indo-Pacífico y promoción del multilateralismo.
*   **Estados Unidos:** Evaluación de acuerdos arancelarios regionales, imposición de aranceles a China y otros países, y negociaciones comerciales bilaterales.
*   **Unión Europea:** Preocupación por la posible inundación de productos chinos en su mercado debido a la guerra comercial entre EE.UU. y China. Búsqueda de acuerdos comerciales con otros socios, incluyendo India y Mercosur.

**Acercamientos e Intercambios de Países de la Región:**

*   Guatemala busca ser incluida en los acuerdos arancelarios regionales de EE.UU.
*   Honduras sigue trabajando para lograr un Tratado de Libre Comercio (TLC) con China.
*   Ecuador recibe luz verde para iniciar negociaciones comerciales con EE. UU.
*   El canciller panameño afirma que varios países reconocen la soberanía de Panamá sobre el Canal.
*   Lula da Silva de Brasil, Gustavo Petro de Colombia y Gabriel Boric de Chile se reunieron con Xi Jinping en Beijing.

## Tendencias

1.  **Regionalización del Comercio:** EE.UU. está considerando acuerdos arancelarios regionales, lo que podría fragmentar el comercio global en bloques más pequeños.
2.  **Competencia Geopolítica:** China y EE.UU. compiten por influencia en América Latina, ofreciendo diferentes modelos de desarrollo y cooperación.
3.  **Incertidumbre Comercial:** Las políticas comerciales de Trump generan incertidumbre y volatilidad en los mercados, afectando las decisiones de inversión y consumo.
4.  **Presión Inflacionaria:** Los aranceles podrían aumentar los precios al consumidor, especialmente en productos importados de China.
5.  **Diversificación de Mercados:** Los países de la región buscan diversificar sus mercados y reducir la dependencia de EE.UU. y China.

## Implicaciones Estratégicas

*   **Para la Región:** América Latina enfrenta el desafío de equilibrar las relaciones con EE.UU. y China, aprovechando las oportunidades de inversión y comercio sin comprometer su soberanía. La integración regional se vuelve crucial para fortalecer la posición negociadora de los países latinoamericanos.
*   **Para Estados Unidos:** La política comercial de Trump podría dañar la credibilidad de EE.UU. como socio comercial confiable y abrir espacio para que China expanda su influencia en la región.
*   **Para el Mundo:** La guerra comercial entre EE.UU. y China podría fragmentar el sistema de comercio global y generar inestabilidad económica.

## Factores Clave a Vigilar

1.  **Negociaciones Arancelarias:** El resultado de las negociaciones entre EE.UU. y China, así como los acuerdos arancelarios regionales que EE.UU. pueda establecer.
2.  **Reacciones de los Países de la Región:** La respuesta de los países latinoamericanos a las políticas comerciales de EE.UU. y China, incluyendo la búsqueda de nuevos socios comerciales y la profundización de la integración regional.
3.  **Impacto en los Precios al Consumidor:** La evolución de los precios al consumidor en EE.UU. y otros países debido a los aranceles.
4.  **Inversión China en la Región:** El aumento de la inversión china en América Latina y su impacto en el desarrollo económico de la región.
</div>

 """, unsafe_allow_html=True)


with st.expander("Segunda semana de mayo de 2025", expanded=False):
    st.markdown("""	
            
    <div class="news-text">
        <div class="div-news-description">
            
# Tensiones comerciales y repercusiones regionales: Implicancias del nuevo proteccionismo estadounidense

*Semana del reporte: 11 de mayo de 2025*

## Diagnóstico

Durante la semana del 11 de mayo de 2025, el panorama noticioso estuvo dominado por las tensiones comerciales impulsadas por la administración Trump, especialmente en lo que respecta a la relación entre Estados Unidos y China. A pesar de los anuncios de "progresos sustanciales" y la promesa de un "reinicio total" en las relaciones comerciales, la realidad es que la incertidumbre persiste y las medidas proteccionistas de Trump están generando ondas expansivas en la economía global, con implicaciones particulares para Latinoamérica y el Caribe.

*   **Negociaciones EEUU-China:** La semana estuvo marcada por la reanudación de las negociaciones comerciales entre Estados Unidos y China en Suiza (11 de mayo). Si bien ambas partes expresaron optimismo y hablaron de "progresos sustanciales", los detalles concretos del acuerdo siguen siendo vagos. Trump incluso sugirió una posible reducción de aranceles al 80%, aunque su equipo aclaró que esto dependerá de concesiones por parte de China. La cautela china se reflejó en la declaración de su agencia oficial de noticias, que insistió en que rechazarán cualquier propuesta que comprometa sus principios fundamentales.
*   **Impacto en el comercio EEUU-China:** Las noticias revelan que la guerra comercial ya está afectando el flujo de bienes entre ambas potencias. Las exportaciones chinas a Estados Unidos cayeron un 21% en abril, mientras que las exportaciones estadounidenses a China también se vieron afectadas. Este estancamiento comercial está generando preocupación en los mercados financieros y entre las pequeñas empresas estadounidenses que dependen de las importaciones chinas.
*   **Reacciones en Latinoamérica y el Caribe:** Ante este escenario, los países de la región están evaluando su autonomía geopolítica y buscando diversificar sus relaciones comerciales. El IV Foro Ministerial China-Celac, que se celebrará el 13 de mayo en Pekín, se presenta como una oportunidad clave para definir el rumbo político de la región y consolidar una plataforma de cooperación multilateral que no esté subordinada a las potencias tradicionales. Sin embargo, la región no acude al foro con una voz unificada, ya que algunos países, como Argentina, han dado un giro drástico en favor de Washington, mientras que otros, como Brasil y Chile, buscan una relación estratégica con China sin romper puentes con Occidente.
*   **Impacto en otros países:** La guerra comercial también está afectando a otros países, como Canadá, donde el aumento del desempleo se atribuye a las políticas arancelarias de Trump. En Europa, la Unión Europea está preparando medidas de represalia contra Estados Unidos en caso de que las negociaciones comerciales fracasen.
*   **Acuerdo comercial EEUU-Reino Unido:** En medio de este panorama de tensiones comerciales, Trump anunció un acuerdo comercial con el Reino Unido (11 de mayo), que incluye cuotas que protegen las exportaciones británicas de acero y automóviles, además de una reducción arancelaria general. Este acuerdo, si bien es un logro para la administración Trump, también genera interrogantes sobre el futuro de las relaciones comerciales entre Estados Unidos y la Unión Europea.
*   **Cierre de fronteras a importaciones de ganado:** Estados Unidos suspenderá las exportaciones mexicanas de ganado bovino en pie durante 15 días para revisar la estrategia conjunta en el combate del gusano barrenador (11 de mayo).

## Tendencias

1.  **Regionalización del comercio:** Ante la incertidumbre generada por las políticas proteccionistas de Trump, los países de Latinoamérica y el Caribe están buscando fortalecer sus lazos comerciales entre sí y con otras regiones del mundo, como Asia y Europa.
2.  **Aumento de la influencia china:** China se está posicionando como un socio estratégico para Latinoamérica y el Caribe, ofreciendo inversiones en infraestructura, tecnología y energía limpia.
3.  **Debilitamiento del multilateralismo:** La administración Trump está erosionando el multilateralismo y el libre comercio, lo que genera un clima de creciente incertidumbre económica internacional.
4.  **Reestructuración de las cadenas de suministro:** Las empresas están buscando diversificar sus cadenas de suministro para reducir su dependencia de China y otros países afectados por las políticas arancelarias de Trump.
5.  **Aumento de la volatilidad en los mercados financieros:** La incertidumbre generada por las tensiones comerciales está provocando una mayor volatilidad en los mercados financieros, lo que dificulta la toma de decisiones de inversión.

## Implicaciones estratégicas

*   **Para la región:**
    *   **Corto plazo:** Aumento de la incertidumbre económica y la volatilidad en los mercados financieros.
    *   **Mediano plazo:** Necesidad de diversificar las relaciones comerciales y fortalecer la integración regional.
    *   **Largo plazo:** Oportunidad de construir una relación más equilibrada y autónoma con China y Estados Unidos.
*   **Para Estados Unidos:**
    *   **Corto plazo:** Posible desaceleración del crecimiento económico y aumento de la inflación.
    *   **Mediano plazo:** Riesgo de perder influencia en la economía global y de erosionar sus alianzas tradicionales.
    *   **Largo plazo:** Incertidumbre sobre el futuro del liderazgo económico estadounidense en un mundo multipolar.
*   **Para el mundo:**
    *   **Corto plazo:** Aumento de las tensiones geopolíticas y riesgo de una guerra comercial a gran escala.
    *   **Mediano plazo:** Reconfiguración del orden económico global y surgimiento de nuevos bloques comerciales.
    *   **Largo plazo:** Incertidumbre sobre el futuro del sistema multilateral y la gobernanza global.

## Factores clave a vigilar

*   **Evolución de las negociaciones comerciales entre Estados Unidos y China:** Los resultados de estas negociaciones tendrán un impacto significativo en la economía global y en las relaciones geopolíticas.
*   **Reacciones de los países de Latinoamérica y el Caribe:** Es clave observar cómo los países de la región están respondiendo a las políticas proteccionistas de Trump y cómo están buscando diversificar sus relaciones comerciales. En ese mismo sentido será clave analizar los resultados de la cumbre CELAC China a efectuarse durante la semana.
*   **Impacto de las políticas de Trump en la economía estadounidense:** Es importante monitorear los indicadores económicos de Estados Unidos para evaluar el impacto de las políticas de Trump en el crecimiento, la inflación y el empleo.
*   **Evolución del sistema multilateral:** Es fundamental observar cómo la Organización Mundial del Comercio (OMC) y otras instituciones multilaterales están respondiendo a los desafíos planteados por el nuevo proteccionismo estadounidense.

</div>

 """, unsafe_allow_html=True)


with st.expander("Primera semana de mayo de 2025", expanded=False):
    st.markdown("""	
            
    <div class="news-text">
        <div class="div-news-description">
            
# Tensiones comerciales y repercusiones regionales: Implicancias del nuevo proteccionismo estadounidense

*Reporte del 28 de abril al 04 de mayo de 2025* 

## Diagnóstico

Durante la primera semana de mayo de 2025, las noticias estuvieron marcadas por la intensificación de las tensiones comerciales a nivel global, principalmente impulsadas por las políticas arancelarias de la administración Trump. Se observó una clara preocupación en diversos sectores económicos y regiones, especialmente en Latinoamérica y el Caribe, ante el impacto de estas medidas.

*   **Estados Unidos y China:** La guerra comercial entre estas dos potencias continuó siendo un tema central. Se reportaron señales contradictorias, con China mostrando disposición a negociar, pero exigiendo el retiro previo de los aranceles estadounidenses. Mientras tanto, Estados Unidos mantenía una postura firme, generando incertidumbre y volatilidad en los mercados.
*   **Impacto en Latinoamérica y el Caribe:** Varios artículos mencionaron el impacto negativo de las políticas de Trump en la región, con la Cepal recortando las previsiones de crecimiento para varios países. Se destacó la vulnerabilidad de las economías latinoamericanas ante las decisiones unilaterales de Estados Unidos y la necesidad de diversificar mercados y fortalecer la integración regional.
*   **Reacciones y medidas en la región:** Algunos países, como México, buscan acuerdos bilaterales con Estados Unidos para mitigar el impacto de los aranceles. Otros, como Uruguay, reportan mejoras en sus exportaciones a otros mercados como China y la Unión Europea. Los países del Mercosur también discutieron medidas para flexibilizar el comercio interno y enfrentar la situación.
*   **Impacto en otros países y sectores:** Se observaron efectos negativos en diversos sectores a nivel global, como la industria automotriz, la tecnología y el transporte marítimo. Empresas como Apple y General Motors advirtieron sobre el impacto de los aranceles en sus costos y ganancias.
*   **Reacciones de otros actores globales:** La Unión Europea continúa expresando su preocupación por las políticas de Trump y busca alternativas para fortalecer su autonomía comercial. China, por su parte, sigue promoviendo la cooperación con otros países del Sur Global y la búsqueda de alternativas al sistema financiero dominado por el dólar.

**Algunos hecho noticiosos destacados:**

*   Se reportó la ralentización del puerto de Los Ángeles debido a la guerra comercial, evidenciando el impacto en la economía estadounidense. [Ver noticia](https://www.elfinancierocr.com/internacionales/los-angeles-el-mayor-puerto-de-ee-uu-baja-el-ritmo/GNNEJ3EFTFFSHGZRGQQJR6BQUY/story/)
*   La embajadora de China en Costa Rica acusó a Estados Unidos de utilizar la cancelación de visas como presión política, mostrando la escalada de tensiones diplomáticas. [Ver noticia]( https://www.nacion.com/politica/embajadora-de-china-en-costa-rica-acusa-a-estados/5I3PYYDKKFCXBJ66ZBUGHNQ4QY/story/)
*   El CEO de Apple, Tim Cook, estimó que los aranceles de Trump le costarán a Apple 900 millones de dólares este trimestre, lo que llevó a la empresa a trasladar la producción de iPhones a la India. [Ver noticia](https://www.thestar.com.my/aseanplus/aseanplus-news/2025/05/03/apple-estimates-tariffs-will-add-us900-million-to-costs-in-june-quarter-business-in-vietnam-to-be-affected#goog_rewarded)
*   Se destacó la creciente influencia de China en América Latina, con inversiones que superan a las de Estados Unidos en algunos sectores. [Ver noticia](https://www.elnacional.com/opinion/la-influencia-de-china-en-america-latina/)
*   Warren Buffett anunció su retiro y advirtió que la guerra comercial perjudicará a Estados Unidos, generando preocupación en los mercados. [Ver noticia](https://www.ijpr.org/npr-news/2025-05-03/warren-buffett-announces-his-retirement-and-warns-the-trade-war-will-hurt-america)
*   El gobernador de California afirmó que el estado continuará abierto al comercio con China, desafiando la política arancelaria del gobierno federal. [Ver noticia](http://www.spanish.xinhuanet.com/20250504/b46fae9a6c3f42fe92511280022184da/c.html)
*   Se conoció la decisión de China de evaluar las propuestas de negociación de Estados Unidos, pero exigiendo concesiones previas. [Ver noticia](https://www.jamaicaobserver.com/2025/05/04/things-stand-us-china-trade-war/)

## Tendencias

1.  **Aumento del proteccionismo:** La administración Trump continúa implementando políticas proteccionistas, generando tensiones comerciales y disrupciones en las cadenas de suministro globales.
2.  **Reconfiguración de alianzas:** Los países de la región buscan diversificar sus socios comerciales y fortalecer la integración regional para reducir su dependencia de Estados Unidos.
3.  **Impacto en la economía global:** Las tensiones comerciales y la incertidumbre política están afectando el crecimiento económico mundial, generando volatilidad en los mercados financieros y aumentando el riesgo de recesión.

## Implicaciones estratégicas

*   **Para la región:** En el corto plazo, la región enfrenta desafíos económicos y sociales debido a la incertidumbre comercial y las políticas migratorias de Estados Unidos. A mediano y largo plazo, la región podría beneficiarse de la diversificación de sus socios comerciales y el fortalecimiento de la integración regional, lo que aumentaría su resiliencia ante futuras crisis.
*   **Para Estados Unidos:** En el corto plazo, las políticas de Trump podrían generar beneficios para algunos sectores de la economía estadounidense, como la industria manufacturera. Sin embargo, a mediano y largo plazo, el proteccionismo podría perjudicar la competitividad de Estados Unidos y su liderazgo en el mundo.
*   **Para el mundo:** La intensificación de las tensiones comerciales y la erosión del multilateralismo podrían generar un mundo más fragmentado y conflictivo, con un mayor riesgo de crisis económicas y políticas.

## Factores clave a vigilar

*   La evolución de las negociaciones comerciales entre Estados Unidos y China.
*   Las medidas que tomen los países de la región para diversificar sus socios comerciales y fortalecer la integración regional.
*   El impacto de las políticas de Trump en la economía estadounidense y mundial.
            </div>

 """, unsafe_allow_html=True)    
    

with st.expander("Cuarta semana de abril de 2025", expanded=False):
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
*   **Acuerdos bilaterales y regionales:** Es importante monitorear los acuerdos que EE.UU. logre negociar con otros países, así como los esfuerzos de integración regional en América Latina y otras partes del mundo.
*   **Indicadores económicos clave:** Prestar atención a los datos de crecimiento, inflación, desempleo, y balanza comercial en EE.UU., China, y los principales países de América Latina y el Caribe.
            </div>

 """, unsafe_allow_html=True)
    
    

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
