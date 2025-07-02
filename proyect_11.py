from typing import Callable

# Creamos una función que toma otra función como argumento
def procesar_funcion(funcion: Callable[[str], None]) -> None:
    print("Ejecutando función...")
    funcion("Hola desde Callable")

# Esta es una función que cumple con la firma: toma un str y no devuelve nada
def mostrar_mensaje(mensaje: str) -> None:
    print(f"Mensaje recibido: {mensaje}")

# Llamamos a la función procesar_funcion pasándole mostrar_mensaje
procesar_funcion(mostrar_mensaje)

# en la funcion procesar_funcion, funcion("Hola desde Callable") se refiere a la llamada a la función mostrar_mensaje
# que se pasa como argumento. Esto es posible porque la función mostrar_mensaje
# tiene la firma correcta: toma un argumento de tipo str y no devuelve nada.
# Por lo tanto, cuando se llama a procesar_funcion(mostrar_mensaje),
# se ejecuta mostrar_mensaje con el argumento "Hola desde Callable".   