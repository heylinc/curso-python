import argparse

variable_cuatro = 'hola{0}{1}'
var = 'hola {variable}{variable 2}'

def  mi_funcion(val):
	print(variable_cuatro)
	print(var)

if __name__=='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('nombre')
	parser.add_argument('apellido')

	args = parser.parse_args()

	print(args.nombre)
	print(args.apellido)
	print(variable_cuatro.format(args.nombre,args.apellido))
	