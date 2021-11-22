from zooAnimales import Animal

class Zona(object):
   
    def __init__(self, nombre, zoo):
        self.__nombre = nombre
        self.__zoo = zoo

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def setZoo(self, zoo):
        self.__zoo = zoo

    def getZoo(self):
        return self.__zoo

    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def cantidadAnimales(self):
        return len(self.animales)
