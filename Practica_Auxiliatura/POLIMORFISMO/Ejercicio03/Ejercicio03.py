'''Un restaurante organiza a su personal mediante las siguientes clases: 
a) Instanciar 1 Cocinero, 2 objetos Mesero y 2 objetos Administrativo. 
b) Sobrecargar el método SueldoTotal para mostrar el sueldo total, 
sumándole las horas extra, considerando el sueldo por hora y la propina 
en caso de los meseros.  
c) Sobrecargar el método para mostrar a aquellos Empleados que tengan 
SueldoMes igual a X.'''
class Empleado:
    def __init__(self, nombre, sueldoMes):
        self.nombre = nombre
        self.sueldoMes = sueldoMes

    def sueldoTotal(self):
        pass

class Cocinero(Empleado):
    def __init__(self, nombre, sueldoMes, horasExtra, sueldoHora):
        super().__init__(nombre, sueldoMes)
        self.horasExtra = horasExtra
        self.sueldoHora = sueldoHora

    def sueldoTotal(self):
        return self.sueldoMes + (self.horasExtra * self.sueldoHora)

class Mesero(Empleado):
    def __init__(self, nombre, sueldoMes, horasExtra, sueldoHora, propina):
        super().__init__(nombre, sueldoMes)
        self.horasExtra = horasExtra
        self.sueldoHora = sueldoHora
        self.propina = propina

    def sueldoTotal(self):
        return self.sueldoMes + (self.horasExtra * self.sueldoHora) + self.propina

cocinero = Cocinero("Juan", 2000, 5, 10)
print(f"Sueldo total de Juan: ${cocinero.sueldoTotal()}")
mesero1 = Mesero("Ana", 1500, 3, 8, 200)
print(f"Sueldo total de Ana: ${mesero1.sueldoTotal()}")
mesero2 = Mesero("Luis", 1600, 2, 8, 150)
print(f"Sueldo total de Luis: ${mesero2.sueldoTotal()}")