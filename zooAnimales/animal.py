

class Animal:

    _totalAnimales=0

    def __init__(self, nombre, edad, habitat, genero) -> None:
        self. _nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales+=1
    
    @classmethod
    def totalPorTipo(cls):
        from . import mamifero
        from . import ave
        from . import reptil
        from . import pez
        from . import anfibio
        return f"Mamiferos: {mamifero.Mamifero.cantidadMamiferos()}\nAves: {ave.Ave.cantidadAves()}\nReptiles: {reptil.Reptil.cantidadReptiles()}\nPeces: {pez.Pez.cantidadPeces()}\nAnfibios: {anfibio.Anfibio.cantidadAnfibio()}"

    @classmethod
    def cantidadTotalAnimales(cls):
        return cls._totalAnimales
    
    def toString(self):
        presentacion = f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi género es {self._genero}"
        if self._zona!=None:
            presentacion+=f", la zona en la que me ubico es {self._zona} en el {self._zona.getZoo()}"
        return presentacion

    def movimiento(_self):
        return "desplazarse"

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero
    
    def setNombre(self,nombre):
        self._nombre=nombre
    
    def setEdad(self,edad):
        self._edad=edad
    
    def setHabitat(self,habitat):
        self._habitat=habitat
    
    def setGenero(self,genero):
        self._genero=genero