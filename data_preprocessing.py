# Importar la biblioteca necesaria
import pandas as pd

def preprocess_data(data):
    """
    Preprocesa el conjunto de datos eliminando filas con valores NaN y manteniendo solo la columna 'Close'.

    Parámetros:
    - data (DataFrame): Conjunto de datos original que puede contener múltiples columnas y valores NaN.

    Retorna:
    - DataFrame: Conjunto de datos preprocesado con solo la columna 'Close' y sin valores NaN.
    """
    
    data = data.dropna()  # Eliminar filas con valores NaN
    data = data[['Close']]  # Mantener solo la columna 'Close'
    
    return data
