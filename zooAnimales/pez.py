class Pez(Animal):

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.__colorEscamas = colorEscamas
        self.__cantidadAletas = cantidadAletas
        __listado.append(self)

    def setColorEscamas(self, colorEscamas):
        self.__colorEscamas = colorEscamas

    def getColorEscamas(self):
        return self.__colorEscamas

    def setCantidadAleas(self, cantidadAletas):
        self.__cantidadAletas = cantidadAletas

    def getCantidadAletas(self):
        return self.__cantidadAletas

    def movimiento(self):
        return "nadar"

    @staticmethod
    def cantidadPeces():
        return len(__listado)

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        salmones += 1
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        return salmon

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        bacalaos += 1
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        return bacalao