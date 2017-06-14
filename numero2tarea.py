lista = []
for i in range(4):
        print("Dígite numero", str(i + 1) + ": ", end="")
        digito = input()
        lista += [digito]
print("La lista creada es:", lista)
print("Primer numero de la lista", lista[0])
print("ultimo numero de la lista", lista[3])