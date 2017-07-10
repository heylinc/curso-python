import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
    def __init__(self, *args, **kwargs):
        super(MiVentana, self).__init__(*args, **kwargs)
        self.set_default_size(500, 300)
        self.connect('delete-event', Gtk.main_quit)

    def agregar_contenedor(self):
        self.contenedor = Gtk.Grid()

if __name__ == '__main__':

    ventana = MiVentana()
    ventana = Gtk.Window(title = 'Variados')
    ventana.connect('delete-event', Gtk.main_quit)
    texto = Gtk.Entry()
    texto.get_text()
    boton = Gtk.Button('Boton')
    label = Gtk.Label()
    label.set_markup('Texto a agregar')

    contenedor = Gtk.Grid()
    contenedor.set_column_homogeneous(True)
    contenedor.set_row_homogeneous(False)
    
    contenedor.attach(texto, 0, 0, 3, 1)
    contenedor.attach(boton, 1, 1, 1, 1)
    contenedor.attach(label, 0, 4, 1, 1)

    ventana.add(contenedor)
    #ventana.add(texto)
    #ventana.add(boton)
    #ventana.add(label)
    ventana.show_all()

    Gtk.main()

	ventana = Miventana()


	
	ventana.show_all()

	Gtk.main()