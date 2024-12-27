import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    correlation_matrix = df.select_dtypes(include=np.number).corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
    ax.set_title('Mapa de Correlación', fontsize=14)
    return fig

def plot_countplot(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(data=df, x='race_ethnicity', palette='husl', ax=ax)
    ax.set_title('Conteo de Valores por Clase: Race ethnicity', fontsize=14)
    ax.set_xlabel('Clase', fontsize=12)
    ax.set_ylabel('Frecuencia', fontsize=12)
    return fig

def plot_histplot(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df['math_score'], kde=True, bins=20, color='skyblue', ax=ax)
    ax.set_title('Distribución de las Notas Finales', fontsize=14)
    ax.set_xlabel('Notas', fontsize=12)
    ax.set_ylabel('Frecuencia', fontsize=12)
    return fig

def plot_boxplot(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df, x='gender', y='math_score', palette='pastel', ax=ax)
    ax.set_title('Rendimiento por Género', fontsize=14)
    ax.set_xlabel('Género', fontsize=12)
    ax.set_ylabel('Notas', fontsize=12)
    return fig

def plot_scatterplot(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x='test_preparation_course', y='math_score', hue='gender', style='gender', palette='Set2', ax=ax)
    ax.set_title('Relación entre el Curso de preparación para el test y Notas', fontsize=14)
    ax.set_xlabel('Horas de Estudio', fontsize=12)
    ax.set_ylabel('Notas', fontsize=12)
    return fig

def plot_barplot(df):
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.barplot(data=df, x='parental_level_of_education', y='math_score', palette='pastel', ci=None, ax=ax)
    ax.set_title('Rendimiento por Nivel de Educación de los Padres', fontsize=14)
    ax.set_xlabel('Nivel de Educación', fontsize=12)
    ax.set_ylabel('Notas', fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    return fig

def plot_violinplot(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.violinplot(data=df, x='race_ethnicity', y='math_score', palette='muted', ax=ax)
    ax.set_title('Distribución de Notas por Identidad Étnica', fontsize=14)
    ax.set_xlabel('Estatus Social', fontsize=12)
    ax.set_ylabel('Notas', fontsize=12)
    return fig

def plot_scatter(df, x_column, y_column):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x=x_column, y=y_column, color='skyblue', ax=ax)
    ax.set_title('Relación entre las variables', fontsize=14)
    ax.set_xlabel(x_column, fontsize=12)
    ax.set_ylabel(y_column, fontsize=12)
    return fig


