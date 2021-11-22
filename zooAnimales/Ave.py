class Ave(Animal):
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.__colorPlumas = colorPlumas
        __listado.append(self)

    def setColorPlumas(self, colorPlumas):
        self.__colorPlumas = colorPlumas

    def getColorPlumas(self):
        return self.__colorPlumas

    def movimiento(self):
        return "volar"

    @staticmethod
    def cantidadAves():
        return len(__listado)

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        halcones += 1
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        return halcon

    @staticmethod
    def crearAguila(nombre, edad, genero):
        aguilas += 1
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        return aguila