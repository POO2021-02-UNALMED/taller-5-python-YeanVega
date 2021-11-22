class Zoologico(object):
  
    def __init__(self, nombre, ubicacion):
        self.__nombre = nombre
        self.__ubicacion = ubicacion

    def agregarZonas(self, zona):
        self.__zonas.append(zona)

    def cantidadTotalAnimales(self):
        cantidad = 0
        i = 0
        while i < len(self.__zonas):
            cantidad += len(self.__zonas[i].animales)
            i += 1
        return cantidad

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getUbicacion(self):
        return self.__ubicacion

    def setUbicacion(self, ubicacion):
        self.__ubicacion = ubicacion

    def getZonas(self):
        return self.__zonas

    def setZonas(self, zonas):
        self.__zonas = zonas


