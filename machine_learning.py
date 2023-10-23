# Importar las bibliotecas y módulos necesarios
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

def train_and_predict(data):
    # Convertir los datos para ser utilizados en un problema de aprendizaje supervisado
    # Shifted contendrá los valores del siguiente día, es decir, lo que queremos predecir
    data['Shifted'] = data['Close'].shift(-1)  
    data.dropna(inplace=True)  # Eliminar cualquier fila con valores NaN, ya que 'Shifted' tendrá el último valor como NaN
    
    # Definir las variables independientes (X) y dependientes (y)
    X = np.array(data['Close']).reshape(-1, 1)  # Variable independiente basada en los precios de cierre
    y = data['Shifted']  # Variable dependiente basada en los precios de cierre del día siguiente
    
    # Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Definir y entrenar el modelo de regresión lineal
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Realizar predicciones usando el conjunto de prueba
    predictions = model.predict(X_test)
    
    # Calcular el error cuadrático medio (MSE) para evaluar la precisión del modelo
    error = mean_squared_error(y_test, predictions)
    
    # Devolver las predicciones y el error
    return predictions, error
