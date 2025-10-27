// MINI SISTEMA DE LOGIN
// Programa que permite registrar e iniciar sesión de usuarios en un sistema simple.
// Utiliza clases para representar al usuario y al sistema que administra el registro e inicio de sesión.




// Importamos la clase Scanner para poder leer datos desde el teclado
import java.util.Scanner;




// Definición de la clase Usuario
class Usuario {


    // Atributos que guardan la información básica del usuario
    String nombre;
    String correo;
    String contrasena;
    boolean sesionIniciada;




    // Constructor de la clase Usuario
    // Se ejecuta automáticamente cuando se crea un nuevo objeto Usuario
    public Usuario(String nombre, String correo, String contrasena) {


        // La palabra "this" se usa para referirse a los atributos del objeto actual
        this.nombre = nombre;


        this.correo = correo;


        this.contrasena = contrasena;


        // Al crear un nuevo usuario, su sesión comienza como no iniciada
        this.sesionIniciada = false;
    }




    // Método para iniciar sesión verificando los datos ingresados
    public void iniciarSesion(String correo, String contrasena) {


        // Se compara el correo y la contraseña ingresados con los guardados
        if (this.correo.equals(correo) && this.contrasena.equals(contrasena)) {


            // Si coinciden, se cambia el valor de la variable sesionIniciada a true
            this.sesionIniciada = true;


            // Se muestra un mensaje de bienvenida
            System.out.println("Inicio de sesión exitoso. Bienvenido, " + this.nombre);
        }


        // Si los datos no coinciden, se muestra un mensaje de error
        else {
            System.out.println("Correo o contraseña incorrectos.");
        }
    }
}




// Definición de la clase SistemaLogin
class SistemaLogin {


    // Lista de usuarios registrada en el sistema (usamos un arreglo simple)
    Usuario[] usuarios;


    // Contador de usuarios registrados para controlar la cantidad en el arreglo
    int cantidad;




    // Constructor que inicializa el sistema
    public SistemaLogin() {


        // Creamos un arreglo de tamaño 100 para guardar los usuarios
        this.usuarios = new Usuario[100];


        // Inicializamos el contador de usuarios en cero
        this.cantidad = 0;
    }




    // Método para registrar un nuevo usuario en el sistema
    public void registrarUsuario(String nombre, String correo, String contrasena) {


        // Creamos un nuevo objeto Usuario con los datos ingresados
        Usuario nuevoUsuario = new Usuario(nombre, correo, contrasena);


        // Guardamos el nuevo usuario en la lista de usuarios usando el contador como índice
        this.usuarios[this.cantidad] = nuevoUsuario;


        // Aumentamos el contador en 1
        this.cantidad++;


        // Mostramos un mensaje de confirmación
        System.out.println("Usuario registrado correctamente.");
    }




    // Método para buscar un usuario por su correo
    public Usuario buscarUsuario(String correo) {


        // Recorremos el arreglo de usuarios registrados
        for (int i = 0; i < this.cantidad; i++) {


            // Si el correo del usuario coincide con el buscado, devolvemos ese objeto
            if (this.usuarios[i].correo.equals(correo)) {
                return this.usuarios[i];
            }
        }


        // Si no se encuentra, se devuelve null (ningún usuario encontrado)
        return null;
    }




    // Método que permite iniciar sesión con un correo y contraseña
    public void iniciarSesion(String correo, String contrasena) {


        // Buscamos el usuario usando el método buscarUsuario
        Usuario usuario = buscarUsuario(correo);


        // Si el usuario existe, se llama al método iniciarSesion para validar la contraseña
        if (usuario != null) {
            usuario.iniciarSesion(correo, contrasena);
        }


        // Si no se encuentra el usuario, mostramos un mensaje
        else {
            System.out.println("El usuario no está registrado.");
        }
    }
}




// Clase principal que contiene el método main (punto de inicio del programa)
public class Main {


    public static void main(String[] args) {


        // Creamos un objeto de la clase Scanner para leer datos desde teclado
        Scanner entrada = new Scanner(System.in);


        // Creamos una instancia del sistema de login
        SistemaLogin sistema = new SistemaLogin();


        // Bucle infinito que mostrará el menú hasta que el usuario decida salir
        while (true) {


            // Se muestra el menú de opciones
            System.out.println("\n--- MENÚ DEL SISTEMA DE LOGIN ---");
            System.out.println("1. Registrar usuario");
            System.out.println("2. Iniciar sesión");
            System.out.println("3. Salir");


            // Se solicita al usuario que elija una opción
            System.out.print("Elige una opción: ");
            String opcion = entrada.nextLine();




            // Si el usuario elige registrar un nuevo usuario
            if (opcion.equals("1")) {


                // Se solicitan los datos necesarios
                System.out.print("Nombre: ");
                String nombre = entrada.nextLine();


                System.out.print("Correo: ");
                String correo = entrada.nextLine();


                System.out.print("Contraseña: ");
                String contrasena = entrada.nextLine();


                // Se llama al método registrarUsuario del sistema
                sistema.registrarUsuario(nombre, correo, contrasena);
            }




            // Si el usuario elige iniciar sesión
            else if (opcion.equals("2")) {


                // Se piden los datos de acceso
                System.out.print("Correo: ");
                String correo = entrada.nextLine();


                System.out.print("Contraseña: ");
                String contrasena = entrada.nextLine();


                // Se llama al método iniciarSesion para validar las credenciales
                sistema.iniciarSesion(correo, contrasena);
            }




            // Si el usuario elige salir del sistema
            else if (opcion.equals("3")) {


                // Se muestra un mensaje y se rompe el ciclo while
                System.out.println("Saliendo del sistema...");
                break;
            }




            // Si el usuario escribe una opción no válida
            else {
                System.out.println("Opción no válida. Intenta nuevamente.");
            }
        }


        // Se cierra el objeto Scanner para liberar recursos
        entrada.close();
    }
}
