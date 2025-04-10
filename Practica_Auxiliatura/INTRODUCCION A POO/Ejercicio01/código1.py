'''Crea una clase Persona con nombre, edad y ciudad 
a) Agrega un método para mostrar el saludo: “Hola, soy {nombre} de {ciudad}” 
b) Crea tres personas y muestra su saludo 
c) Agrega un método para verificar si es mayor de edad'''

class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad 
        self.ciudad = ciudad

    def saludo(self):
        print(f'Hola, soy {self.nombre} de {self.ciudad}')

    def verificarEdad(self):
        if(self.edad >=  18):
            print(f'{self.nombre} es mayor de edad')
        else:
            print(f'{self.nombre} es menor de edad')

p1 = Persona('Marcos', 21, 'La Paz')
p1.saludo()
p1.verificarEdad()
print()
p2 = Persona('Maria', 15, 'Oruro')
p2.saludo()
p2.verificarEdad()
print()
p3 = Persona('Roberto', 19, 'Pando')
p3.saludo()
p3.verificarEdad()