import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from src.hipotesis import hipotesis_1, hipotesis_2_1, hipotesis_2_2, hipotesis_3_1, hipotesis_3_2, hipotesis_4_1, hipotesis_4_2, hipotesis_5_1, hipotesis_5_2, hipotesis_5_3

# Carga el DataFrame
@st.cache_data
def load_data():
    return pd.read_csv('data/study_performance.csv')

# Cargar datos
df = load_data()

st.title('Hipótesis del Proyecto Integrador')

# Hipótesis 1
st.header('Hipótesis 1: El género tiene un impacto en los puntajes de las asignaturas')
fig_h1 = hipotesis_1(df)
st.pyplot(fig_h1, use_container_width=True)

# Hipótesis 2
st.header('Hipótesis 2: El nivel educativo de los padres influye en el rendimiento de los estudiantes')
fig_h2_1= hipotesis_2_1(df)
st.pyplot(fig_h2_1, use_container_width=True)

fig_h2_2= hipotesis_2_2(df)
st.pyplot(fig_h2_2, use_container_width=True)

# Hipótesis 3
st.header('Hipótesis 3: Los estudiantes que realizaron el curso de preparación para el examen tienen mejores puntajes')
fig_h3_1 = hipotesis_3_1(df)
st.pyplot(fig_h3_1, use_container_width=True)

fig_h3_2 = hipotesis_3_2(df)
st.pyplot(fig_h3_2, use_container_width=True)

# Hipótesis 4
st.header('Hipótesis 4: El tipo de almuerzo influye en el rendimiento académico')
fig_h4_1= hipotesis_4_1(df)
st.pyplot(fig_h4_1, use_container_width=True)

fig_h4_2 = hipotesis_4_2(df)
st.pyplot(fig_h4_2, use_container_width=True)

# Hipótesis 5
st.header('Hipótesis 5: La etnia de los estudiantes tiene una relación con sus puntajes en las tres asignaturas')
fig_h5_1 = hipotesis_5_1(df)
st.pyplot(fig_h5_1, use_container_width=True)

fig_h5_2 = hipotesis_5_2(df)
st.pyplot(fig_h5_2, use_container_width=True)

fig_h5_3 = hipotesis_5_3(df)
st.pyplot(fig_h5_3, use_container_width=True)
