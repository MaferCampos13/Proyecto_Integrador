import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap(df):
    plt.figure(figsize=(10, 6))
    correlation_matrix = df.select_dtypes(include=np.number).corr()  
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Mapa de Correlación', fontsize=14)
    plt.show()

def plot_countplot(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='race_ethnicity', palette='husl')
    plt.title('Conteo de Valores por Clase: Race ethnicity', fontsize=14)
    plt.xlabel('Clase', fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.show()


def plot_histplot(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df['math_score'], kde=True, bins=20, color='skyblue')
    plt.title('Distribución de las Notas Finales', fontsize=14) 
    plt.xlabel('Notas', fontsize=12) 
    plt.ylabel('Frecuencia', fontsize=12)
    plt.show()

def plot_boxplot(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='gender', y='math_score', palette='pastel')  
    plt.title('Rendimiento por Género', fontsize=14)
    plt.xlabel('Género', fontsize=12)
    plt.ylabel('Notas', fontsize=12)
    plt.show()

def plot_scatterplot(df):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='test_preparation_course', y='math_score', hue='gender', style='gender', palette='Set2') 
    plt.title('Relación entre el Curso de preparación para el test y Notas', fontsize=14)
    plt.xlabel('Horas de Estudio', fontsize=12)
    plt.ylabel('Notas', fontsize=12)
    plt.show()

def plot_barplot(df):
    plt.figure(figsize=(12, 5))
    sns.barplot(data=df, x='parental_level_of_education', y='math_score', palette='pastel', ci=None) 
    plt.title('Rendimiento por Nivel de Educación de los Padres', fontsize=14)
    plt.xlabel('Nivel de Educación', fontsize=12)
    plt.ylabel('Notas', fontsize=12)
    plt.xticks(rotation=45)
    plt.show()

def plot_violinplot(df):
    plt.figure(figsize=(8, 5))
    sns.violinplot(data=df, x='race_ethnicity', y='math_score', palette='muted')  
    plt.title('Distribución de Notas por Estatus Social', fontsize=14)
    plt.xlabel('Estatus Social', fontsize=12)
    plt.ylabel('Notas', fontsize=12)
    plt.show()

def plot_scatter(df, x_column, y_column):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x=x_column , y=y_column , color='skyblue')
    plt.title('Relación entre las variables', fontsize=14)
    plt.xlabel(x_column, fontsize=12)
    plt.ylabel(y_column, fontsize=12)
    plt.show()

