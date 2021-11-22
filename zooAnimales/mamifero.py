from zooAnimales.animal import Animal

class Mamifero(Animal):

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.__pelaje = pelaje
        self.__patas = patas
        __listado.append(self)


    def setPelaje(self, pelaje):
        self.__pelaje = pelaje

    def isPelaje(self):
        return self.__pelaje

    def setPatas(self, patas):
        self.__patas = patas

    def getPatas(self):
        return self.__patas

    @staticmethod
    def cantidadMamiferos():
        return len(__listado)

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        caballos += 1
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        return caballo

    @staticmethod
    def crearLeon(nombre, edad, genero):
        leones += 1
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        return leon
