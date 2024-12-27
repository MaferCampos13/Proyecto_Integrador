import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.pyplot as plt
import seaborn as sns

# Hipótesis 1
def hipotesis_1(data):
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Subgráfico 1
    sns.boxplot(data=data, x='gender', y='math_score', palette='Set2', ax=axes[0])
    axes[0].set_title('Math Score por Gender')

    # Subgráfico 2
    sns.boxplot(data=data, x='gender', y='reading_score', palette='Set2', ax=axes[1])
    axes[1].set_title('Reading Score por Gender')

    # Subgráfico 3
    sns.boxplot(data=data, x='gender', y='writing_score', palette='Set2', ax=axes[2])
    axes[2].set_title('Writing Score por Gender')

    fig.tight_layout()
    return fig

# Hipótesis 2
def hipotesis_2_1(data):
    fig, axes = plt.subplots(1, 3, figsize=(28, 10))

    # Subgráfico 1
    sns.boxplot(data=data, x='parental_level_of_education', y='math_score', palette='Set2', ax=axes[0])
    axes[0].set_title('Math Score por Parental Level of Education')

    # Subgráfico 2
    sns.boxplot(data=data, x='parental_level_of_education', y='reading_score', palette='Set2', ax=axes[1])
    axes[1].set_title('Reading Score por Parental Level of Education')

    # Subgráfico 3
    sns.boxplot(data=data, x='parental_level_of_education', y='writing_score', palette='Set2', ax=axes[2])
    axes[2].set_title('Writing Score por Parental Level of Education')

    fig.tight_layout()
    return fig

def hipotesis_2_2(data):
    mean_scores_by_parent_education = data.groupby('parental_level_of_education')[['math_score', 'reading_score', 'writing_score']].mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    mean_scores_by_parent_education.plot(kind='bar', ax=ax, color=['lightskyblue', 'lightcoral', 'mediumseagreen'])

    ax.set_title('Promedio de puntajes según nivel educativo de los padres')
    ax.set_ylabel('Promedio de puntajes')
    ax.set_xlabel('Nivel educativo de los padres')
    ax.legend(['Math Score', 'Reading Score', 'Writing Score'])
    ax.tick_params(axis='x', rotation=45)

    fig.tight_layout()
    return fig

# Hipótesis 3
def hipotesis_3_1(data):
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Subgráfico 1
    sns.boxplot(data=data, x='test_preparation_course', y='math_score', palette='Set2', ax=axes[0])
    axes[0].set_title('Math Score por Test Preparation Course')

    # Subgráfico 2
    sns.boxplot(data=data, x='test_preparation_course', y='reading_score', palette='Set2', ax=axes[1])
    axes[1].set_title('Reading Score por Test Preparation Course')

    # Subgráfico 3
    sns.boxplot(data=data, x='test_preparation_course', y='writing_score', palette='Set2', ax=axes[2])
    axes[2].set_title('Writing Score por Test Preparation Course')

    fig.tight_layout()
    return fig

def hipotesis_3_2(data):
    mean_scores_by_prep_course = data.groupby('test_preparation_course')[['math_score', 'reading_score', 'writing_score']].mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    mean_scores_by_prep_course.plot(kind='bar', ax=ax, color=['lightskyblue', 'lightcoral', 'mediumseagreen'])

    ax.set_title('Promedio de puntajes según preparación para el examen')
    ax.set_ylabel('Promedio de puntajes')
    ax.set_xlabel('Curso de preparación')
    ax.legend(['Math Score', 'Reading Score', 'Writing Score'])
    ax.tick_params(axis='x', rotation=0)

    fig.tight_layout()
    return fig


# Hipótesis 4
import seaborn as sns
import matplotlib.pyplot as plt

def hipotesis_4_1(data):
    # Gráfico 1
    # Crear figura y ejes explícitamente
    fig, axes = plt.subplots(1, 3, figsize=(24, 18))
    
    # Subgráfico 1 para lunch vs math_score
    sns.boxplot(data=data, x='lunch', y='math_score', palette='Set2', ax=axes[0])
    axes[0].set_title('Math Score por Lunch')
    
    # Subgráfico 2 para lunch vs reading_score
    sns.boxplot(data=data, x='lunch', y='reading_score', palette='Set2', ax=axes[1])
    axes[1].set_title('Reading Score por Lunch')
    
    # Subgráfico 3 para lunch vs writing_score
    sns.boxplot(data=data, x='lunch', y='writing_score', palette='Set2', ax=axes[2])
    axes[2].set_title('Writing Score por Lunch')
    
    # Ajustar diseño
    fig.tight_layout()
    
    # Devolver la figura creada
    return fig

def hipotesis_4_2(data):
    # Gráfico 2
    fig, ax = plt.subplots(figsize=(18, 6))
    sns.violinplot(data=data, x='lunch', y='math_score', palette='Set2', inner='quartile', ax=ax)
    ax.set_title('Distribución de Math Scores según tipo de almuerzo')
    ax.set_xlabel('Lunch Type')
    ax.set_ylabel('Math Score')

    return fig

# Hipótesis 5
def hipotesis_5_1(data):
    # Gráfico 1
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Subgráfico 1
    sns.boxplot(data=data, x='race_ethnicity', y='math_score', palette='Set2', ax=axes[0])
    axes[0].set_title('Math Score por Race/Ethnicity')

    # Subgráfico 2
    sns.boxplot(data=data, x='race_ethnicity', y='reading_score', palette='Set2', ax=axes[1])
    axes[1].set_title('Reading Score por Race/Ethnicity')

    # Subgráfico 3
    sns.boxplot(data=data, x='race_ethnicity', y='writing_score', palette='Set2', ax=axes[2])
    axes[2].set_title('Writing Score por Race/Ethnicity')

    fig.tight_layout()
    return fig

def hipotesis_5_2(data):
    # Gráfico 2
    mean_scores_by_ethnicity = data.groupby('race_ethnicity')[['math_score', 'reading_score', 'writing_score']].mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    mean_scores_by_ethnicity.plot(
        kind='bar', stacked=True, color=['lightskyblue', 'lightcoral', 'mediumseagreen'], ax=ax
    )

    ax.set_title('Promedio de puntajes por grupo étnico')
    ax.set_ylabel('Promedio de puntajes')
    ax.set_xlabel('Grupo étnico')
    ax.legend(['Math Score', 'Reading Score', 'Writing Score'])
    ax.tick_params(axis='x', rotation=45)

    fig.tight_layout()
    return fig

def hipotesis_5_3(data):
    # Gráfico 3
    fig, ax = plt.subplots(figsize=(18, 6))
    sns.swarmplot(data=data, x='race_ethnicity', y='math_score', hue='gender', palette='Set2', dodge=True, ax=ax)

    ax.set_title('Math Score por grupo étnico y género')
    ax.set_xlabel('Grupo étnico')
    ax.set_ylabel('Math Score')
    ax.legend(title='Gender')

    return fig






