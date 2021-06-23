class Sillon:
    def __init__(self, nombre, color, base, ancho, altura, precio, cojines):
        self.nombre = nombre
        self.color = color
        self.base = base
        self.ancho = ancho
        self.altura = altura
        self.precio = precio
        self.cojines = cojines

    def area(self):
        return int(self.base) * int(self.ancho)
    def volumen(self):
        return int(self.base) * int(self.altura) * int(self.ancho)

print("Este es un programa que te permite registrar un sillón con sus características y luego imprimirlo en pantalla.")

nombre = input("Introduce el nombre del sillón: ")
color = input("Introduce el color del sillón: ")
base = input("Introduce la base en cm del sillón: ")
ancho = input("Introduce el ancho en cm del sillón: ")
altura = input("Introduce la altura en cm del sillón: ")
precio = input("Introduce el precio del sillón en pesos mexicanos: ")
cojines = 0

while (cojines < 1) or (cojines > 2):
    cojines = int(input("Introduce si el sillón tiene cojines \n1 = Sí\n2 = No\n"))
    if (cojines < 1) or (cojines > 2):
        print("Error, debe de ser entre 1 y 2 \n")
    else:
        pass
if cojines == 1:
    cojines = "Sí"
else:
    cojines = "No"

sillon = Sillon(nombre, color, base, ancho, altura, precio, cojines)

print("\nLas características del sillón " + sillon.nombre + " son:\nNombre: " + sillon.nombre + "\nColor: " + sillon.color + "\nBase(cm): " + sillon.base + "\nAncho(cm): " + ancho + "\nAltura(cm): " + sillon.altura + "\nÁrea(cm2): " + str(sillon.area()) + "\nVolumen(cm3): " + str(sillon.volumen()) + "\nCojines: " + sillon.cojines + "\nPrecio: $" + sillon.precio)