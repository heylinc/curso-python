import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Mi_Ventana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		
		super(Mi_Ventana, self).__init__(*args, **kwargs)
		self.set_size_request(500, 300)
		self.connect('delete-event', Gtk.main_quit)

		self.agregar_contenedor()
		self.agregar_entrada()
		self.agregar_boton()
		self.agregar_lista()

	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
		self.entrada_monto = Gtk.Entry()
		self.contenedor.attach(self.entrada, 0, 0, 2, 1)
		self.contenedor.attach_next_to(
			self.entrada_monto,
			self.entrada,
			Gtk.PositionType.RIGHT,
			1,
			1

		)
		


	def agregar_boton(self):
		self.boton = Gtk.Button('Agregar')
		self.contenedor.attach_next_to(
			self.boton,
			self.entrada,
			Gtk.PositionType.BOTTOM,
			1,
			1
		)
		self.boton.connect('clicked', self.agregar_fila)
    
	def agregar_lista(self):

	    self.modelo = Gtk.ListStore(str, float)
	    self.modelo.append(['Valor1', 1.5])

	    self.lista_arvhivos = Gtk.TreeView(self.modelo)

	    descripcion = Gtk.CellRendererText()
	    columna_descripcion = Gtk.TreeViewColumn(
	    	'Descripcion', 
	    	descripcion, 
	    	text=0
	    )

	    monto = Gtk.CellRendererText()
	    columna_monto = Gtk.TreeViewColumn('Monto', monto, text=1)

	    self.lista_arvhivos.append_column(columna_descripcion)
	    self.lista_arvhivos.append_column(columna_monto)

	    self.contenedor.attach_next_to(
	    	self.lista_arvhivos,
	    	self.boton,
	    	Gtk.PositionType.BOTTOM,
	    	1,
	    	1
	    )
	    self.modelo.append(['valor 2',2.0])

	def agregar_fila(self, btn):
		texto = self.entrada.get_text()
		monto = self.entrada_monto.get_text()
		self.modelo.append([texto, float(monto)])
	


if __name__ == '__main__':
	ventana = Mi_Ventana()
	ventana.show_all()
	Gtk.main()