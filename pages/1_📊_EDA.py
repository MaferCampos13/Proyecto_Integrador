import streamlit as st
import pandas as pd
import numpy as np
from src.eda import plot_heatmap, plot_countplot, plot_histplot, plot_boxplot, plot_scatterplot, plot_barplot, plot_violinplot, plot_scatter 

@st.cache_data
def load_data():
    return pd.read_csv('data/study_performance.csv')

# Configuración de la Página
st.title('Análisis Exploratorio de Datos (EDA)')

# Carga de Datos
df = load_data()

# Visualización de Aspectos Básicos del Conjunto de Datos
st.header('Visualización de Aspectos Básicos del Conjunto de Datos')
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric('Número de Filas', df.shape[0], border=True)
    with col2:
        st.metric('Número de Columnas', df.shape[1], border=True)
    with col3:
        st.metric('Número de Valores Nulos', df.isnull().sum().sum(), border=True)
    with col4:
        st.metric('Número de Duplicados', df.duplicated().sum(), border=True)
    
# Visualización de la Información del Conjunto de Datos
st.header('Visualización de las Dimensiones del Conjunto de Datos')
st.write(df.shape)

# Visualización de las Primeras Filas del Conjunto de Datos
st.header('Visualización de las Primeras Filas del Conjunto de Datos')
st.dataframe(df.head())

# Visualización de la Descripción Estadística del Conjunto de Datos
st.header('Descripción Estadística del Conjunto de Datos')
st.write(df.describe())

# Mostrar gráficos
st.header('Correlación entre Variables Numéricas')
heatmap_fig = plot_heatmap(df) 
st.pyplot(heatmap_fig, use_container_width=True)

st.header('Conteo de Valores por Clase "Race Ethnicity"')
countplot_fig = plot_countplot(df)
st.pyplot(countplot_fig, use_container_width=True)

st.header('Distribución de las Notas Finales')
histplot_fig = plot_histplot(df)
st.pyplot(histplot_fig, use_container_width=True)

st.header('Rendimiento por Género')
boxplot_fig = plot_boxplot(df)
st.pyplot(boxplot_fig, use_container_width=True)

st.header('Relación entre el Curso de Preparación para el Test y Notas')
scatterplot_fig = plot_scatterplot(df)
st.pyplot(scatterplot_fig, use_container_width=True)

st.header('Rendimiento por Nivel de Educación de los Padres')
barplot_fig = plot_barplot(df)
st.pyplot(barplot_fig, use_container_width=True)

st.header('Distribución de Notas por Identidad Étnica')
violinplot_fig = plot_violinplot(df)
st.pyplot(violinplot_fig, use_container_width=True)

st.header('Relación entre las variables')
x_column = st.selectbox('Seleccione la variable X:', df.columns)
y_column = st.selectbox('Seleccione la variable Y:', df.columns)

scatter_fig = plot_scatter(df, x_column, y_column)
st.pyplot(scatter_fig, use_container_width=True)

