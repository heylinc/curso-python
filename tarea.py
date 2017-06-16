

if __name__ == '__main__':
    nombre = input("Digita tu nombre: ")
    apellido = input("Digita tu apellido: ")
    edad = int(input("Digita tu edad: "))
    cumple = 100 - edad
    cumplira = 2017 + cumple
    mensaje = "<< {nombre} >>, cumplira 100 años en el: {anio}"
    print(mensaje.format(nombre=nombre, anio=cumplira))
