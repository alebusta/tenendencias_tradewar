import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Datos 
default_data = {
    'País/Región': ['Paraguay', 'Argentina', 'Perú', 'Uruguay', 'Colombia', 
                    'Global', 'Brasil', 'Chile', 'Ecuador', 'Bolivia', 'México', 'Venezuela'],
    'Crecimiento (%)': [3.8, 5.5, 2.8, 2.8, 2.4, 2.8, 2.0, 2.0, 1.7, 1.1, -0.3, -4.0]
}

# Crear DataFrame
df = pd.DataFrame(default_data)

def crear_grafico_fmi(titulo='Previsiones de Crecimiento Económico del FMI para 2025', 
                     fuente='Elaboración propia sobre proyecciones del FMI reseñadas en medios y publicadas el 22 de abril de 2025',
                     color_positivo='#2E8B57', color_negativo='#D62728', color_global='#4169E1'):
    """
    Crea un gráfico de barras horizontales ordenado con las previsiones de crecimiento económico.
    """
    # Ordenar los datos
    df_sorted = df.sort_values('Crecimiento (%)', ascending=True)
    
    # Crear colores según el valor
    colors = [color_positivo if x >= 0 else color_negativo for x in df_sorted['Crecimiento (%)']]
    
    # Cambiar color para Global
    for i, pais in enumerate(df_sorted['País/Región']):
        if pais == 'Global':
            colors[i] = color_global
    
    # Crear el gráfico con Plotly
    fig = go.Figure()
    
    # Añadir barras horizontales
    fig.add_trace(go.Bar(
        y=df_sorted['País/Región'],
        x=df_sorted['Crecimiento (%)'],
        orientation='h',
        marker_color=colors,
        text=[f'{x}%' for x in df_sorted['Crecimiento (%)']],
        textposition='auto',
    ))
    
    # Configurar el diseño
    fig.update_layout(
        title={
            'text': titulo,
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=16)
        },
        xaxis_title='Crecimiento Económico Proyectado (%)',
        xaxis=dict(
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='black',
            gridcolor='lightgray',
            gridwidth=1
        ),
        yaxis=dict(
            title=None,
            autorange="reversed"  # Para mantener el orden ascendente
        ),
        showlegend=False,
        height=600,
        margin=dict(t=100, b=100),  # Márgenes para el título y la fuente
        annotations=[
            dict(
                text=fuente,
                xref='paper',
                yref='paper',
                x=0.5,
                y=-0.15,
                showarrow=False,
                font=dict(size=10, color='gray'),
                align='center'
            )
        ]
    )
    
    # Mostrar en Streamlit
    st.plotly_chart(fig, use_container_width=True)

