from flask import Flask, request, jsonify, render_template
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

DB_CONFIG = {
    'host': 'localhost',
    'database': 'empresa_pgadmin',
    'user': 'postgres',
    'password': '123456',
    'port': 5432
}

def conectar_bd():
    try:
        return psycopg2.connect(**DB_CONFIG)
    except Exception as e:
        print("Error de conexión:", e)
        return None


# creamos tablas con sus atributos y tipo de datos 
def crear_tablas():
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(120) UNIQUE NOT NULL,
            edad INTEGER,
            salario NUMERIC(10,2),
            activo BOOLEAN DEFAULT TRUE,
            fecha_contratacion DATE,
            creado TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS departamentos (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            descripcion TEXT,
            creado TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS asignaciones (
            id SERIAL PRIMARY KEY,
            empleado_id INTEGER REFERENCES empleados(id),
            departamento_id INTEGER REFERENCES departamentos(id),
            fecha DATE NOT NULL,
            notas TEXT,
            creado TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
        );
        """)

        conexion.commit()
        cursor.close()
        conexion.close()


# Esta es la ruta principal 
@app.route('/')
def home():
    return render_template("index.html")


#Hacemos las interacciones o operaciones basicas para los datos de empleados

@app.route('/empleados', methods=['POST'])
def crear_empleado():
    datos = request.get_json()
    
    nombre = datos.get('nombre')
    email = datos.get('email')
    edad = datos.get('edad')
    salario = datos.get('salario')
    fecha_contratacion = datos.get('fecha_contratacion')

    if not nombre or not email:
        return jsonify({'error': 'Nombre y email obligatorios'}), 400

    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO empleados (nombre, email, edad, salario, fecha_contratacion)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id;
    """, (nombre, email, edad, salario, fecha_contratacion))

    nuevo_id = cursor.fetchone()[0]
    conexion.commit()
    cursor.close()
    conexion.close()

    return jsonify({'mensaje': 'Empleado creado', 'id': nuevo_id}), 201


@app.route('/empleados', methods=['GET'])
def obtener_empleados():
    conexion = conectar_bd()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM empleados ORDER BY creado DESC;")
    empleados = cursor.fetchall()

    cursor.close()
    conexion.close()
    return jsonify(empleados), 200


# hacemos las operaciones basicas para los datos de departamentos 
@app.route('/departamentos', methods=['POST'])
def crear_departamento():
    datos = request.get_json()
    nombre = datos.get('nombre')
    descripcion = datos.get('descripcion')

    if not nombre:
        return jsonify({'error': 'El nombre es obligatorio'}), 400

    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO departamentos (nombre, descripcion)
        VALUES (%s, %s)
        RETURNING id;
    """, (nombre, descripcion))

    new_id = cursor.fetchone()[0]
    conexion.commit()
    cursor.close()
    conexion.close()

    return jsonify({'mensaje': 'Departamento creado', 'id': new_id}), 201


@app.route('/departamentos', methods=['GET'])
def obtener_departamentos():
    conexion = conectar_bd()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM departamentos ORDER BY creado DESC;")
    departamentos = cursor.fetchall()

    cursor.close()
    conexion.close()
    return jsonify(departamentos), 200


# hacemos las operaciones basicas para asignaciones

@app.route('/asignaciones', methods=['POST'])
def crear_asignacion():
    datos = request.get_json()
    empleado_id = datos.get('empleado_id')
    departamento_id = datos.get('departamento_id')
    fecha = datos.get('fecha')
    notas = datos.get('notas')

    if not empleado_id or not departamento_id or not fecha:
        return jsonify({'error': 'empleado_id, departamento_id y fecha son obligatorios'}), 400

    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO asignaciones (empleado_id, departamento_id, fecha, notas)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
    """, (empleado_id, departamento_id, fecha, notas))

    asign_id = cursor.fetchone()[0]
    conexion.commit()
    cursor.close()
    conexion.close()

    return jsonify({'mensaje': 'Asignación creada', 'id': asign_id}), 201


@app.route('/asignaciones', methods=['GET'])
def obtener_asignaciones():
    conexion = conectar_bd()
    cursor = conexion.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM asignaciones ORDER BY creado DESC;")
    asignaciones = cursor.fetchall()

    cursor.close()
    conexion.close()
    return jsonify(asignaciones), 200


#-Inicio del servidor flask 

if __name__ == '__main__':
    print("Iniciando servidor empresa_pgadmin...")
    crear_tablas()
    app.run(debug=True, host='0.0.0.0', port=5000)
