# Importar la biblioteca necesaria
import pandas as pd

def preprocess_data(data):
  
    data = data.dropna()  # Eliminar filas con valores NaN
    data = data[['Close']]  # Mantener solo la columna 'Close'
    
    return data
