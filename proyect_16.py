# Definimos una función que saluda según la hora del día
def saludar_según_hora(hora):
    """
    Esta función toma una hora (en formato 24 horas) como argumento
    y muestra un saludo apropiado según la hora del día.
    """

    if hora < 12:
        # Si la hora es menor a 12, es por la mañana
        print("¡Buenos días!")
    elif hora < 18:
        # Si no es por la mañana y la hora es menor a 18, es por la tarde
        print("¡Buenas tardes!")
    elif hora < 24:
        # Si no es por la mañana ni por la tarde, es por la noche
        print("¡Buenas noches!")
    else:
        # Si no se cumple ninguna de las anteriores, es por la noche
        print("introduce una hora válida entre 0 y 23.")

# Ejemplo de uso de la función
saludar_según_hora(10)  # Cambia este valor para probar otras horas
