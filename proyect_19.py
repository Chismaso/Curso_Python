#Solicitando elementos de List/Set uno por uno
List = list()
Set = set()
l = int(input('introduzca el tamaño de la lista: '))
s = int(input('introduzca el tamaño del Set: '))
print("Introduzca los elementos de la lista:")
for i in range(0, l):
    List.append(int(input()))
print("Introduzca los elementos del Set:")
for i in range(0, s):
    Set.add(int(input()))
# Muestra los elementos ingresados en la lista y el set
print("Lista:", List)
print("Set:", Set)

#-----------------------------------------------------------

#Solicitando elementos de List/Set en una sola línea
# Solicita los tamaños
l = int(input('Introduzca el tamaño de la lista: '))
s = int(input('Introduzca el tamaño del Set: '))

# Solicita los elementos de la lista en una sola línea
print(f"Introduzca {l} elementos de la lista separados por espacios:")
List = list(map(int, input().split()))

# Solicita los elementos del set en una sola línea
print(f"Introduzca {s} elementos del set separados por espacios:")
Set = set(map(int, input().split()))

# Muestra los elementos ingresados
print("Lista:", List)
print("Set:", Set)