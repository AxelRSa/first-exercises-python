import math
class Auto:

    def __init__(self, nombre):
        self.nombre = nombre
        self.xpos = 0
        self.ypos = 0

    def irArriba(self, q):
        self.ypos += q
    def irAbajo(self, q):
        self.ypos -= q
    def irIzquierda(self, q):
        self.xpos -= q
    def irDerecha(self, q):
        self.xpos += q

    def getPos(self):
        return("(" + str(self.xpos) + "," + str(self.ypos) + ")")

def getDis(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

print("Este es un programa que te permite lanzar dos carros y moverlos en un plano cartesioano y luego calcular la distancia a la que se encuentra uno del otro")

nombreCarro1 = input("Introduce el nombre del primer carro: ")
nombreCarro2 = input("Introduce el nombre del segundo carro: ")

carro1 = Auto(nombreCarro1)
carro2 = Auto(nombreCarro2)

carro1.irDerecha(int(input("¿Cuántos metros a la derecha quieres que se mueva " + carro1.nombre + "? ")))
carro1.irIzquierda(int(input("¿Cuántos metros a la izquierda quieres que se mueva " + carro1.nombre + "? ")))
carro1.irArriba(int(input("¿Cuántos metros hacia arriba quieres que se mueva " + carro1.nombre + "? ")))
carro1.irAbajo(int(input("¿Cuántos metros hacia abajo quieres que se mueva " + carro1.nombre + "? ")))

carro2.irDerecha(int(input("¿Cuántos metros a la derecha quieres que se mueva " + carro2.nombre + "? ")))
carro2.irIzquierda(int(input("¿Cuántos metros a la izquierda quieres que se mueva " + carro2.nombre + "? ")))
carro2.irArriba(int(input("¿Cuántos metros hacia arriba quieres que se mueva " + carro2.nombre + "? ")))
carro2.irAbajo(int(input("¿Cuántos metros hacia abajo quieres que se mueva " + carro2.nombre + "? ")))

print("\n" + carro1.nombre + " se encuentra en la posición " + carro1.getPos() + "\n" + carro2.nombre + " se encuentra en la posición " + carro2.getPos() + "\n" + carro1.nombre + " se encuentra a " + str(round(getDis(carro1.xpos, carro1.ypos, carro2.xpos, carro2.ypos),2)) + " metros de distancia de " + carro2.nombre)