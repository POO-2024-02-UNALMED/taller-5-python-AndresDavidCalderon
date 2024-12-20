from . import animal

class Anfibio(animal.Animal):
    _listado = []
    ranas=0
    salamandras =0 

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    def movimiento(_self):
        return "saltar"
    
    @classmethod
    def crearRana(cls,nombre,edad,genero):
        cls.ranas+=1
        return Anfibio(nombre,edad,"selva",genero,"rojo",True)
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras+=1
        return Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)

    @classmethod
    def getRanas(cls):
        return cls.ranas

    @classmethod
    def getSalamandras(cls):
        return cls.salamandras
    
    def getColorPiel(self):
        return self._colorPiel

    def isVenenoso(self):
        return self._venenoso

    def setColorPiel(self,colorPiel):
        self._colorPiel=colorPiel
    
    def setVenenoso(self,venenoso):
        self._venenoso=venenoso
    