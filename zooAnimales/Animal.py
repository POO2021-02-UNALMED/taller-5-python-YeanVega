from gestion import Zona

class Animal(object):
    __totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        __totalAnimales += 1

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def setHabitat(self, habitat):
        self.habitat = habitat

    def getHabitat(self):
        return self.habitat

    def setGenero(self, genero):
        self.genero = genero

    def getGenero(self):
        return self.genero

    def setZona(self, zona):
        self.__zona = zona

    def getZona(self):
        return self.__zona

    @staticmethod
    def totalPorTipo():
        return "Mamiferos: " + Mamifero.cantidadMamiferos() + "\nAves: " + Ave.cantidadAves() + "\nReptiles: " + Reptil.cantidadReptiles() + "\nPeces: " + Pez.cantidadPeces() + "\nAnfibios: " + Anfibio.cantidadAnfibios()

    def toString(self):
        if self.__zona is None:
            return "Mi nombre es " + self.nombre + ", tengo una edad de " + self.edad + ", habito en " + self.habitat + " y mi genero es " + self.genero
        else:
            return "Mi nombre es " + self.nombre + ", tengo una edad de " + self.edad + ", habito en " + self.habitat + " y mi genero es " + self.genero + ", la zona en la que me ubico es " + self.__zona + ", en el " + self.__zona.getZoo().getNombre()

    def movimiento(self):
        return "desplazarse"
