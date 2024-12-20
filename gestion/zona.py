class Zona():
    def __init__(self, nombre, zoo=None) -> None:
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []
    
    def agregarAnimales(self,animal):
        self._animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self._animales)
    
    def getNombre(self):
        return self._nombre

    def getZoo(self):
        return self._zoo
    
    def getAnimales(self):
        return self._animales
    
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setZoo(self,zoo):
        self._zoo=zoo

    def setAnimales(self,animales):
        self._animales=animales