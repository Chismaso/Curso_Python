
# ?El mercado está a seis millas de su casa.
# ?La escuela está a tres kilómetros de su casa. 
# ?Utilice Python para calcular cuánto más lejos está el mercado de su casa que la escuela (en millas).
# ?Nota: Su resultado debe tener el formato de un número, no de una frase.
# !Should print 4
mercado_millas = 6
escuela_Km = 3
transformar_millas = 0.6
escuela_millas = escuela_Km * transformar_millas
diferencia = mercado_millas - escuela_millas
print(int(diferencia))  #!Esto trunca el número, es decir, simplemente elimina lo que hay después del punto decimal sin redondear.
                        #!Si prefieres que redondee (por ejemplo, 4.6 → 5), podrías usar round():