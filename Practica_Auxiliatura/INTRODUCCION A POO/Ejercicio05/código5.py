'''Crea una clase Estudiante con nombre, nota_1, nota_2 
a) Agrega un método para calcular el promedio 
b) Agrega un método para verificar si aprobó (promedio >=6) 
c) Crea tres estudiantes, muestra sus promedios y si aprobaron'''
class Estudiante:
    def __init__(self, nombre, nota_1, nota_2):
        self.nombre = nombre
        self.nota_1 = nota_1
        self.nota_2 = nota_2

    def calcularPromedio(self):
        return (self.nota_1 + self.nota_2)/2

    def verificarNota(self):
        if(self.calcularPromedio() >= 6):
            print(f'{self.nombre} Aprrobo\nPromedio: {self.calcularPromedio()}')
        else:
            print(f'{self.nombre} Reprobo\nPromedio: {self.calcularPromedio()}')

e1 = Estudiante('Jose', 8, 7)
e1.verificarNota()
print()
e2 = Estudiante('Maria', 2, 6)
e2.verificarNota()
print()
e3 = Estudiante('Andres', 3, 10)
e3.verificarNota()