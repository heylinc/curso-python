class Mascota(object):

    def __init__(self,nombre, bebida = 'Leche' , comida = 'Galletas'):
        self.nombre = nombre
        self.bebida = bebida
        self.comida = comida
    def obtener_nombre(self):
        return self.nombre
        
    def obtener_bebida(self):
        print 'Tienen de bebiba en comun:'
        return self.bebida
    
    def obtener_comida(self):
        print 'Tiene de Alimento en comun:'
        return self.comida

class Perro(Mascota):

    def __init__(self, raza, nombre):
        super(Perro, self).__init__(nombre)
        self.raza = raza
        

    def obtener_raza(self):
        
        return 'La raza de mi perro es: ' + self.raza
    
    def obtener_nombre(self):
        
        return 'El nombre de mi perro es: ' + self.nombre
class Gato(Mascota):

    def __init__(self, raza, nombre):
        super(Gato, self).__init__(nombre)
        self.raza = raza
        

    def obtener_raza(self):
        
        return 'La raza de mi gato es: ' + self.raza
    
    def obtener_nombre(self):
        
        return 'El nombre de mi gato es: ' + self.nombre



if __name__ == '__main__':
    p = Perro("Doberman", "Doggi")
    c = Gato("Antano", "Katitu")
    
    print p.obtener_nombre()
    print c.obtener_nombre()
    print p.obtener_raza()
    print c.obtener_raza()
    print p.obtener_comida()
    print p.obtener_bebida()