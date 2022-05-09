from Cuadrado import Cuadrado


if __name__ == '__main__':
    mi_cuadrado=Cuadrado([5,4],6)
    print(mi_cuadrado.calcular_area())
    mi_cuadrado.mover([0,0])
    print(mi_cuadrado.get_centro())
    mi_cuadrado.cambiar_lado(5)
    print(mi_cuadrado.calcular_area())