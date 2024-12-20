from . import animal

class Mamifero(animal.Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        cls.caballos+=1
        return Mamifero(nombre,edad,"pradera",genero,True,4)
    
    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        cls.leones+=1
        return Mamifero(nombre,edad,"selva",genero,True,4)
    
    @classmethod
    def getCaballos(cls):
        return cls.caballos
    
    @classmethod
    def getLeones(cls):
        return cls.leones
    
    @classmethod
    def getListado(cls):
        return cls._listado

    def isPelaje(self):
        return self._pelaje
    
    def getPatas(self):
        return self._patas

    def setPelaje(self,pelaje):
        self._pelaje=pelaje
    
    def setPatas(self,patas):
        self._patas=patas