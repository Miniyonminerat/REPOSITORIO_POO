#Formulario basico con Flask y Jinja2 con Nombre Apellido Ciudad y Telefono 

from flask import Flask, render_template, request #flask para crear la aplicacion web 

app = Flask(__name__) #crea la aplicacion web creamos el punto de inicio

@app.route('/') #ruta principal de la aplicacion

def index(): #Esto lo que hace es que se meta en la carpeta templates y buscar el archivo index.html y lo renderiza

    return render_template("index.html", titulo="Formulario Basico") 

if __name__ == '__main__': #si este archivo se ejecuta directamente flask iniciara un servidor que me creara una direccion local para colocar en el navegador
    
    app.run(debug=True)








