#sin funcion
name = "Kay"

#?len es una funcion que devuelve la longitud de un objeto
#!en este caso, devuelve la cantidad de caracteres del string name
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))

name = "Cameron"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))
print("----------------")
#con funcion
def lucky_number(name):
    number = len(name) * 9
    return f"Hello {name}. Your lucky number is {number}"
print(lucky_number("Kay"))
print(lucky_number("Cameron"))