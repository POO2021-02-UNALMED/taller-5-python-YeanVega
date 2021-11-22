from zooAnimales.animal import Animal
class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        Anfibio.listado.append(self)
    
    def getColorPiel(self):
        return self.colorPiel
    
    def isVenenoso(self):
        return self.venenoso
    
    def movimiento(self):
        pass
    
    @classmethod
    def cantidadAnfibios(cls):
        lista = cls.listado
        return len(lista)
    
    @classmethod
    def crearRana(cls,nombre,edad,genero):
        cls.ranas = cls.ranas +1
        return Anfibio(nombre, edad,"selva",genero,"rojo",True)
    
    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        cls.salamandras = cls.salamandras +1
        return Anfibio(nombre,edad,"selva",genero,"negro y amarillo", False)
