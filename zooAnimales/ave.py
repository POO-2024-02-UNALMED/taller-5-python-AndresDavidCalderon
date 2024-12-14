from . import animal

class Ave(animal.Animal):
    _listado=[]
    halcones = 0
    aguilas =0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas;
        Ave._listado.append(self)
    
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    def movimiento(_self):
        return "volar"

    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        cls.halcones+=1
        return Ave(nombre,edad,"montañas",genero,"cafe glorioso")
    
    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        cls.aguilas+=1
        return Ave(nombre,edad,"montañas",genero,"blanco y amarillo")
    
    @classmethod
    def getHalcones(cls):
        return cls.halcones
    
    @classmethod
    def getAguilas(cls):
        return cls.aguilas

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self,colorPlumas):
        self._colorPlumas=colorPlumas