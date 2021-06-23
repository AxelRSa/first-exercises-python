if estado == 1:
    matricula = input("Hola, introduce tu matrícula: ")
    persona = Estudiante(nombre, matricula)
    persona.acceso()
else:
    curp = input("Hola, introduce tu CURP: ")
    persona = Ciudadano(nombre, curp)
    persona.acceso()