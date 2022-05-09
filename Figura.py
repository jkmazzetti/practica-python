from abc import ABC, abstractmethod
class Figura(ABC):
    def __init__(self, centro):
        self.__centro = centro

    @abstractmethod
    def calcular_area(self):
       pass
    def mover(self,nueva_posicion):
        self.__centro=nueva_posicion
    def get_centro(self):
        return self.__centro






