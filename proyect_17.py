# bucle WHILE
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

attempts(5)
# Este código define una función attempts que toma un número n como argumento
# y utiliza un bucle while para imprimir "Attempt" seguido del número de intento
# desde 1 hasta n. Al final, imprime "Done". La función attempts se llama con el argumento 5,
# lo que significa que imprimirá "Attempt 1" hasta "Attempt 5" y luego "Done".
# Puedes cambiar el valor de n al llamar a la función para ver más o menos intentos.

#-------------------------------------------------------------------------------------------
my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1
# Este código define una variable my_variable con un valor inicial de 5.
# Luego, utiliza un bucle while para imprimir "Hello" mientras my_variable sea menor que 10.
# En cada iteración del bucle, se incrementa my_variable en 1.
# Cuando my_variable alcanza 10, el bucle se detiene.

#--------------------------------------------------------------------------------------------
x = 1
sum = 0
while x < 10:
    sum = sum + x
    x = x + 1

product = 1
while x < 10:
    product = product * x
    x = x + 1

print(sum, product)
#Ouput 45 1
# Este código inicializa una variable x en 1 y una variable sum en 0.
# Luego, utiliza un bucle while para sumar los números del 1 al 9 (excluyendo el 10) a la variable sum. 
# Después, inicializa una variable product en 1 y utiliza otro bucle while para multiplicar los números del 1 al 9 (excluyendo el 10) a la variable product.
# Finalmente, imprime el resultado de sum y product.
# Sin embargo, hay un error en el código: después de la primera suma, x se convierte en 10,
# por lo que el segundo bucle while nunca se ejecuta. Para corregir esto, deberías reiniciar x a 1 antes del segundo bucle.

#---------------------------------------------------------------------------------------------
def count_down(start_number):
  current = start_number 
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)
# Este código define una función count_down que toma un número de inicio como argumento.
# Utiliza un bucle while para contar hacia atrás desde ese número hasta 1, imprimiendo cada número en el camino.
# Cuando llega a 0, imprime "Zero!".