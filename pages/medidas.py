# Urls a seguir: 
# https://www.tradecomplianceresourcehub.com/2025/07/03/trump-2-0-tariff-tracker/
# https://www.ft.com/trump-tariffs (paywall)
# https://taxfoundation.org/research/all/federal/trump-tariffs-trade-war/#timeline

import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

# Configuración de la página con estilo The Economist
st.set_page_config(
    page_title="Aranceles de Trump",
    page_icon="📊",
    layout="wide"
)

# Ocultar la sidebar con CSS
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none !important;
        }
        [data-testid="collapsedControl"] {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

if st.button("Ir a Inicio"):
    st.switch_page("app.py")

# Aplicar estilo The Economist
st.markdown("""
<style>
    .main {
        background-color: #ffffff;
        color: #121212;
        font-family: 'Georgia', serif;
    }
    h1, h2, h3, h4 {
        font-family: 'Georgia', serif;
        font-weight: bold;
        color: #121212;
    }
    .stDataFrame {
        font-family: 'Georgia', serif;
    }
    .st-bc {
        background-color: #ffffff;
    }
    footer {
        font-family: 'Georgia', serif;
        font-size: 12px;
        color: #666666;
    }
</style>
""", unsafe_allow_html=True)

# Título y descripción con estilo The Economist
st.markdown("<h1 style='font-family: Georgia; font-weight: bold; margin-bottom: 5px'>Guerra Comercial: Cronología de Aranceles Trump</h1>", unsafe_allow_html=True)

st.markdown("""
### Cronología de medidas arancelarias de EE.UU. – 2025

- **7 ago 2025 – EE. UU.**: Entran en vigor los aranceles globales de EE. UU.  
- **6 ago 2025 – EE. UU.**: Donald Trump anuncia un arancel del **100 %** sobre los chips no fabricados en EE. UU.  
- **6 ago 2025 – EE. UU.**: EE. UU. aumentará los aranceles a la India debido a sus compras de petróleo ruso.  
- **31 jul 2025 – EE. UU.**: Donald Trump impone nuevos aranceles a decenas de socios comerciales, vigentes desde el 7 de agosto.  
- **30 jul 2025 – EE. UU.**: Donald Trump anuncia que las importaciones de India estarán sujetas a un **arancel del 25 %** a partir del 1 de agosto.  
- **27 jul 2025 – EE. UU./UE**: EE. UU. y la UE alcanzan un acuerdo arancelario que aplicará un arancel estadounidense del **15 %** a la mayoría de las importaciones del bloque.  
- **22 jul 2025 – EE. UU./Japón**: EE. UU. acuerda un pacto comercial con Japón que impondrá aranceles del **15 %** a los bienes importados a EE. UU.  
- **16 de Julio de 2025**: Actualización de las estimaciones de ingresos y económicas para los aranceles recíprocos y una actualización sobre los aranceles de represalia de la UE.  
- **Julio de 2025**: Actualización de las estimaciones de ingresos y económicas para los aranceles recíprocos y los aranceles del cobre de la Sección 232.  
- **Julio de 2025**: Incluye una actualización del cronograma sobre la implementación de los aranceles recíprocos y estimaciones actualizadas de ingresos y económicas para esos aranceles.  
- **Julio 15, 2025**: La UE publica una lista de $84 mil millones en bienes estadounidenses que enfrentarían aranceles de represalia si no se llega a un acuerdo antes del 1 de agosto.  
- **Julio 14, 2025**: El presidente Trump amenaza a Rusia con aranceles del 100%.  
- **Julio 12, 2025**: El presidente Trump anuncia que los aranceles recíprocos para la UE y México se fijarán en un 30% para el 1 de agosto. Esto es inferior al arancel recíproco anterior para la UE anunciado en mayo, que se había fijado en un 50%.  
- **Julio 10, 2025**: El presidente Trump amenaza a Canadá con un arancel del 35% que entraría en vigor el 1 de agosto.  
- **Julio 9, 2025**: La administración Trump envía cartas a 7 países más y amenaza a Brasil con un arancel del 50% que entraría en vigor el 1 de agosto.  
- **Julio 8, 2025**: El presidente Trump anuncia que impondrá un arancel del 50% al cobre el 1 de agosto. También amenaza con un arancel del 200% a los productos farmacéuticos.  
- **Julio 7, 2025**: El presidente anuncia que los aranceles recíprocos se retrasarían hasta el 1 de agosto. Envió cartas a 14 países, incluidos Japón y Corea del Sur, indicando los aranceles que enfrentarían si no presentaban un acuerdo comercial con los EE. UU. a fines de julio. También amenazó a los "países alineados con los BRICS" con un arancel adicional del 10%.

- **Julio 2, 2025**: El presidente anunció que Estados Unidos llegó a un acuerdo con Vietnam. Se mantendrá un arancel base del **20%** sobre las importaciones de Vietnam, mientras que se impondrá un arancel del **40%** sobre cualquier transbordo. No se ha programado una fecha de entrada en vigor para el acuerdo.

- **Junio 30, 2025**: Entró en vigor el acuerdo entre Estados Unidos y el Reino Unido. El arancel del **25%** sobre las importaciones de acero y aluminio del Reino Unido permanecerá en vigor.

- **Junio 11, 2025**: Trump anunció un acuerdo comercial con China que mantendría los aranceles actuales del **20%** sobre el *fentanilo* y del **10%** *recíprocos*, pausando los aranceles más altos durante 90 días.

- **Junio 10, 2025**: El Tribunal de Apelaciones para el Circuito Federal de Washington, DC, permitió que los aranceles IEEPA de Trump permanezcan en vigor hasta que se emita un fallo definitivo. Audiencia programada para el **31 de julio de 2025**.

- **Mayo 30, 2025**: Trump anunció que los aranceles sobre acero y aluminio se duplicarían al **50%** a partir del **4 de junio**, excepto para el Reino Unido.

- **Mayo 29, 2025**: Un segundo tribunal federal falló en contra de los aranceles IEEPA.

- **Mayo 28, 2025**: Un panel del Tribunal Internacional de Comercio dictaminó por unanimidad que los aranceles IEEPA eran **ilegales**. La administración Trump apeló. El fallo dio al presidente **10 días** para comenzar a detener el cobro de los aranceles IEEPA. No afecta los aranceles de las **Secciones 232 y 301**. Los importadores podrían recibir compensación retroactiva.

- **Mayo 25, 2025**: Se anunció que estos aranceles entrarían en vigor el **9 de julio**.

- **Mayo 23, 2025**: Trump anunció un arancel recíproco del **50%** a la UE desde el **1 de junio**.

- **Mayo 12, 2025**: El Secretario del Tesoro anunció una pausa de **90 días** en las escaladas con China, reduciendo el arancel del **125% al 10%**.

- **Mayo 8, 2025**: Se anunciaron los lineamientos de un acuerdo con el Reino Unido que mantendría el arancel "recíproco" del **10%**, pero reduciría el arancel del **25% al 10%** en las primeras **100,000 importaciones** de automóviles, y eliminaría los aranceles del 25% sobre acero y aluminio.
""")

st.markdown("---")


st.markdown("<h2 style='font-family: Georgia; font-weight: bold; margin-bottom: 5px'>Tabla de Aranceles de los primeros 60 días de la guerra comercial (hasta 8 de mayo de 2025)</h1>", unsafe_allow_html=True)
# Función para convertir fechas textuales a objetos datetime
def parse_spanish_date(date_string):
    """
    Convierte una fecha en español como '4 de marzo de 2025' a un objeto datetime.
    Maneja espacios adicionales, caracteres invisibles y errores de formato.
    """
    # Diccionario de meses en español
    months_dict = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
        'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }
    
    # Limpiar espacios adicionales y caracteres invisibles
    date_string = date_string.strip().replace('\u200b', '').replace('\xa0', ' ')
    
    # Validar que la fecha no esté vacía
    if not date_string:
        raise ValueError("La fecha está vacía o contiene solo caracteres invisibles.")
    
    # Dividir la fecha en partes
    
    parts = date_string.split()
    
    # Validar el formato esperado: "día de mes de año"
    if len(parts) == 5 and parts[1].lower() == 'de' and parts[4].isdigit():
        try:
            # Extraer día, mes y año
            day = int(parts[0])
            month = months_dict.get(parts[2].lower())
            year = int(parts[4])
            
            # Validar que el mes sea válido
            if month is None:
                raise ValueError(f"Mes no reconocido: {parts[2]}")
            
            # Crear y devolver el objeto datetime
            return datetime(year, month, day)
        except Exception as e:
            raise ValueError(f"Error al procesar la fecha: '{date_string}'. Detalles: {e}")
    else:
        raise ValueError(f"Formato de fecha no reconocido: '{date_string}'")

# Leer CSV con medidas arancelarias
df = pd.read_csv('aranceles.csv') #, encoding='utf-8')

# Agregar columnas de fecha parseadas para ordenamiento
df['Anuncio_fecha'] = df['Fecha de Anuncio'].apply(parse_spanish_date)


# Ordenar por fecha de entrada en vigor
df = df.sort_values(by='Anuncio_fecha', ascending=False)

# Crear versión para mostrar (sin columnas de fecha parseadas y sin índice)
display_df = df.drop(columns=['Anuncio_fecha'])

# Crear tabla Plotly para más control sobre el estilo y formato
fig = go.Figure(data=[go.Table(
    header=dict(
        values=list(display_df.columns),
        fill_color='#121212',
        font=dict(color='white', size=13, family='Georgia'),
        align='left',
        height=40
    ),
    cells=dict(
        values=[display_df[col] for col in display_df.columns],
        fill_color=[['#e6e6e6' if i % 2 == 0 else 'white' for i in range(len(display_df))]],
        font=dict(color= '#121212', 
                  size=14, family='Georgia'),
        align='left',
        height=35
    )
)])

# Ajustar diseño de la tabla
fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    height=700,
    width=1200
)

# Mostrar tabla
st.plotly_chart(fig, use_container_width=True)

# Leyenda con estilo The Economist
st.markdown("""
<div style='background-color: #f8f8f8; padding: 15px; border-left: 5px solid #121212; margin-top: 20px; font-family: Georgia;'>
<strong>Leyenda:</strong><br>
🔴 <span style='color: #990000; font-weight: bold;'>EE.UU. impone</span>: Aranceles impuestos por Estados Unidos a otros países<br>
🔵 <span style='color: #000099; font-weight: bold;'>Respuesta a EE.UU.</span>: Contramedidas impuestas por otros países en respuesta a los aranceles de EE.UU.
</div>
""", unsafe_allow_html=True)

# Nota metodológica con estilo The Economist
st.markdown("""
<div style='font-family: Georgia; font-size: 12px; color: #666666; margin-top: 30px;'>
<strong>Metodología:</strong> Los datos presentados han sido compilados a partir de información de Yahoo Finance publicada el 2 de abril de 2025 y actualizados desde ese sitio, Financial Times y el sitio oficial de la casa blanca. 

</div>
""", unsafe_allow_html=True)

# Firma de The Economist
st.markdown("""
<div style='font-family: Georgia; font-style: italic; text-align: right; margin-top: 40px; color: #666666;'>
© 2025 Lab.
</div>
""", unsafe_allow_html=True)


