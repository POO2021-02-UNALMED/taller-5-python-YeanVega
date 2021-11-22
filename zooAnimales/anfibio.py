from zooAnimales.animal import Animal

class Anfibio(Animal):
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.__colorPiel = colorPiel
        self.__venenoso = venenoso
        __listado.append(self)

    def setColorPiel(self, colorPiel):
        self.__colorPiel = colorPiel

    def getColorPiel(self):
        return self.__colorPiel

    def setVenenoso(self, venenoso):
        self.__venenoso = venenoso

    def isVenenoso(self):
        return self.__venenoso

    def movimiento(self):
        return "saltar"

    @staticmethod
    def cantidadAnfibios():
        return len(__listado)

    @staticmethod
    def crearRana(nombre, edad, genero):
        ranas += 1
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        return rana

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        salamandras += 1
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        return salamandra