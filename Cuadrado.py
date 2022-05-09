from Figura import Figura
import math

class Cuadrado(Figura):

    def __init__(self, centro,lado):
        super().__init__(centro)
        self.__lado=lado

    def calcular_area(self):
        return round(math.pow(self.__lado,2),2)

    def cambiar_lado(self,nuevo_valor):
        self.__lado=nuevo_valor

    def perimetro(self):
        return round(self.__lado*4,2)
        
    def diagonal(self):
        return round(self.__lado*math.sqrt(2),2)