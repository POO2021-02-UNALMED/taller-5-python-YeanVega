class Zona:
    def __init__(self,nombre,zoo = None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def getNombre(self):
        return self.nombre

    def getZoo(self):
        return self.zoo

    def agregarAnimales(self,animal):
        self.animales.append(animal)
        
    def cantidadAnimales(self):
        resultado = self.animales
        return len(resultado)