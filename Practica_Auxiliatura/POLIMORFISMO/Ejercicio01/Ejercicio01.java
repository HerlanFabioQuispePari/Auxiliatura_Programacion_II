public class Videojuego {
    private String nombre;
    private String plataforma;
    private int cantidadJugadores;

    public Videojuego(String nombre, String plataforma) {
        this(nombre, plataforma, 1);
    }

    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }

    public void mostrar() {
        System.out.println("Nombre: " + nombre + ", Plataforma: " + plataforma + 
                         ", Jugadores: " + cantidadJugadores);
    }

    public void agregarJugadores() {
        cantidadJugadores += 1;
    }

    public void agregarJugadores(int cantidad) {
        cantidadJugadores += cantidad;
    }

    public static void main(String[] args) {
        Videojuego zelda = new Videojuego("The Legend of Zelda", "Nintendo Switch");
        Videojuego fifa = new Videojuego("FIFA 23", "PlayStation 5", 1);

        zelda.agregarJugadores();
        fifa.agregarJugadores(4);

        zelda.mostrar();
        fifa.mostrar();
    }
}