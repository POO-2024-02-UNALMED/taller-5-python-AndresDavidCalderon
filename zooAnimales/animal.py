from mamifero import Mamifero
from ave import Ave
from reptil import Reptil
from pez import Pez
from anfibio import Anfibio

class Animal:

    _totalAnimales=0

    def __init__(self, nombre, edad, habitat, genero) -> None:
        self. _nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal._totalAnimales+=1
    
    @classmethod
    def totalPorTipo():
        return f"Mamiferos: {Mamifero.cantidadMamiferos()}\nAves: {Ave.cantidadAves()}\nReptiles: {Reptil.cantidadReptiles()}\nPeces: {Pez.cantidadPeces()}\nAnfibios: {Anfibio.cantidadAnfibio()}"

    @classmethod
    def cantidadTotalAnimales(cls):
        return cls._totalAnimales
    
    def toString(self):
        presentacion = f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi género es {self._genero}"
        if self._zona!=None:
            presentacion+=f", la zona en la que me ubico es {self._zona} en el {self._zona.getZoo()}"
        return presentacion

    def movimiento(_self):
        return "desplazarse"