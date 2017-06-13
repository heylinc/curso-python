#dado el texto 'esto es una prueba' imprimir una cadena formateada de la sig manera
#argumento <nombre>
#'esto es una prueba'


#-Imprimir cuantas letras 'e' tiene la cadena
#capitalizar cadena 
#mprimir longitud de cadena
#Reemplazar en la cadena la letra o por 

dato = (input("Ingrese un texto: "))
texto = dato
cuenta = 0
buscar = "o"
reemplazar_por= 0
for carac in texto:
    if carac == 'e':
        cuenta += 1
print ("El texto tiene ",cuenta ," Caracteres de e")
print("capitalizacion: ", texto.upper())
print("La longitud de la cadena es de: ", len(dato))
print("Reemplazando o por 0 : ", dato.replace(buscar,str(reemplazar_por)))

