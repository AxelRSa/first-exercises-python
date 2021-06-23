class Camion:
    def __init__(self, tanque, rendimientoKilometros):
        self.tanque = tanque
        self.rendimientoKilometros = rendimientoKilometros

    def rendimientoTanque(self):
        return self.rendimientoKilometros / self.tanque
    def costoXKilometro(self, gasolinaPrecio):
        return self.rendimientoTanque() / gasolinaPrecio

print("Este es un programa que te ayuda a saber cuánto dinero te vas a gastar en gasolina según el camión que manejes de un punto a otro")
tanque = int(input("Introduce la cantidad de litros de tu tanque: "))
rendimientoKilometros = int(input("Introduce la cantidad de kilómetros que te rinde un tanque lleno: "))
gasolinaPrecio = float(input ("Introduce el precio de la gasolina: "))
distancia = float(input("Introduce la distancia que deseas recorrer en kilómetros: "))

camion = Camion(tanque, rendimientoKilometros)

print("\nTu camión tiene un rendimiento de " + str(round(camion.rendimientoTanque(),2)) + " kilómetros por litro de gasolina.\nCada kilómetro cuesta: $" + str(round(camion.costoXKilometro(gasolinaPrecio),2)) + "\nRecorrer la distancia de " + str(distancia) + " kilómetros te costaría un aproximado de: $" + str(round((distancia)*(camion.costoXKilometro(gasolinaPrecio)))) + "\nNecesitarás " + str(round(distancia/camion.rendimientoKilometros,2)) + " tanques para llegar a tu destino." )