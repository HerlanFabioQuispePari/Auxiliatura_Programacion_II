'''Crea una clase Celular con espacio para 20 aplicaciones o 1024Mb de Espacio 
a) Crea un método para instalar una nueva aplicación 
b) Crea un método para utilizar una aplicación (las aplicaciones que pesan más 
de 100Mb utilizan un 2% de batería por cada 10 minutos uso, las que pesan 
más de 250Mb utilizan 5% por cada 10 minutos de uso, en otros casos utiliza 
un 1% cada 10 minutos de uso) 
c) Muestra el porcentaje de batería restante 
d) Cuando la batería se acabe al tratar de utilizar el celular este debe mostrar el 
mensaje de celular apagado '''
class Celular:
    def __init__(self):
        self.espacio = 1024
        self.max = 20
        self.aplicaciones = []
        self.bateria = 100

    def instalarApp(self, nombre, peso):
        if len(self.aplicaciones) < self.max:
            if peso <= self.espacio:
                self.espacio -= peso
                app = [nombre, peso]
                self.aplicaciones.append(app)
                print(f'Se Instalo {nombre}')
            else:
                print('Memoria llena.')
        else:
            print('Máximo de aplicaciones alcanzado.')

    def utlizarApp(self, nombre, minutos):
        if self.bateria <= 0:
            print('Celular apagado')
            return

        app = next((a for a in self.aplicaciones if a[0] == nombre), False)
        if not app:
            print('Aplicación no encontrada.')
            return

        peso = app[1]
        if peso > 250:
            consumo = 5
        elif peso > 100:
            consumo = 2
        else:
            consumo = 1

        min10 = minutos // 10
        total = consumo * min10

        if self.bateria - total <= 0:
            self.bateria = 0
            print('Celular apagado')
        else:
            self.bateria -= total
            print(f'Usando "{nombre}" por {minutos} minutos.')

    def mostrarBateria(self):
        print(f'Batería restante: {self.bateria}%')


cel = Celular()
cel.instalarApp("Facebook", 150)
cel.instalarApp("Candy Crush", 300)
cel.instalarApp("Notas", 50)
cel.instalarApp("Maps", 120)
print()
cel.utlizarApp("Notas", 20)
cel.mostrarBateria()
cel.utlizarApp("Facebook", 30)
cel.mostrarBateria()
cel.utlizarApp("Candy Crush", 40)
cel.mostrarBateria()
cel.utlizarApp("Maps", 600)
cel.mostrarBateria()
cel.utlizarApp("Notas", 10)