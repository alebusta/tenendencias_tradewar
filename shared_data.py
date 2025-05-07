import streamlit as st
import pandas as pd

# Función para cargar el DataFrame desde Google Drive con caché
@st.cache_data(ttl=3600)  # Caché con tiempo de vida de 1 hora
def load_data_from_drive():
    """
    Carga datos desde Google Drive y devuelve un DataFrame
    """
    try:
      # ID del archivo en Google Drive (extraído del enlace compartido)
      file_id = '1C5w6w3u-pFKv3-l7iLAGhphyO9nn4Xmc'
      url = f'https://drive.google.com/uc?id={file_id}'      
      df = pd.read_csv(url)
      return df

    except Exception as e:
        st.error(f"Error al cargar datos: {e}")
        return None

# Función para acceder al DataFrame desde cualquier página
def get_dataframe():
    """
    Recupera el DataFrame desde la caché o lo carga si no está disponible
    """
    return load_data_from_drive()
