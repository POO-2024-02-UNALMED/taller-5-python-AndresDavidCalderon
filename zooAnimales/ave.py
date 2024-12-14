from animal import Animal

class Ave(Animal):
    _listado=[]
    _halcones = 0
    _aguilas =0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas;
        Ave._listado.append(self)
    
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    def movimiento(_self):
        return "volar"

    def crearHalcon(cls,nombre,edad,genero):
        cls._halcones+=1
        return Ave(nombre,edad,"montañas",genero,"cafe glorioso")
    
    def crearAguila(cls,nombre,edad,genero):
        cls._aguilas+=1
        return Ave(nombre,edad,"montañas",genero,"blanco y amarillo")
    