from animal import Animal

class Pez(Animal):
    _listado = []
    _salmones = 0
    _bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    
    def movimiento(_self):
        return "nadar"
    
    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        cls._salmones+=1
        return Pez(nombre,edad,"oceano",genero,"rojo",6)
    
    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        cls._bacalaos+=1
        return Pez(nombre,edad,"oceano",genero,"gris",6)