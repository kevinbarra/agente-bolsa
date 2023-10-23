# Importar la biblioteca yfinance, que permite descargar datos financieros de Yahoo Finance
import yfinance as yf

def get_data_from_yahoo(ticker, start_date, end_date):
    """
    Descarga datos históricos para un ticker específico desde Yahoo Finance entre las fechas especificadas.




  
    """
    
    # Utilizar la función download de yfinance para obtener los datos históricos
    data = yf.download(ticker, start=start_date, end=end_date)
    
    return data
