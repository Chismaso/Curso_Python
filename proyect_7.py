def to_celsius(x):
    #convetir farenheit en celsius
    return (x-32) * 5/9

#creamos una variable temperatura para guardar el resultado que devuelve tu función to_celsius(75)
    #!llamamos a la funcion y le pasamos la temperatura de farenheit que queremos pasar a celsius
temperatura = to_celsius(75)
print(temperatura)

# !Mostramos el resultado redondeado a 2 decimales usando round()
print(round(temperatura, 2))
# !Si queremos mostrar el número sin decimales, redondeamos al entero más cercano
print(round(temperatura))

#?convertido en texto con f-string
# !Alternativamente, podemos usar un f-string para mostrar exactamente 2 decimales
print(f"{temperatura:.2f}")
# !lo mismo pero con .0f para no dar decimales (se redondea)
print(f"{temperatura:.0f}")