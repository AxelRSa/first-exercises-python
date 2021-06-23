class Triangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def area(self):
        return (self.base * self.altura) / 2

print("Este programa funciona para sacar el área de dos triángulos y sumarlas")

base1 = int(input("Introduce la base del primer triángulo: "))
altura1 = int(input("Introduce la altura del primer triángulo: "))
base2 = int(input("Introduce la base del segundo triángulo: "))
altura2 = int(input("Introduce la altura del segundo triángulo: "))

triangulo1 = Triangulo(altura1, base1)
triangulo2 = Triangulo(altura2, base2)

print("\nEl área del primer triángulo es: " + str(triangulo1.area()) + " metros cuadrados.\nEl área del segundo triángulo es: " + str(triangulo2.area()) + " metros cuadrados.\nSu área sumada es: " + str(triangulo1.area() + triangulo2.area()) + " metros cuadrados")

