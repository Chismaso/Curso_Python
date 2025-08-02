#Uso del operador %
# El operador % se utiliza para formatear cadenas de texto
# Ejemplo de uso del operador %
# %d – entero
# %f – flotante
# %s - cadena
# %x - hexadecimal
# %o – octal

# Entrada de datos
num = int(input("Introduzca un número:"))
add = num+2.7
# Salida
# Ejemplo de uso del operador %
print("El número ingresado es %d y la suma es %d" %(num, add)) 
# Ejemplo de uso del operador % con formato de flotante 
print("El número ingresado es %d y la suma es %f" %(num, add))
# Ejemplo de uso del operador % con formato de flotante con dos decimales
print("El número ingresado es %d y la suma es %.2f" %(num, add))
# Ejemplo de uso del operador % con formato de cadena
print("El número ingresado es %s y la suma es %.2f" %(str(num), add))
# Ejemplo de uso del operador % con formato hexadecimal
print("El número ingresado es %x y la suma es %.2f" %(num, add))
# Ejemplo de uso del operador % con formato octal
print("El número ingresado es %o y la suma es %.2f" %(num, add))  
