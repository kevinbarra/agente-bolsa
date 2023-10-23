# Importación de las funciones y módulos necesarios desde otros archivos
from data_acquisition import get_data_from_yahoo
from data_preprocessing import preprocess_data
from analytic_models import moving_average, exponential_moving_average
from machine_learning import train_and_predict
from interface import interpret_results

def main():
    # Definición del ticker para obtener datos de Yahoo Finance
    ticker = "USDMXN=X"  # Símbolo para USD/MXN en Yahoo Finance

    # Rango de fechas para la extracción de datos
    start_date = "2023-01-01"
    end_date = "2023-10-16"
    
    # Obtención de datos históricos de Yahoo Finance para el par USD/MXN
    data = get_data_from_yahoo(ticker, start_date, end_date)
    
    # Preprocesamiento de datos para limpiar y organizar
    preprocessed_data = preprocess_data(data)
    
    # Cálculo de la Media Móvil Simple (MA) y la Media Móvil Exponencial (EMA)
    ma = moving_average(preprocessed_data)
    ema = exponential_moving_average(preprocessed_data)
    
    # Entrenamiento del modelo de aprendizaje automático y obtención de predicciones
    predictions, error = train_and_predict(preprocessed_data)
    
    # Interpretación de los resultados basada en los indicadores y predicciones
    analysis = interpret_results(ma, ema, predictions)
    
    # Impresión de la interpretación y el error del modelo
    print(analysis)
    print("Error del modelo:", error)

# Verificación para ejecutar la función main() solo si el script se ejecuta directamente
if __name__ == "__main__":
    main()

