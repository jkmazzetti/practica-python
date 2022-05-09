from Cuadrado import Cuadrado

if __name__ == '__main__':
    mi_cuadrado=Cuadrado([5,4],6)
    print("Posición:",mi_cuadrado.get_centro())
    print("Área:",mi_cuadrado.calcular_area())
    print("Diagonal:", mi_cuadrado.diagonal())
    mi_cuadrado.cambiar_lado(5)
    mi_cuadrado.mover([0,5])
    print("Nueva posición:",mi_cuadrado.get_centro())
    mi_cuadrado.cambiar_lado(5)
    print("Nueva área:",mi_cuadrado.calcular_area())
    print("Nueva Diagonal:", mi_cuadrado.diagonal())