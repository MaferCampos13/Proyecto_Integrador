import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

try: 
    @st.cache_data
    def load_data():
        # Cargar los datos de entrenamiento desde el archivo predefinido
        data = pd.read_csv('data/study_performance.csv')
        st.title("Vista previa de los datos:")
        st.dataframe(data.head())
        return data
    
    train_data = load_data()

    #Comprobar que el archivo tiene la columna 'math_score', 'reading_score' y 'writing_score'
    if 'math_score' not in train_data.columns or 'reading_score' not in train_data.columns or 'writing_score' not in train_data.columns:
        st.error('El archivo seleccionado no tiene las columnas necesarias para entrenar el modelo.')
    else:
        #Colocando el modelo
        # Variables independientes (X) y dependientes (Y)
        X = train_data.drop(['math_score', 'reading_score', 'writing_score'], axis=1)  # Eliminar puntajes
        Y = train_data[['math_score', 'reading_score', 'writing_score']]  # Puntajes de las tres asignaturas
        
        # Convertir variables categóricas a variables dummy
        X_encoded = pd.get_dummies(X, drop_first=True)
        
        # Dividir el conjunto de datos en entrenamiento y prueba
        X_train, X_test, Y_train, Y_test = train_test_split(X_encoded, Y, test_size=0.2, random_state=42)
        
        # Crear el modelo de regresión lineal
        regressor = LinearRegression()
        
        # Entrenar el modelo
        regressor.fit(X_train, Y_train)
        
        # Realizar predicciones
        Y_pred = regressor.predict(X_test)
        
        # Asignar el modelo entrenado a la variable model
        model = regressor

        # Evaluar el modelo
        mse = mean_squared_error(Y_test, Y_pred)
        r2 = r2_score(Y_test, Y_pred)
        
        # Resultados
        print(f'Mean Squared Error: {mse}')
        print(f'R^2 Score: {r2}')
        
        # Mostrar resultados utilizando métricas
        st.title('Resultados del modelo de Machine Learning:')
        col1, col2 = st.columns(2)
        col1.metric('Mean Squared Error', mse, f"{mse:.4f}", border=True)
        col2.metric('R^2 Score', r2, f"{r2:.4f}", border=True)

except FileNotFoundError:
    st.error('No se encontró el archivo de datos. Por favor, asegúrese de que el archivo seleccionado es correcto.')
    
except Exception as e:
    st.error(f'Ocurrió un error al procesar el archivo de entrenamiento: {e}')


# Realizando gráfico de dispersión
st.title('Visualización en un gráfico de dispersión de los valores reales y predichos:')

# Convertir los resultados en DataFrame para facilitar la visualización
Y_test_df = Y_test.reset_index(drop=True)  # Asegurar que tengan el mismo índice
Y_pred_df = pd.DataFrame(Y_pred, columns=Y_test.columns)

# Crear gráficos para cada asignatura
subjects = Y_test.columns
plt.figure(figsize=(15, 5))

for i, subject in enumerate(subjects):
    plt.subplot(1, 3, i + 1)
    plt.scatter(Y_test_df[subject], Y_pred_df[subject], alpha=0.7, color='blue', edgecolor='k')
    plt.plot([Y_test_df[subject].min(), Y_test_df[subject].max()], 
             [Y_test_df[subject].min(), Y_test_df[subject].max()], 
             color='red', linewidth=2, label='Línea Ideal (y=x)')
    plt.title(f'Real vs Predicción: {subject}')
    plt.xlabel('Valores Reales')
    plt.ylabel('Valores de Predicción')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()

st.pyplot(plt, use_container_width=True)


# Sección para realizar predicciones
st.title('Espacio para Realizar Predicciones:')
prediction_file = st.file_uploader('Cargar archivo para realizar predicciones', type=['csv'])

if prediction_file is not None and model is not None:
    try:
        # Cargar los datos de predicción
        prediction_data = pd.read_csv(prediction_file)
        st.write('Vista previa de los datos de predicción:')
        st.dataframe(prediction_data.head())

        # Validar si "math_score", "reading_score" y "writing_score" están en el archivo y eliminarlos
        if 'math_score' in prediction_data.columns:
            prediction_data.drop(['math_score'], axis=1, inplace=True)
        if 'reading_score' in prediction_data.columns:
            prediction_data.drop(['reading_score'], axis=1, inplace=True)
        if 'writing_score' in prediction_data.columns:
            prediction_data.drop(['writing_score'], axis=1, inplace=True)
        st.warning('Las columnas "math_score", "reading_score" y "writing_score" no serán tomadas en cuenta para la predicción.')

        # Codificar las columnas categóricas para que coincidan con el modelo
        prediction_data_encoded = pd.get_dummies(prediction_data, drop_first=True)

        # Asegurar que todas las columnas esperadas estén presentes
        expected_features = model.feature_names_in_
        missing_features = set(expected_features) - set(prediction_data_encoded.columns)
        for feature in missing_features:
            prediction_data_encoded[feature] = 0  # Agregar columna faltante con valor 0

        # Ordenar las columnas en el mismo orden que el modelo espera
        prediction_data_encoded = prediction_data_encoded[expected_features]

        # Realizar predicciones
        predictions = model.predict(prediction_data_encoded)

        # Mostrar las predicciones
        st.write('Predicciones:')
        st.dataframe(pd.DataFrame(predictions, columns=['math_score', 'reading_score', 'writing_score']))
        
    except Exception as e:
        st.error(f'Ocurrió un error al procesar el archivo de predicción: {e}')



