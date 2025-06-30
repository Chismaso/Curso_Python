# ESte codigo es igual que el del proyect_1 pero no se repiten los nombres
friends = ["Alex", "Sara", "Ismael", "Veronica"]
for i in range(len(friends)):
    for j in range(i + 1, len(friends)): #!así evitamos imprimir combinaciones repetidas o invertidas. 
                                         #!Por ejemplo: Si i = 0 (Alex), j empezará en 1 (Sara) y no volverá a 0
        print("hi " + friends[i] + " and " + friends[j])