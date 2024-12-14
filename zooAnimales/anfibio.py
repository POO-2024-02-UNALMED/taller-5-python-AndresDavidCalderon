from animal import Animal

class Anfibio(Animal):
    _listado = []
    _ranas=0
    _salamandras =0 

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
        cls._ranas+=1
        return Anfibio(nombre,edad,"selva",genero,"rojo",True)
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls._salamandras+=1
        return Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
