'''Se hace referencia a algunos animales mediante las siguientes clases: 
a) Instanciar 1 Perro, 1 Gato y 1 Pájaro. 
b) Sobrecargar el método hacerSonido() para que cada animal emita su sonido 
característico. 
c) Implementar un método moverse() que indique cómo se mueve cada animal 
(correr, saltar, volar, etc.). '''
class Animal:
    def hacerSonido(self):
        pass

    def moverse(self):
        pass

class Perro(Animal):
    def hacerSonido(self):
        print("¡Guau!")

    def moverse(self):
        print("Corriendo")

class Gato(Animal):
    def hacerSonido(self):
        print("¡Miau!")

    def moverse(self):
        print("Saltando")

class Pajaro(Animal):
    def hacerSonido(self):
        print("¡Pío!")

    def moverse(self):
        print("Volando")

perro = Perro()
gato = Gato()
pajaro = Pajaro()

perro.hacerSonido()
perro.moverse()
gato.hacerSonido()
gato.moverse()
pajaro.hacerSonido()
pajaro.moverse()