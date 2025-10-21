#Para estos ejercicios obviamente no los saque yo si no que me ayude con la IA de OpenAI, ChatGPT y un poco de motivacion para hacerlos jaja 

#Bueno un ejemplo que da la IA es el siguiente con estructura que cualquier codigo de POO debe tener 

class Perro: #Definicion de la clase Perro al que vamos a agregarle los metodos y atributos
    
    def __init__(self, nombre, edad): #Iniciamos la construccion de los atributos de la clase que son nombre y edad

        self.nombre = nombre #aqui le estamos diciendo que el atributo nombre de la clase Perro va a ser igual al parametro nombre que le pasemos al crear un objeto de la clase

        self.edad = edad #lo mismo para el atributo edad le decimos que va a ser igual al parametro edad que le pasemos al crear un objeto de la clase

    def ladrar(self): #Aqui definimos el metodo ladrar que no recibe ningun parametro adicional aparte de self

        print(f"{self.nombre} el perro esta ladrando.")#Aqui usamos el atributo nombre del objeto para imprimir un mensaje indicando que el perro esta ladrando llamando su nombre 

    def cumplir_años(self): #Aqui definimos el metodo cumplir_años que no recibe ningun parametro adicional aparte de self 

        self.edad += 1 #Aqui incrementamos en 1 el atributo edad del objeto 

        print(f"{self.nombre} en 1 año tendra {self.edad} años.") #Aqui imprimimos un mensaje indicando la nueva edad del perro usando sus atributos nombre y edad

nombre = input("Ingresa el nombre del perro: ") #Aqui le pedimos al usuario que ingrese el nombre del perro

edad = int(input("Ingresa la edad del perro: ")) #Aqui le pedimos al usuario que ingrese la edad del perro

mi_perro = Perro(nombre, edad) #Aqui los datos nombre y edad que el usuario que coloco el usuario se pasan alos atributos osea python automaticamente hace que los datos sean atributos del objeto mi_perro osea aqui creamos el objeto mi_perro de la clase Perro 

while True: #Aqui iniciamos un bucle infinito para que el usuario pueda elegir que accion realizar con su perro

    print("\n ¿Qué te gustaría hacer con tu perro?") #Aqui le preguntamos al usuario que le gustaria hacer con su perro
    
    print("1. Hacer que el perro ladre") #Aqui le damos la opcion 1 al usuario

    
    print("2. Hacer que el perro cumpla años") #Aqui le damos la opcion 2 al usuario
    

    opcion = input("Ingresa el número de la opción (o 'salir' para terminar): ") #Aqui le pedimos al usuario que ingrese el numero de la opcion que desea realizar o que escriba salir para terminar el programa

    if opcion == "1": #Si la opcion del usuario es 1

        mi_perro.ladrar() #Aqui llamamos al metodo ladrar del objeto mi_perro

    elif opcion == "2": #Si la opcion del usuario es 2

        mi_perro.cumplir_años() #Aqui llamamos al metodo cumplir_años del objeto mi_perro

    elif opcion.lower() == 'salir': #Si la opcion del usuario es salir

        print("¡Hasta luego!") #Aqui imprimimos un mensaje de despedida

        break #Aqui salimos del bucle infinito
    
    else: #Si la opcion del usuario no es ninguna de las anteriores

        print("Opción no válida. Por favor, intenta de nuevo.") #Aqui le decimos al usuario que la opcion no es valida y que intente de nuevo    



mi_perro.ladrar() #Aqui llamamos al metodo ladrar del objeto mi_perro
mi_perro.cumplir_años() #Aqui llamamos al metodo cumplir_años del objeto mi_perro


#QUE HACE EL CODIGO? EL CODIGO LO QUE HACE ES CREAR UNA CLASE PERRO CON ATRIBUTOS NOMBRE Y EDAD Y METODOS PARA HACERLO LADRAR Y CUMPLIR AÑOS, LUEGO PIDE AL USUARIO QUE INGRESE EL NOMBRE Y LA EDAD DEL PERRO Y CREA UN OBJETO DE LA CLASE PERRO CON ESOS DATOS, LUEGO LE DA OPCIONES AL USUARIO PARA HACER QUE EL PERRO LADRE O CUMPLA AÑOS HASTA QUE EL USUARIO DECIDA SALIR DEL PROGRAMA. 



#EJERCICIO TERMINADO CON LA IA ME AYUDO BASTANTE A ENTENDER LA POO Y A HACERLO PERO IGUAL ME QUEDARON DUDAS ASI QUE SEGUIRE PRACTICANDO Y MEJORANDO TRABAJO EN CASA HECHO DIA 20/10/2025












