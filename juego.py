opciones = {
  'piedra':{
    'papel': False,
    'tijera': True,
  },
  'papel': {
    'piedra': True,
    'tijera': False,
  },
  'tijera': {
    'piedra': False,
    'papel': True,
  }
}
import random
print ("Bienvenido al juego")
count = 1    
while count <= 3:   
  print(input(""" "Digite "piedra, papel o tijera":  """))
  print("Turno de la maquina")
  print(random.choice(["piedra", "papel", "tijera"]))
count += 1