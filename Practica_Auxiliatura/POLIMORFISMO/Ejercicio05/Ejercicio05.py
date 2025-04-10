'''Se hace referencia a algunos de los diferentes ambientes de la Universidad 
mediante las siguientes clases: 
a) Instanciar 2 objetos Oficina, 2 Aulas y 1 Laboratorio 
b) Crear un método mostrar() para mostrar los datos de cada objeto 
c) Sobrecargar el método cantidadMuebles(), para conocer el número total de 
muebles dentro de cada ambiente'''
class Ambiente:
    def cantidadMuebles(self):
        pass

class Oficina(Ambiente):
    def __init__(self, sillas, escritorios, estanterias):
        self.sillas = sillas
        self.escritorios = escritorios
        self.estanterias = estanterias

    def cantidadMuebles(self):
        return self.sillas + self.escritorios + self.estanterias

class Aula(Ambiente):
    def __init__(self, sillas, pupitres):
        self.sillas = sillas
        self.pupitres = pupitres

    def cantidadMuebles(self):
        return self.sillas + self.pupitres

oficina1 = Oficina(5, 3, 2)
print(f"Muebles en Oficina1: {oficina1.cantidadMuebles()}")
oficina2 = Oficina(4, 2, 1)
print(f"Muebles en Oficina2: {oficina2.cantidadMuebles()}")
aula1 = Aula(30, 15)
print(f"Muebles en Aula1: {aula1.cantidadMuebles()}")
aula2 = Aula(25, 20)
print(f"Muebles en Aula2: {aula2.cantidadMuebles()}")