# MINI SISTEMA DE LOGIN
# Programa que permite registrar e iniciar sesión de usuarios en un sistema simple.




# Definición de la clase Usuario
class Usuario:


    # Método constructor que se ejecuta al crear un nuevo objeto de tipo Usuario
    def __init__(self, nombre, correo, contrasena):


        # self hace referencia al propio objeto que se está creando
        # Es obligatorio en todos los métodos de instancia de una clase
        self.nombre = nombre


        # Se almacena el correo del usuario recibido por parámetro
        self.correo = correo


        # Se almacena la contraseña del usuario recibido por parámetro
        self.contrasena = contrasena


        # Se inicializa el atributo sesion_iniciada como False
        # Esto indica que el usuario aún no ha iniciado sesión
        self.sesion_iniciada = False




    # Método para iniciar sesión comparando datos ingresados con los del usuario guardado
    def iniciar_sesion(self, correo, contrasena):


        # Se verifica si el correo y la contraseña ingresados coinciden con los del usuario
        if self.correo == correo and self.contrasena == contrasena:


            # Si coinciden, se cambia el valor del atributo sesion_iniciada a True
            self.sesion_iniciada = True


            # Se muestra un mensaje de éxito con el nombre del usuario
            print("Inicio de sesión exitoso. Bienvenido,", self.nombre)


        # Si los datos no coinciden, se muestra un mensaje de error
        else:
            print("Correo o contraseña incorrectos.")




# Definición de la clase SistemaLogin
class SistemaLogin:


    # Método constructor que crea una lista vacía para guardar los usuarios registrados
    def __init__(self):


        # Se crea una lista llamada usuarios donde se almacenarán todos los objetos de tipo Usuario
        self.usuarios = []




    # Método que permite registrar un nuevo usuario en el sistema
    def registrar_usuario(self, nombre, correo, contrasena):


        # Se crea un nuevo objeto de tipo Usuario con los datos recibidos
        nuevo_usuario = Usuario(nombre, correo, contrasena)


        # Se agrega ese nuevo objeto (usuario) a la lista de usuarios del sistema
        self.usuarios.append(nuevo_usuario)


        # Se muestra un mensaje para confirmar que el registro fue exitoso
        print("Usuario registrado correctamente.")




    # Método que busca un usuario por su correo electrónico dentro de la lista de usuarios
    def buscar_usuario(self, correo):


        # Se recorre la lista de usuarios registrados en el sistema
        for usuario in self.usuarios:


            # Si el correo del usuario coincide con el que se busca, se devuelve ese objeto
            if usuario.correo == correo:
                return usuario


        # Si no se encuentra ningún usuario con ese correo, se devuelve None (ninguno)
        return None




    # Método que permite iniciar sesión a un usuario registrado
    def iniciar_sesion(self, correo, contrasena):


        # Se busca el usuario llamando al método buscar_usuario y se guarda en la variable usuario
        usuario = self.buscar_usuario(correo)


        # Si se encontró un usuario con ese correo, se verifica su contraseña
        if usuario:


            # Se llama al método iniciar_sesion del objeto encontrado para validar la contraseña
            usuario.iniciar_sesion(correo, contrasena)


        # Si no existe el usuario, se muestra un mensaje informando que no está registrado
        else:
            print("El usuario no está registrado.")




# Definición de la función principal que contiene el menú del sistema
def menu():


    # Se crea un objeto del tipo SistemaLogin para administrar los usuarios
    sistema = SistemaLogin()


    # Ciclo infinito para mostrar el menú de opciones mientras el usuario no decida salir
    while True:


        # Se muestra el menú con las opciones disponibles
        print("\n--- MENÚ DEL SISTEMA DE LOGIN ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")


        # Se pide al usuario que elija una de las opciones
        opcion = input("Elige una opción: ")




        # Si la opción es 1, se ejecuta el registro de un nuevo usuario
        if opcion == "1":


            # Se solicitan los datos al usuario
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")


            # Se llama al método registrar_usuario para guardar el nuevo usuario
            sistema.registrar_usuario(nombre, correo, contrasena)




        # Si la opción es 2, se ejecuta el proceso de inicio de sesión
        elif opcion == "2":


            # Se piden los datos de acceso
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")


            # Se llama al método iniciar_sesion del sistema para validar los datos
            sistema.iniciar_sesion(correo, contrasena)




        # Si la opción es 3, el sistema termina
        elif opcion == "3":


            # Se muestra un mensaje de salida
            print("Saliendo del sistema...")


            # Se rompe el ciclo para finalizar el programa
            break




        # Si se ingresa una opción diferente a las válidas, se muestra un mensaje de error
        else:
            print("Opción no válida. Intenta nuevamente.")




# Llamado final a la función menu() para que el programa comience a ejecutarse
menu()



