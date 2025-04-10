public class Empleado {
    protected String nombre;
    protected double sueldoMes;

    public Empleado(String nombre, double sueldoMes) {
        this.nombre = nombre;
        this.sueldoMes = sueldoMes;
    }

    public double sueldoTotal() {
        return sueldoMes;
    }

    public static void mostrarPorSueldo(Empleado[] empleados, double x) {
        for (Empleado emp : empleados) {
            if (emp.sueldoMes == x) {
                System.out.println(emp.nombre + " tiene sueldo igual a " + x);
            }
        }
    }
}

public class Cocinero extends Empleado {
    private int horasExtra;
    private double sueldoHora;

    public Cocinero(String nombre, double sueldoMes, int horasExtra, double sueldoHora) {
        super(nombre, sueldoMes);
        this.horasExtra = horasExtra;
        this.sueldoHora = sueldoHora;
    }

    @Override
    public double sueldoTotal() {
        return sueldoMes + (horasExtra * sueldoHora);
    }
}

public class Mesero extends Empleado {
    private int horasExtra;
    private double sueldoHora;
    private double propina;

    public Mesero(String nombre, double sueldoMes, int horasExtra, double sueldoHora, double propina) {
        super(nombre, sueldoMes);
        this.horasExtra = horasExtra;
        this.sueldoHora = sueldoHora;
        this.propina = propina;
    }

    @Override
    public double sueldoTotal() {
        return sueldoMes + (horasExtra * sueldoHora) + propina;
    }
}

public class Main {
    public static void main(String[] args) {
        Cocinero cocinero = new Cocinero("Juan", 2000, 5, 10);
        Mesero mesero1 = new Mesero("Ana", 1500, 3, 8, 200);
        Mesero mesero2 = new Mesero("Luis", 1600, 2, 8, 150);

        System.out.println("Sueldo total de Juan: $" + cocinero.sueldoTotal());
        System.out.println("Sueldo total de Ana: $" + mesero1.sueldoTotal());
        System.out.println("Sueldo total de Luis: $" + mesero2.sueldoTotal());

        Empleado[] empleados = {cocinero, mesero1, mesero2};
        Empleado.mostrarPorSueldo(empleados, 1500);
    }
}