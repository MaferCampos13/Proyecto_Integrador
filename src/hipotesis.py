import matplotlib.pyplot as plt
import seaborn as sns

# Hipótesis 1
def hipotesis_1(data):
    plt.figure(figsize=(18, 6))

    #Subgráfico 1
    plt.subplot(1, 3, 1)
    sns.boxplot(data=data, x='gender', y='math_score', palette='Set2')
    plt.title('Math Score por Gender')

    #Subgráfico 2
    plt.subplot(1, 3, 2)
    sns.boxplot(data=data, x='gender', y='reading_score', palette='Set2')
    plt.title('Reading Score por Gender')

    #Subgráfico 3
    plt.subplot(1, 3, 3)
    sns.boxplot(data=data, x='gender', y='writing_score', palette='Set2')
    plt.title('Writing Score por Gender')

    plt.tight_layout()
    plt.show()

# Hipótesis 2
def hipotesis_2_1(data):
   #Gráfico 1
    plt.figure(figsize=(18, 6))

    #Subgráfico 1
    plt.subplot(1, 3, 1)
    sns.boxplot(data=data, x='parental_level_of_education', y='math_score', palette='Set2')
    plt.title('Math Score por Parental Level of Education')

    #Subgráfico 2
    plt.subplot(1, 3, 2)
    sns.boxplot(data=data, x='parental_level_of_education', y='reading_score', palette='Set2')
    plt.title('Reading Score por Parental Level of Education')

    #Subgráfico 3
    plt.subplot(1, 3, 3)
    sns.boxplot(data=data, x='parental_level_of_education', y='writing_score', palette='Set2')
    plt.title('Writing Score por Parental Level of Education')
    
    plt.tight_layout()
    plt.show()

    
def hipotesis_2_2(data):
    #Gráfico 2
    # Promedio de puntajes por nivel educativo de los padres
    mean_scores_by_parent_education = data.groupby('parental_level_of_education')[['math_score', 'reading_score', 'writing_score']].mean()
    
    # Gráfico de barras
    mean_scores_by_parent_education.plot(kind='bar', figsize=(10, 6), color=['skyblue', 'salmon', 'lightgreen'])
    plt.title('Promedio de puntajes según nivel educativo de los padres')
    plt.ylabel('Promedio de puntajes')
    plt.xlabel('Nivel educativo de los padres')
    plt.xticks(rotation=45)
    plt.legend(['Math Score', 'Reading Score', 'Writing Score'])

    plt.tight_layout()
    plt.show()

# Hipótesis 3
def hipotesis_3_1(data):
    #Gráfico 1
    plt.figure(figsize=(18, 6))
    
    # Subgráfico 1 para test_preparation_course vs math_score
    plt.subplot(1, 3, 1)
    sns.boxplot(data=data, x='test_preparation_course', y='math_score', palette='Set2')
    plt.title('Math Score por Test Preparation Course')
    
    # Subgráfico 2 para test_preparation_course vs reading_score
    plt.subplot(1, 3, 2)
    sns.boxplot(data=data, x='test_preparation_course', y='reading_score', palette='Set2')
    plt.title('Reading Score por Test Preparation Course')
    
    # Subgráfico 3 para test_preparation_course vs writing_score
    plt.subplot(1, 3, 3)
    sns.boxplot(data=data, x='test_preparation_course', y='writing_score', palette='Set2')
    plt.title('Writing Score por Test Preparation Course')
    
    plt.tight_layout()
    plt.show()

def hipotesis_3_2(data):
    #Gráfico 2
    mean_scores_by_prep_course = data.groupby('test_preparation_course')[['math_score', 'reading_score', 'writing_score']].mean()
    mean_scores_by_prep_course.plot(kind='bar', figsize=(10, 6), color=['lightblue', 'orange', 'lightgreen'])
    plt.title('Promedio de puntajes según preparación para el examen')
    plt.ylabel('Promedio de puntajes')
    plt.xlabel('Curso de preparación')
    plt.legend(['Math Score', 'Reading Score', 'Writing Score'])

    plt.xticks(rotation=0)
    plt.show()

# Hipótesis 4
def hipotesis_4_1(data):
    #Gráfico 1
    plt.figure(figsize=(18, 6))

    # Subgráfico 1 para lunch vs math_score
    plt.subplot(1, 3, 1)
    sns.boxplot(data=data, x='lunch', y='math_score', palette='Set2')
    plt.title('Math Score por Lunch')
    
    # Subgráfico 2 para lunch vs reading_score
    plt.subplot(1, 3, 2)
    sns.boxplot(data=data, x='lunch', y='reading_score', palette='Set2')
    plt.title('Reading Score por Lunch')
    
    # Subgráfico 3 para lunch vs writing_score
    plt.subplot(1, 3, 3)
    sns.boxplot(data=data, x='lunch', y='writing_score', palette='Set2')
    plt.title('Writing Score por Lunch')
    
    plt.tight_layout()
    plt.show()

def hipotesis_4_2(data):
    #Gráfico 2
    plt.figure(figsize=(18, 6))
    sns.violinplot(data=data, x='lunch', y='math_score', palette='Set1', inner='quartile')
    plt.title('Distribución de Math Scores según tipo de almuerzo')
    plt.xlabel('Lunch Type')
    plt.ylabel('Math Score')

    plt.show()

# Hipótesis 5
def hipotesis_5_1(data):
    #Gráfico 1
    plt.figure(figsize=(18, 6))

    # Subgráfico 1 para race_ethnicity vs math_score
    plt.subplot(1, 3, 1)
    sns.boxplot(data=data, x='race_ethnicity', y='math_score', palette='Set2')
    plt.title('Math Score por Race/Ethnicity')
    
    # Subgráfico 2 para race_ethnicity vs reading_score
    plt.subplot(1, 3, 2)
    sns.boxplot(data=data, x='race_ethnicity', y='reading_score', palette='Set2')
    plt.title('Reading Score por Race/Ethnicity')
    
    # Subgráfico 3 para race_ethnicity vs writing_score
    plt.subplot(1, 3, 3)
    sns.boxplot(data=data, x='race_ethnicity', y='writing_score', palette='Set2')
    plt.title('Writing Score por Race/Ethnicity')
    
    plt.tight_layout()
    plt.show()

def hipotesis_5_2(data):
    #Gráfico 2
    mean_scores_by_ethnicity = data.groupby('race_ethnicity')[['math_score', 'reading_score', 'writing_score']].mean()
    mean_scores_by_ethnicity.plot(kind='bar', figsize=(10, 6), stacked=True, color=['purple', 'gold', 'teal'])
    plt.title('Promedio de puntajes por grupo étnico')
    plt.ylabel('Promedio de puntajes')
    plt.xlabel('Grupo étnico')
    plt.legend(['Math Score', 'Reading Score', 'Writing Score'])
    
    plt.xticks(rotation=45)
    plt.show()

def hipotesis_5_3(data):
    #Gráfico 3
    plt.figure(figsize=(18, 6))
    sns.swarmplot(data=data, x='race_ethnicity', y='math_score', hue='gender', palette='Set2', dodge=True)
    plt.title('Math Score por grupo étnico y género')
    plt.xlabel('Grupo étnico')
    plt.ylabel('Math Score')
    plt.legend(title='Gender')

    plt.show()







