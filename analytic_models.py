def moving_average(data, window=14):
    """
    Calcula la Media Móvil Simple (SMA) de los precios de cierre.

    Parámetros:
    - data (DataFrame): Conjunto de datos que contiene los precios de cierre.
    - window (int, opcional): Tamaño de la ventana de tiempo para la SMA. Por defecto es 14.

    Retorna:
    - Series: Media Móvil Simple de los precios de cierre.
    """
    return data['Close'].rolling(window=window).mean()

def exponential_moving_average(data, window=14):
    """
    Calcula la Media Móvil Exponencial (EMA) de los precios de cierre.

    Parámetros:
    - data (DataFrame): Conjunto de datos que contiene los precios de cierre.
    - window (int, opcional): Tamaño de la ventana de tiempo para la EMA. Por defecto es 14.

    Retorna:
    - Series: Media Móvil Exponencial de los precios de cierre.
    """
    return data['Close'].ewm(span=window, adjust=False).mean()
