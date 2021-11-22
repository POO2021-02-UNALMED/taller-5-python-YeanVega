class Animal:
    def __init__(self,nombre,edad,habitat,genero):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = None
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        self.totalAnimales = Mamifero.cantidadMamiferos() + Ave.cantidadAves() + Reptil.cantidadReptiles() + Pez.cantidadPeces() + Anfibio.cantidadAnfibios()
    
    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad
    
    def getHabitat(self):
        return self.habitat
    
    def getGenero(self):
        return self.genero
    
    def __str__(self):
        from gestion.zona import Zona
        if self.zona != None:
            return "Mi nombre es " + str(self.nombre) + ", tengo una edad de " + str(self.edad) + ", habito en " + str(self.habitat) + " y mi genero es " + str(self.genero) + ", la zona en la que me ubico es " +  str(self.zona.getNombre()) + ", en el " + str(self.zona.getZoo().getNombre())
        else:
            return "Mi nombre es " + str(self.nombre) + ", tengo una edad de " + str(self.edad) + ", habito en " + str(self.habitat) + " y mi genero es " + str(self.genero) 
    
    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return "Mamiferos : " + str(Mamifero.cantidadMamiferos())+"\n" + "Aves : " + str(Ave.cantidadAves()) + "\n" + "Reptiles : " + str(Reptil.cantidadReptiles()) + "\n" + "Peces : " + str(Pez.cantidadPeces()) + "\n"+ "Anfibios : " + str(Anfibio.cantidadAnfibios())
    
    def movimiento(self):
        pass

