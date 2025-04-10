''' Crea una clase Coche con marca, modelo y velocidad 
a) Agrega un método acelerar () que aumente la velocidad en 10 
b) Agrega un método frenar () que disminuya la velocidad en 5 
c) Crea dos coches, aceléralos, frénalos y muestra sus velocidades'''
class Coche:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 10
        return self.velocidad

    def frenar(self):
        self.velocidad -= 5
        return self.velocidad

c1 = Coche('Toyota', 1999, 100)
print(f'El coche esta acelerando : {c1.acelerar()} km')
print(f'El coche esta frenando : {c1.frenar()} km')
print()
c2 = Coche('Honda ', 2020, 130)
print(f'El coche esta acelerando : {c2.acelerar()} km')
print(f'El coche esta frenando : {c2.frenar()} km')