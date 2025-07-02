# Las siguientes líneas asignan a la variable a la izquierda del operador = 
# los valores y expresiones aritméticas que están a la derecha del operador =.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total / room_guests

# Esta línea muestra el resultado del cálculo final almacenado
# en la variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person))  
# cambia el tipo de dato a string para concatenar con el texto.