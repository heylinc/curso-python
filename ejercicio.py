import random
lista_aleatorio = [ ]
lista_par = []
lista_impar = []


for i in range (20):

    lista_aleatorio.append(random.randint(0, 100))
    
print (lista_aleatorio)
lista_aleatorio.sort()
print("Ordenados ascendentemente")
print(lista_aleatorio)
print("Imprimiendo los pares")
while len(lista_aleatorio)> 0:
  num = lista_aleatorio.pop()
  if (num%2 == 0):
    lista_par.append(num)
  else:
    lista_impar.append(num)
  
print("Lista de pares")  
print (lista_par)
lista_par.sort()
print (lista_par)
print("Lista de impares")
print(lista_impar)
lista_impar.sort()
print (lista_impar)
print("completado")
print(lista_par,lista_impar)