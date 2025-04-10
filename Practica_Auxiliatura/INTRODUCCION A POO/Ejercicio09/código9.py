'''Realiza la abstracción de una Computadora  
a) Muestra los componentes principales de la computadora 
b) Muestra el estado de la computadora (encendido o apagado) 
c) Crea una instancia y simula encender y apagar la computadora.'''
class Computadora:
    def __init__(self, procesador, ram, almacenamiento):
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.estado = 'apagada'

    def componentes(self):
        print(f'Componentes: \nProcesador: {self.procesador} \nRam: {self.ram}GB \nAlamacenamiento: {self.almacenamiento}GB')
        
    def estadoComputadora(self):
        print(f'Estado de la computadora: {self.estado}')

    def encender(self):
        self.estado = 'encendida'
        print('La computadora esta encendida')

    def apagar(self):
        self.estado = 'apagada'
        print('La computadora es apagada')

c1 = Computadora('Intel Core i5', 8, 250)
c1.componentes()
print()
c1.estadoComputadora()
c1.encender()
c1.estadoComputadora()
c1.apagar()
c1.estadoComputadora()