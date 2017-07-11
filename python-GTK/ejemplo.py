
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Mi_Ventana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		
		super(Mi_Ventana, self).__init__(*args, **kwargs)
		self.set_size_request(500, 300)
		self.connect('delete-event', Gtk.main_quit)

		self.agregar_contener()
		self.agregar_entrada()
		self.agregar_boton()
		self.agregar_lista()

	def agregar_contenedor(self):
		self.contenedor = Gtk,Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
		self.contenedor.attach(self.entrada, 0, 0, 1, 1)

	def agregar_boton(self):
		self.boton = Gtk.Button('Agregar')
		self.contenedor.attach_next_to(
			self.boton,
			self.entrada,
			Gtk.PositionType.BOTTOM,
			1,
			1
		)

	def agregar_lista(self):
		"""crea un TreeView
		1- crear el modelos de datos(Gtk.ListStore(type, type....., type))
		2- crear un widget que contiene o muestra los datos del modelo
		TreeView(<model>)
		3- definir las columnas y sus contenidos
		3.1- crear celda para cada cplumna de la fila
		los CallRender son widget que srievn para mostrar contenidos dentro de
	    otro widget dependiendo de su tipo
	    3.2- crear columnas (TreeViewColumn) del TreeView que mostraran los datos
	    usando CellRunder como widget como elemntos hijos.
	    args: (Titulo, CellRunder, Posicion en el modelo de la informacion a mostart)
	    3.3- agregar cda TreeViewColumn al TreeView widget"""

	    self.modelo = Gtk.ListStore(str, float)
	    self.lista_arvhivos = Gtk.TreeView(self.modelo)

	    descripcion = Gtk.CellRenderText()
	    columna_descripcion = Gtk.TreeViewColumn(
	    	'Descripcion', 
	    	Descripcion, 
	    	text=0
	    	)

	    monto = Gtk.CellRenderText()
	    columna_monto = Gtk.TreeViewColumn('Monto', monto, text=1)

	    self.lista_arvhivos.append_column(columna_descripcion)
	    self.lista_arvhivos,.append_column(columna_monto)

	    self.contenedor.attach_next_to(
	    	self.lista_arvhivos,
	    	self.boton,
	    	Gtk.PositionType.BOTTOM,
	    	1,
	    	1
	    )


if __name__ == '__main__':
	ventana = Mi_Ventana()
	ventana.show_all()

	Gtk.main()

    

    	