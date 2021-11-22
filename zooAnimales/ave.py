from zooAnimales.animal import Animal
class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.colorPlumas = colorPlumas
        Ave.listado.append(self)
    
    def getColorPlumas(self):
        return self.colorPlumas

    def movimiento(self):
        pass

    @classmethod
    def cantidadAves(cls):
        lista = cls.listado
        return len(lista)

    @classmethod
    def crearHalcon(cls,nombre,edad, genero):
        cls.halcones = cls.halcones + 1
        return Ave(nombre,edad,"montanas",genero,"cafe glorioso")

    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        cls.aguilas = cls.aguilas +1
        return Ave(nombre,edad,"montanas",genero,"blanco y amarillo")

    def toString(self):
        return "Mi nombre es " + str(self.nombre) + ", tengo una edad de " + str(self.edad) + ", habito en "+ str(self.habitat) + " y mi genero es " + str(self.genero)
    