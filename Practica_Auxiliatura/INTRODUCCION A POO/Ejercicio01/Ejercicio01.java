public class Persona {
    private String nombre;
    private int edad;
    private String ciudad;

    public Persona(String nombre, int edad, String ciudad) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
    }

    public void saludo() {
        System.out.println("Hola, soy " + nombre + " de " + ciudad);
    }

    public void verificarEdad() {
        if (edad >= 18) {
            System.out.println(nombre + " es mayor de edad");
        } else {
            System.out.println(nombre + " es menor de edad");
        }
    }

    public static void main(String[] args) {
        Persona p1 = new Persona("Marcos", 21, "La Paz");
        p1.saludo();
        p1.verificarEdad();
        System.out.println();

        Persona p2 = new Persona("Maria", 15, "Oruro");
        p2.saludo();
        p2.verificarEdad();
        System.out.println();

        Persona p3 = new Persona("Roberto", 19, "Pando");
        p3.saludo();
        p3.verificarEdad();
    }
}