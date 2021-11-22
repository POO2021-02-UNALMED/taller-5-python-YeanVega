from zooAnimales.animal import Animal
class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0
    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.listado.append(self)
    
    def isPelaje(self):
        return self.pelaje
    
    def getPatas(self):
        return self.patas
    
    @classmethod
    def cantidadMamiferos(cls):
        lista = cls.listado
        return len(lista)
    
    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        cls.caballos = cls.caballos +1
        return Mamifero(nombre,edad,"pradera",genero,True,4)
    
    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        cls.leones = cls.leones + 1
        return Mamifero(nombre,edad,"selva",genero,True,4)