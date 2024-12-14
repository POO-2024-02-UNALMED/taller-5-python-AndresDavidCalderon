from animal import Animal;

class Reptil(Animal):
    _listado = []
    _iguanas = 0
    _serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil._listado.append(self)
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    def movimiento(_self):
        return "reptar"

    @classmethod
    def crearIguana(cls,nombre,edad,genero):
        cls._iguanas+=1
        return Reptil(nombre,edad,"humedal",genero,"blanco",1)

    @classmethod
    def crearSerpiente(cls,nombre,edad,genero):
        cls._serpientes+=1
        return Reptil(nombre,edad,"jungla",genero,"blanco",1)
    