from zooAnimales.animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        Reptil.listado.append(self)

    def getColorEscamas(self):
        return self.colorEscamas

    def getLargoCola(self):
        return self.largoCola

    def movimiento(self):
        pass

    @classmethod
    def cantidadReptiles(cls):
        lista = cls.listado
        return len(lista)

    @classmethod
    def crearIguana(cls,nombreIguana,edadIguana,generoIguana):
        cls.iguanas = cls.iguanas +1
        return Reptil(nombreIguana,edadIguana,"humedal",generoIguana,"verde",3)
        
    @classmethod
    def crearSerpiente(cls,nombreSerpiente,edadSerpiente,generoSerpiente):
        cls.serpientes = cls.serpientes + 1
        return Reptil(nombreSerpiente,edadSerpiente,"jungla",generoSerpiente,"blanco",1)
    