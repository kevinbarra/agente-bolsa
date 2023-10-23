def interpret_results(ma, ema, predictions):
    interpretation = ""
    
    # Verificar tendencia basada en las dos últimas observaciones de Medias Móviles
    # Tanto para la Media Móvil Simple (MA) como para la Media Móvil Exponencial (EMA)
    if ma[-1] > ma[-2] and ema[-1] > ema[-2]:
        # Si ambas medias móviles muestran un aumento en sus últimos valores,
        # se interpreta como una tendencia alcista
        interpretation += "El USD/MXN está en una tendencia alcista basada en medias móviles. "
        interpretation += "Esto se debe a que tanto la media móvil simple (MA) como la media móvil exponencial (EMA) mostraron un aumento en sus últimos valores.\n"
    else:
        # Si alguna o ambas medias móviles muestran una disminución en sus últimos valores,
        # se interpreta como una tendencia bajista
        interpretation += "El USD/MXN está en una tendencia bajista basada en medias móviles. "
        interpretation += "Esto se indica por una disminución en los valores más recientes de la media móvil simple (MA) y/o la media móvil exponencial (EMA).\n"

    # Interpretación basada en la comparación de la predicción del modelo con la última observación de MA
    if predictions[-1] > ma[-1]:
        # Si la última predicción es mayor que el último valor de la MA,
        # se interpreta como una posible tendencia alcista
        interpretation += "El modelo predice un posible aumento en el valor del USD/MXN. "
        interpretation += "La predicción del modelo supera el valor actual de la media móvil, lo que podría sugerir un movimiento alcista.\n"
    else:
        # Si la última predicción es menor o igual al último valor de la MA,
        # se interpreta como una posible tendencia bajista
        interpretation += "El modelo predice una posible disminución en el valor del USD/MXN. "
        interpretation += "La predicción del modelo es inferior al valor actual de la media móvil, lo que podría indicar un movimiento bajista.\n"

    # Devolver la interpretación generada
    return interpretation
