#en Python, las tuplas son inmutables, lo que significa que no se pueden modificar una vez creadas.
# Sin embargo, puedes convertir una tupla en una lista, modificar la lista y luego volver a convertirla en una tupla.
# Aquí tienes un ejemplo de cómo hacerlo:
T = (2, 3, 4, 5, 6)
print("Tupla inicial")
print(T)
L = list(T)
L.append(int(input("Introduzca el nuevo elemento: ")))
L = tuple(L)
print("Tupla final")
print(L)
