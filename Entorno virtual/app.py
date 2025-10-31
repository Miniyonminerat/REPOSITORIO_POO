from flask import Flask, render_template #flask para crear la aplicacion web render renderiza las plantillas html

app = Flask(__name__) #crea la aplicacion web creamos el punto de inicio 

@app.route('/') #ruta principal de la aplicacion 
def index():
    return render_template('index.html', titulo= "Pagina SENA") #renderiza la plantilla index.html cuando se accede a la ruta principal

if __name__ == '__main__': #si este archivo se ejecuta directamente flask iniciara un servidor que me creara una direccion local para colocar en el navegador
    app.run(debug=True) #debug true para que se reinicie automaticamente el servidor cada vez que se haga un cambio en el codigo



