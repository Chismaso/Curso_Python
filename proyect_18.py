nombre = input('Introduzca su nombre:')
# Solicita al usuario que escriba su nombre y lo guarda en la variable 'nombre'
print("hola " + nombre)
print(type(nombre))
# Muestra un saludo personalizado usando el nombre ingresado
# Muestra el tipo de dato de la variable 'nombre' (siempre será 'str')

#------------------------------------------------------------------------------

# Ejemplo de uso de la función input para solicitar un número entero
num = int(input('Introduzca un número entero: '))
add = num + 1
print("El número ingresado más uno es:", add)

#pedir varios valores de una sola vez
a, b, c = input('Introduzca tres números separados por espacios: ').split()
# Asigna los valores ingresados a las variables a, b y c
print("Los números ingresados son:", a, b, c)