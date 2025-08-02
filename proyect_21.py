#en python f antes de abrir comillas indica que es un string formateado
# f-string permite insertar variables directamente en el string
# Ejemplo de uso de f-string
# Declaramos una variable
name = input('Introduzca su nombre: ')
# Salida
print(f'hola {name}!. Qué tal?')

# Ejemplo de uso de format()
# Declaramos de variables
a = 20
b = 10
# Suma
sum = a+b
# Resta
sub = a-b
# Salida

# Usando f-string
print(f'El valor de a es {a} y b es {b}')
# Usando format()
print('El valor de a es {} y b es {}'.format(a,b))

# Usando f-string para operaciones
print(f'{a} + {b} = {sum}')
# Usando format() para operaciones
print('{2} es la suma de {0} y {1}'.format(a, b, sum))
# Usando format() para operaciones(otro metodo)
print('{sub_value} es la resta de {value_a} y {value_b}'.format(value_a=a,value_b=b,sub_value=sub))
