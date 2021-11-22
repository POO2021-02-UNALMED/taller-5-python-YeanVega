from zooAnimales.animal import Animal
class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,cantidadAletas):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        Pez.listado.append(self)

    def getColorEscamas(self):
        return self.colorEscamas

    def getCantidadAletas(self):
        return self.cantidadAletas

    def movimiento(self):
        pass

    @classmethod
    def cantidadPeces(cls):
        lista = cls.listado
        return len(lista)

    @classmethod
    def crearSalmon(cls,nombreSalmon,edadSalmon,generoSalmon):
        cls.salmones = cls.salmones + 1
        return Pez(nombreSalmon,edadSalmon,"oceano",generoSalmon,"rojo",6)
        
    @classmethod
    def crearBacalao(cls,nombreBacalao,edadBacalao,generoBacalao):
        cls.bacalaos = cls.bacalaos +1
        return Pez(nombreBacalao,edadBacalao,"oceano",generoBacalao,"gris",6)