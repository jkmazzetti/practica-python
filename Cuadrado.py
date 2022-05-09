from Figura import Figura
import math


class Cuadrado(Figura):
    def __init__(self, centro,lado):
        super().__init__(centro)
        self.__lado=lado

    def calcular_area(self):
        return math.pow(self.__lado,2)
    def cambiar_lado(self,nuevo_valor):
        self.__lado=nuevo_valor