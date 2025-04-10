'''Para los bloques del juego Minecraft se usará los siguientes objetos: 
Carrera de Informática - UMSA 
Página 6 
INF -121 PROGRAMACION II 
a) Crear e instanciar al menos 2 bloques de cada tipo 
b) Sobrescribe accion() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando 
distintos mensajes según el tipo de bloque. 
c) Sobrecarga colocar() para permitir colocar un bloque en diferentes 
orientaciones (por ejemplo, en el suelo o en la pared). 
d) Sobrescribe romper() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando 
distintos mensajes según el tipo de bloque y que puede suceder al romperlos.'''
class Bloque:
    def accion(self):
        pass

    def romper(self):
        pass

class BloqueCofre(Bloque):
    def accion(self):
        print("Abriendo cofre...")

    def romper(self):
        print("¡Cuidado! El cofre puede contener objetos")

class BloqueTnt(Bloque):
    def accion(self):
        print("¡Explosión inminente!")

    def romper(self):
        print("¡BOOM! La TNT explotó")

class BloqueHorno(Bloque):
    def accion(self):
        print("Fundiendo materiales...")

    def romper(self):
        print("El horno se ha roto")

cofre = BloqueCofre()
tnt = BloqueTnt()
horno = BloqueHorno()

cofre.accion()
cofre.romper()
tnt.accion()
tnt.romper()
horno.accion()
horno.romper()