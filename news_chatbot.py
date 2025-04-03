# news_chatbot.py
import streamlit as st
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

# Estilos CSS personalizados
CSS = """
<style>
    .main-header {
        color: #003366;
        text-align: center;
        margin-bottom: 20px;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .chat-message.user {
        background-color: #e6f7ff;
        border-left: 5px solid #1890ff;
    }
    .chat-message.bot {
        background-color: #f6f6f6;
        border-left: 5px solid #003366;
    }
    .source-section {
        margin-top: 1rem;
        padding: 0.8rem;
        background-color: #f0f0f0;
        border-radius: 0.3rem;
        font-size: 0.9rem;
    }
</style>
"""

# Función para configurar Gemini
def setup_genai(api_key=None):
    if api_key is None:
        # Intentar cargar de variables de entorno
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        
        # Si aún no se encuentra, intentar con secretos de Streamlit
        if not api_key:
            try:
                api_key = st.secrets.get("GEMINI_API_KEY", None)
            except:
                pass
    
    if not api_key:
        st.error("No se encontró la clave API de Gemini. Por favor proporciona una clave API válida.")
        return None
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.0-flash-lite")

# Función para generar respuestas
def generate_response(model, user_query, news_data):
    if not model or not news_data:
        return "Lo siento, no puedo procesar tu pregunta en este momento."
    
    prompt = """
    INSTRUCCIONES:
    Eres un experimentado analista de noticias de la Comisión Económica y Social para América Latina y El Caribe de las Naciones Unidas (CEPAL). Tu función es proporcionar información precisa basada en la base de datos de noticias que tienes como contexto.

    CONTEXTO:
    Tienes acceso a una base de datos de noticias en formato JSON con la siguiente estructura:
    - date_process: fecha de publicación
    - title: titular de la noticia
    - content: contenido completo de la noticia
    - resumen: resumen de la noticia (no siempre disponible)
    - url: enlace a la fuente original

    COMPORTAMIENTO:
    1. Responde de manera clara, concisa y objetiva a las preguntas del usuario.
    2. Utiliza ÚNICAMENTE la información contenida en el contexto proporcionado.
    3. Si no tienes suficiente información en el contexto para responder, indícalo claramente.
    4. No inventes información ni cites fuentes que no estén en el contexto.
    5. Enfoca tus respuestas en hechos, evitando opiniones personales.
    6. Estructura tus respuestas de manera organizada, utilizando párrafos cuando sea necesario.

    FORMATO DE RESPUESTA:
    - Responde la pregunta del usuario de forma directa y completa.
    - Si es relevante, menciona la fecha de la información proporcionada.
    - Al final de cada respuesta, incluye una sección titulada "FUENTES" con las 1-3 fuentes más relevantes utilizadas, en el siguiente formato:
        
    FUENTES:
    1. "[título de la noticia]" - [url]
    2. "[título de la noticia]" - [url]
    3. "[título de la noticia]" - [url]
    
    PREGUNTA DEL USUARIO:
    {query}
    """
    
    # Combinamos el prompt con el contexto JSON
    prompt_with_context = prompt.format(query=user_query)
    
    try:
        response = model.generate_content(
            [prompt_with_context, json.dumps(news_data, ensure_ascii=False)],
            generation_config=genai.GenerationConfig(
                max_output_tokens=2000,
                temperature=0,
            )
        )
        return response.text
    except Exception as e:
        st.error(f"Error al generar respuesta: {e}")
        return f"Lo siento, ocurrió un error al procesar tu pregunta: {str(e)}"

# Función principal del chatbot que puedes llamar desde tu aplicación principal
def news_chatbot_component(api_key=None, news_data=None, title="Chatbot de Noticias CEPAL", height=600):
    """
    Componente de chatbot de noticias que se puede integrar en cualquier aplicación Streamlit.
    
    Parámetros:
    - api_key (str): Clave API de Gemini (opcional si está en variables de entorno)
    - news_data (list/dict): Datos de noticias en formato JSON (requerido)
    - title (str): Título del componente de chatbot
    - height (int): Altura del contenedor del chat en píxeles
    
    Retorna:
    - None
    """
    # Aplicar estilos CSS
    st.markdown(CSS, unsafe_allow_html=True)
    
    # Título del componente
    #st.markdown(f"<h2 class='main-header'>📰 {title}</h2>", unsafe_allow_html=True)
    
    # Verificar si hay datos de noticias
    if news_data is None:
        # Usar datos de ejemplo integrados (puedes reemplazar esto con tus propios datos)
        news_data = [
            {
                "date_process": "2025-03-28",
                "title": "CEPAL proyecta crecimiento económico de 1.9% para América Latina en 2025",
                "content": "La Comisión Económica para América Latina y el Caribe (CEPAL) proyectó hoy un crecimiento de 1.9% para las economías de la región en 2025, cifra superior al 1.7% previsto anteriormente. Según el informe, la recuperación estará impulsada por un mejor desempeño de Brasil y México, así como por políticas fiscales más expansivas en varios países de la región.",
                "resumen": "CEPAL mejora proyección de crecimiento para América Latina a 1.9% para 2025.",
                "url": "https://www.cepal.org/es/comunicados/cepal-proyecta-crecimiento-19-2025"
            },
            {
                "date_process": "2025-03-25",
                "title": "Aumenta la inseguridad alimentaria en Centroamérica, alerta CEPAL",
                "content": "Un nuevo estudio de la CEPAL señala que la inseguridad alimentaria en Centroamérica aumentó un 8% en el último año, afectando a más de 18 millones de personas. El fenómeno se atribuye principalmente a los efectos del cambio climático, que ha provocado sequías prolongadas e inundaciones que han afectado la producción agrícola en Guatemala, Honduras, El Salvador y Nicaragua.",
                "url": "https://www.cepal.org/es/comunicados/aumenta-inseguridad-alimentaria-centroamerica"
            },
            {
                "date_process": "2025-03-30",
                "title": "CEPAL y UNICEF firman acuerdo para combatir pobreza infantil en la región",
                "content": "La CEPAL y UNICEF firmaron hoy un acuerdo de cooperación para implementar programas conjuntos destinados a reducir la pobreza infantil en América Latina y el Caribe. El convenio contempla inversiones por USD 45 millones durante los próximos tres años, con énfasis en programas de protección social, educación y salud en comunidades vulnerables.",
                "resumen": "CEPAL y UNICEF firman acuerdo de cooperación por USD 45 millones para reducir pobreza infantil.",
                "url": "https://www.cepal.org/es/acuerdos/cepal-unicef-firman-acuerdo-combatir-pobreza-infantil"
            }
        ]
    
    # Contenedor con altura fija para el chat
    chat_container = st.container(height=height)
    
    # Inicializar modelo de Gemini
    model = setup_genai(api_key)
    
    # Inicializar historial de chat en la sesión si no existe
    if "news_chat_messages" not in st.session_state:
        st.session_state.news_chat_messages = [
            {"role": "assistant", "content": "¡Hola! Soy tu asistente de noticias de CEPAL. ¿Qué información necesitas sobre América Latina y el Caribe?"}
        ]
    
    # Mostrar mensajes del chat
    with chat_container:
        for message in st.session_state.news_chat_messages:
            role_class = "user" if message["role"] == "user" else "bot"
            st.markdown(f'<div class="chat-message {role_class}"><div>{message["content"]}</div></div>', unsafe_allow_html=True)
    
    # Input para nuevos mensajes
    if user_query := st.chat_input("Escribe tu pregunta aquí"):
        # Añadir mensaje del usuario al historial
        st.session_state.news_chat_messages.append({"role": "user", "content": user_query})
        
        # Generar respuesta
        with st.spinner("Analizando noticias..."):
            response = generate_response(model, user_query, news_data)
        
        # Añadir respuesta al historial
        st.session_state.news_chat_messages.append({"role": "assistant", "content": response})
        
        # Recargar para mostrar nuevos mensajes
        st.rerun()

# Si este archivo se ejecuta directamente, mostrar un ejemplo
if __name__ == "__main__":
    st.set_page_config(page_title="Demo Chatbot de Noticias", layout="wide")
    
    # Ejemplo de datos de noticias (reemplaza esto con tus propios datos)
    example_news = [
        {
            "date_process": "2025-03-28",
            "title": "CEPAL proyecta crecimiento económico de 1.9% para América Latina en 2025",
            "content": "La Comisión Económica para América Latina y el Caribe (CEPAL) proyectó hoy un crecimiento de 1.9% para las economías de la región en 2025, cifra superior al 1.7% previsto anteriormente. Según el informe, la recuperación estará impulsada por un mejor desempeño de Brasil y México, así como por políticas fiscales más expansivas en varios países de la región.",
            "resumen": "CEPAL mejora proyección de crecimiento para América Latina a 1.9% para 2025.",
            "url": "https://www.cepal.org/es/comunicados/cepal-proyecta-crecimiento-19-2025"
        },
        {
            "date_process": "2025-03-25",
            "title": "Aumenta la inseguridad alimentaria en Centroamérica, alerta CEPAL",
            "content": "Un nuevo estudio de la CEPAL señala que la inseguridad alimentaria en Centroamérica aumentó un 8% en el último año, afectando a más de 18 millones de personas. El fenómeno se atribuye principalmente a los efectos del cambio climático, que ha provocado sequías prolongadas e inundaciones que han afectado la producción agrícola en Guatemala, Honduras, El Salvador y Nicaragua.",
            "url": "https://www.cepal.org/es/comunicados/aumenta-inseguridad-alimentaria-centroamerica"
        },
        {
            "date_process": "2025-03-30",
            "title": "CEPAL y UNICEF firman acuerdo para combatir pobreza infantil en la región",
            "content": "La CEPAL y UNICEF firmaron hoy un acuerdo de cooperación para implementar programas conjuntos destinados a reducir la pobreza infantil en América Latina y el Caribe. El convenio contempla inversiones por USD 45 millones durante los próximos tres años, con énfasis en programas de protección social, educación y salud en comunidades vulnerables.",
            "resumen": "CEPAL y UNICEF firman acuerdo de cooperación por USD 45 millones para reducir pobreza infantil.",
            "url": "https://www.cepal.org/es/acuerdos/cepal-unicef-firman-acuerdo-combatir-pobreza-infantil"
        }
    ]
    
    # Ejecutar el componente de chatbot
    news_chatbot_component(news_data=example_news)