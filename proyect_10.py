#La razón por la que se escribe import typing es para 
# poder usar herramientas que te permiten especificar claramente 
# los tipos de datos en tu código de Python
import typing

# Definir una variable de tipo str (cadena de texto)
z: str = "Hello, world!"

# Definir una variable de tipo int (entero)
x: int = 10

# Definir una variable de tipo float (decimal)
y: float = 1.23

# Definir una variable de tipo list (lista de enteros)
list_of_numbers: typing.List[int] = [1, 2, 3]

# Definir una variable de tipo tuple (tupla de tres enteros)
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)

# Definir una variable de tipo dict (diccionario con claves tipo str y valores tipo int)
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}

# Definir una variable de tipo set (conjunto de enteros)
set_of_numbers: typing.Set[int] = {1, 2, 3}