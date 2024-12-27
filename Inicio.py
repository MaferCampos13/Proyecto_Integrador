import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración inicial de la Página
st.set_page_config(layout='wide')

# Título de la Página
st.title('Proyecto Integrador: Análisis de Rendimiento Académico')
st.markdown('## **¡Bienvenido!** ')
st.markdown('En esta aplicación se presenta un análisis de rendimiento académico de estudiantes, donde se exploran diferentes aspectos relacionados con el desempeño de los estudiantes en matemáticas, lectura y escritura. Además, se plantean hipótesis y se entrena un modelo de Machine Learning para predecir el rendimiento académico de los estudiantes.')

# Sección de Páginas
col1, col2 = st.columns([2, 2]) 

with col1:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    st.image("utils/EDA.png", width=300)
    st.markdown('</div>', unsafe_allow_html=True)


with col2:
    st.subheader('**1. Análisis Exploratorio de Datos (EDA)**')
    st.markdown('En esta página se realiza un análisis exploratorio de los datos, mostrando aspectos básicos del conjunto de datos, visualización de la información, descripción estadística y gráficos de correlación entre variables numéricas, conteo de valores y más información relevante.')


col3, col4 = st.columns([2, 2])

with col3:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    st.image("utils/HIPOTESIS.png", width=300)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.subheader('**2. Hipótesis del Proyecto Integrador**')
    st.markdown('En esta página se presentan las hipótesis planteadas en el proyecto, mostrando visualizaciones que permiten validar o refutar cada una de ellas. Se incluyen gráficos de caja, de barras, de dispersión y más.')


col5, col6 = st.columns([2, 2])

with col5:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    st.image("utils/MODELO.png", width=300)
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.subheader('**3. Modelo de Machine Learning**')
    st.markdown('En esta página se presenta el modelo de Machine Learning que se ha entrenado para predecir el rendimiento académico de los estudiantes. Se incluye el modelo de regresión lineal como algoritmo base.')

