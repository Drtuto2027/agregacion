class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Clase:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def listar_estudiantes(self):
        print(f"Estudiantes en la clase {self.nombre}:")
        if not self.estudiantes:
            print("No hay estudiantes en esta clase.")
        for estudiante in self.estudiantes:
            print(f" - {estudiante}")

# Crear estudiantes
estudiante1 = Estudiante("Juan Pérez")
estudiante2 = Estudiante("Ana Gómez")
estudiante3 = Estudiante("Luis Martínez")

# Crear una clase
clase1 = Clase("Matemáticas")

# Agregar estudiantes a la clase
clase1.agregar_estudiante(estudiante1)
clase1.agregar_estudiante(estudiante2)

# Listar estudiantes de la clase
clase1.listar_estudiantes()

# Crear otra clase y agregar otro estudiante
clase2 = Clase("Ciencias")
clase2.agregar_estudiante(estudiante3)
clase2.listar_estudiantes()

# Los estudiantes pueden existir sin una clase
print(estudiante1)  # Juan Pérez
print(estudiante2)  # Ana Gómez
print(estudiante3)  # Luis Martínez
