# Piramides a la izquierda: 
print("Piramides a la izquierda:")
print()
# Piramide invertida de "*"(asteriscos)
print("Piramide invertida de *")
print()
for i in range (10, 0, - 1):#!Comenzamos desde 10 hasta 1, en pasos de -1
    print("*" * i)          #!Imprime i asteriscos en cada línea
print()
# Piramide normal de "*"(asteriscos)
print("Piramide normal de *")
for i in range(0, 10, +1):
    print("*" * i)
print()

# Piramides a la derecha:
print("Piramides a la derecha:")
print()

# Piramide normal de "*"(asteriscos)
print("Piramide normal de *:")
print()
for i in range(0, 10):
    print(" " * (10 - 1 * i) + "*" * i)
print()
# Piramide invertida de "*"(asteriscos)
print("Piramide invertida de *:")
print()
for i in range (0, 10):
    print("*" * i + " " * (10 - 1 * i) + "|")   #!(10 - 1 * i) esto es para que despues del asterisco quede el mismo espacio
                                                #!+ "|" añadí esto para ver que el espacio queda igual despues de los asteriscos
print()

# Piramides enteras:
print("Piramides enteras:")
print()

# Piramide normal
print("Piramide normal:")
for i in range(0, 10):
    print(" " * (10 - i) + "*" * (2 * i - 1))
        #!range(1, 11) → Recorre los valores del 1 al 10 (inclusive). Cada valor representa una fila de la pirámide.
        #!" " * (10 - i) → Añade espacios al principio de cada fila para centrar los asteriscos.
        #!"*" * (2 * i - 1) → Genera un número impar de asteriscos por línea, que va creciendo con cada iteración.
        #!¿Por qué (2 * i - 1)? Esto genera los números impares: 1, 3, 5, 7, ..., 19. De este modo, los asteriscos forman una figura simétrica, más ancha conforme baja.
print()
#Piramide invertida:
print("Piramide invertida:")
print()
for i in range (10, 0, -1):
    print(" " * (10 - i) + "*" * (2 * i - 1))