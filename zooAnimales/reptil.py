from zooAnimales.animal import Animal

class Reptil(Animal):

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.__colorEscamas = colorEscamas
        self.__largoCola = largoCola
        __listado.append(self)


    def setColorEscamas(self, colorEscamas):
        self.__colorEscamas = colorEscamas

    def getColorEscamas(self):
        return self.__colorEscamas

    def setLargoCola(self, largoCola):
        self.__largoCola = largoCola

    def getLargoCola(self):
        return self.__largoCola

    def movimiento(self):
        return "reptar"

    @staticmethod
    def cantidadReptiles():
        return len(__listado)

    @staticmethod
    def crearIguana(nombre, edad, genero):
        iguanas += 1
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        return iguana

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        serpientes += 1
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        return serpiente