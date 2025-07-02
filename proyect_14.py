lista_numeros = [12, 2, 32, 19, 57, 22, 14]

# !Con sorted() Ordenamos la lista de menor a mayor
print(lista_numeros)
print(sorted(lista_numeros))
#Si queremos ordenar de mayor a menor, podemos usar el argumento reverse=True
print(sorted(lista_numeros, reverse=True))

#!Con frase concatenada
print("con str():")
print("La lista ordenada de menor a mayor es: " + str(sorted(lista_numeros)))
# Con f-strings
    # !(RECOMENDADA)
print("con f-strings:")
print(f"La lista ordenada de menor a mayor es: {sorted(lista_numeros)}")


#con frase concatenada
print("con str(): ")
print("La lista ordenada de mayor a menor es: " + str(sorted(lista_numeros, reverse=True)))
# Con f-strings
    # !(RECOMENDADA)
print("con f-strings:")
print(f"La lista ordenada de mayor a menor es: {sorted(lista_numeros, reverse=True)}")

# !Con min() y max() obtenemos el valor mínimo y máximo de la lista
print("valores min y max:")
print(min(lista_numeros))
print(max(lista_numeros))

#!con frase concatenada 
print("con str(): ")
print("El valor minimo de la lista es: " + str(min(lista_numeros)))

print("con str(): ")
print(f"El valor maximo de la lista es: {max(lista_numeros)}")

#tambien se puede hacer con f-strings 
    #!(RECOMENDADA)
print("con f-strings:")
print(f"El valor minimo de la lista es: {min(lista_numeros)}")

print("con f-strings:")
print("El valor maximo de la lista es: " + str(max(lista_numeros)))   
