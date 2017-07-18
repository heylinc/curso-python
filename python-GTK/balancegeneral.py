import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Mi_Ventana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		
		super(Mi_Ventana, self).__init__(*args, **kwargs)
		self.set_size_request(500, 300)
		#self.connect('delete-event', Gtk.main_quit)

		self.agregar_contenedor()
		self.agregar_entrada()
		self.agregar_entrada2()
		self.agregar_boton()
		self.agregar_boton2()
		self.agregar_lista()
		self.agregar_lista2()

	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
		self.entrada_monto = Gtk.Entry()
		self.contenedor.attach(self.entrada, 0, 0, 3, 1)
		self.contenedor.attach_next_to(
			self.entrada_monto,
			self.entrada,
			Gtk.PositionType.RIGHT,
			1,
			1	

		)
	def agregar_entrada2(self):
		self.entrada2 = Gtk.Entry()
		self.entrada_monto2 = Gtk.Entry()

		self.contenedor.attach(self.entrada2, 0, 1, 3, 1)
		self.contenedor.attach_next_to(
			self.entrada_monto2,
			self.entrada2,
			Gtk.PositionType.RIGHT,
			1,
			1	

		)

		


	def agregar_boton(self):
		self.boton = Gtk.Button('Activos')
		self.contenedor.attach_next_to(
			self.boton,
			self.entrada2,
			Gtk.PositionType.BOTTOM,
			2,
			2
		)
	def agregar_boton2(self):
		self.boton2 = Gtk.Button('Agregar Pasivos')
		self.contenedor.attach_next_to(
			self.boton2,
			self.entrada2,
			Gtk.PositionType.BOTTOM,
			4,
			2
		)
	
		self.boton.connect('clicked', self.agregar_fila)
		self.boton2.connect('clicked', self.agregar_fila2)
		#self.botonsumactivo.connect('clicked', self.sumarlosactivos)
    
	def agregar_lista(self):

	    self.modelo = Gtk.ListStore(str, float)
	    #self.modelo.append(['Valor1', 1.5])

	    self.lista_arvhivos = Gtk.TreeView(self.modelo)

	    descripcion = Gtk.CellRendererText()
	    columna_descripcion = Gtk.TreeViewColumn(
	    	'Descripcion', 
	    	descripcion, 
	    	text=1
	    )

	    monto = Gtk.CellRendererText()
	    columna_monto = Gtk.TreeViewColumn('Monto', monto, text=0)

	    self.lista_arvhivos.append_column(columna_descripcion)
	    self.lista_arvhivos.append_column(columna_monto)

	    self.contenedor.attach_next_to(
	    	self.lista_arvhivos,
	    	self.boton,
	    	Gtk.PositionType.BOTTOM,
	    	2,
	    	2
	    )
	def agregar_lista2(self):

	    self.modelo2 = Gtk.ListStore(str, float)
	    #self.modelo.append(['Valor1', 1.5])

	    self.lista_arvhivos2 = Gtk.TreeView(self.modelo2)

	    descripcion2 = Gtk.CellRendererText()
	    columna_descripcion2 = Gtk.TreeViewColumn(
	    	'Descripcion', 
	    	descripcion2, 
	    	text=1
	    )

	    monto2 = Gtk.CellRendererText()
	    columna_monto2 = Gtk.TreeViewColumn('Monto', monto2, text=0)

	    self.lista_arvhivos2.append_column(columna_descripcion2)
	    self.lista_arvhivos2.append_column(columna_monto2)

	    self.contenedor.attach_next_to(
	    	self.lista_arvhivos2,
	    	self.lista_arvhivos,
	    	Gtk.PositionType.RIGHT,
	    	2,
	    	2
	    )
	    #self.modelo.append(['valor 2',2.0])

	def agregar_fila(self, btn):
		texto = self.entrada.get_text()
		monto = self.entrada_monto.get_text()
		self.modelo.append([texto, float(monto)])

	def agregar_fila2(self, btn):
		texto2 = self.entrada2.get_text()
		monto2 = self.entrada_monto2.get_text()
		self.modelo2.append([texto2, float(monto2)])

	
		

if __name__ == '__main__':
	ventana = Mi_Ventana()
	ventana.show_all()
	Gtk.main()