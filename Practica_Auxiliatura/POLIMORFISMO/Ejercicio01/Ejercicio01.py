'''Sea la clase Videojuego: 
a) Instanciar al menos 2 videojuegos 
b) Sobrecargar el constructor 2 veces 
c) Implementar un método mostrar() 
d) Sobrecargar el método agregarJugadores() donde en el primero se agregue 
solo 1 jugador y en otro se ingrese una cantidad de jugadores a aumentar.  '''
class Videojuego:
    def __init__(self, nombre, plataforma, cantidadJugadores=1):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidadJugadores = cantidadJugadores

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Plataforma: {self.plataforma}, Jugadores: {self.cantidadJugadores}")

    def agregarJugadores(self, cantidad=1):
        self.cantidadJugadores += cantidad

class UnJugador(Videojuego):
    def agregarJugadores(self, cantidad=1):
        print("Este juego no admite más jugadores")

class Multijugador(Videojuego):
    def agregarJugadores(self, cantidad=1):
        self.cantidadJugadores += cantidad

zelda = UnJugador("The Legend of Zelda", "Nintendo Switch")
fifa = Multijugador("FIFA 23", "PlayStation 5")

zelda.agregarJugadores(2)
zelda.mostrar()
fifa.agregarJugadores(2)
fifa.mostrar()