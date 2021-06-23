class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, nombre, matricula):
        self.matricula = matricula
        Persona.__init__(self, nombre)

    def acceso(self):
        print("Estudiante " + self.nombre + " tu matricula es: " + str(self.matricula) + " y tienes acceso a la biblioteca todos los días.")

class Ciudadano(Persona):
    def __init__(self,nombre, curp):
        self.curp = curp
        Persona.__init__(self,nombre)
    def acceso(self):
        print("Ciudadano " + self.nombre + " tu CURP es: " + self.curp + " y tienes acceso a la biblioteca solo los sábados")

def acceso(estado):
    estado.acceso()

print("Este es un programa que clasifica a estudiantes y personas que no lo son y a cada uno le da características especiales y se intenta practicar con el poliformismo")
nombre = input("Introduce tu nombre: ")
estado = int(input("Introduce un número según tu condición\n1 = si eres estudiante\n2 = si no estudias\n"))

if estado == 1:
    matricula = input(str("Introduce tu matrícula: "))
    persona = Estudiante(nombre, matricula)
    acceso(persona)
else:
    curp = input(str("introduce tu CURP: "))
    persona = Ciudadano(nombre, curp)
    acceso(persona)




