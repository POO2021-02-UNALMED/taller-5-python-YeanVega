
class Zoologico:
    def __init__(self,nombre,ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def getNombre(self):
        return self.nombre

    def getUbicacion(self):
        return self.ubicacion

    def agregarZonas(self,zona):
        self.zonas.append(zona)

    def getZona(self):
        return self.zonas 


    def cantidadTotalAnimales(self):
        Suma = 0
        for i in range(0,len(self.zonas)):
            Suma = Suma + self.zonas[i].cantidadAnimales()
        return Suma


