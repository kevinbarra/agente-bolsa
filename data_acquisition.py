# Importar la biblioteca yfinance, que permite descargar datos financieros de Yahoo Finance
import yfinance as yf

def get_data_from_yahoo(ticker, start_date, end_date):
    """
    Descarga datos históricos para un ticker específico desde Yahoo Finance entre las fechas especificadas.

    Parámetros:
    - ticker (str): El símbolo del activo en Yahoo Finance (por ejemplo, "AAPL" para Apple).
    - start_date (str): Fecha de inicio en formato "AAAA-MM-DD".
    - end_date (str): Fecha final en formato "AAAA-MM-DD".

    Retorna:
    - DataFrame: Conjunto de datos históricos con las columnas de Fecha, Open, High, Low, Close, Adj Close y Volume.
    """
    
    # Utilizar la función download de yfinance para obtener los datos históricos
    data = yf.download(ticker, start=start_date, end=end_date)
    
    return data
