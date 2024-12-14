class Zona():
    def __init__(self, nombre, zoo) -> None:
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []
    
    def agreagarAnimales(self,animal):
        self._animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self._animales)