import argparse


if __name__=='__main__':

	parser= argparse.ArgumentParser('valor')
	parser.add_argument('Nombre')
	parser.add_argument('Edad')
	parser.add_argument('Clase')


	args = parser.parse_args()

	datos = {
	'Nombre': args.Nombre,
	'Edad': args.Edad,
	'Clase': args.Clase,

	}

	for llave,valor in datos.iteritems():
		print llave, valor

