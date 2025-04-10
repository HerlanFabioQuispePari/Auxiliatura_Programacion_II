public class Coche {
    private String marca;
    private int modelo;
    private int velocidad;

    public Coche(String marca, int modelo, int velocidad) {
        this.marca = marca;
        this.modelo = modelo;
        this.velocidad = velocidad;
    }

    public int acelerar() {
        velocidad += 10;
        return velocidad;
    }

    public int frenar() {
        velocidad -= 5;
        return velocidad;
    }

    public static void main(String[] args) {
        Coche c1 = new Coche("Toyota", 1999, 100);
        System.out.println("El coche esta acelerando: " + c1.acelerar() + " km");
        System.out.println("El coche esta frenando: " + c1.frenar() + " km");
        System.out.println();

        Coche c2 = new Coche("Honda", 2020, 130);
        System.out.println("El coche esta acelerando: " + c2.acelerar() + " km");
        System.out.println("El coche esta frenando: " + c2.frenar() + " km");
    }
}