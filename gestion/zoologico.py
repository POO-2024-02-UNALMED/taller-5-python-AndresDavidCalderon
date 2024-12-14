class Zoologico:
    def __init__(self, nombre, ubicacion) -> None:
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
    
    def agregarZonas(self,zona):
        self._zonas.append(zona)
    
    def cantidadTotalAnimales(self):
        total = 0
        for i in self._zonas:
            total+=i.cantidadAnimales()
        return i