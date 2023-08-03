from flask import Flask, jsonify, request
from classes import User
from flask_cors import CORS
import datos 
app = Flask(__name__)
CORS(app)  # Agregamos CORS a la aplicación

users = []

@app.route('/users', methods=['GET'])
def obtener_todos_los_usuarios():
    usuarios = datos.obtener_usuarios()
    return jsonify(usuarios), 200

@app.route('/users', methods=['POST'])
def crear_nuevo_usuario():
    data = request.get_json()
    name = data.get('name')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    datebirth=data.get('datebirth')
    if datos.crear_usuario(name,username,email,password,datebirth):
        return jsonify({'message': 'Usuario creado exitosamente'}), 201
    else:
        return jsonify({'message': 'Error al crear usuario'}), 500

@app.route('/users/<int:id_usuario>', methods=['GET'])
def obtener_usuario_por_su_id(id_usuario):
    usuario = datos.obtener_usuario_por_id(id_usuario)
    if usuario:
        return jsonify(usuario), 200
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 404

@app.route('/users/<int:id_usuario>', methods=['PUT'])
def actualizar_usuario_por_su_id(id_usuario):
    data = request.get_json()
    name = data.get('name')
    username=data.get('username')
    email = data.get('email')
    password = data.get('password')
    datebirth=data.get('datebirth')

    if datos.actualizar_usuario(id_usuario, name, username, email,password,datebirth):
        return jsonify({'message': 'Usuario actualizado exitosamente'}), 200
    else:
        return jsonify({'message': 'Error al actualizar usuario'}), 500

@app.route('/users/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario_por_su_id(id_usuario):
    if datos.eliminar_usuario(id_usuario):
        return jsonify({'message': 'Usuario eliminado exitosamente'}), 200
    else:
        return jsonify({'message': 'Error al eliminar usuario'}), 500

@app.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email', '')
    password = data.get('password', '')
    user = next((user for user in datos.obtener_usuarios() if user['email'] == email and user['password'] == password), None)

    if user:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid email or password'}), 401
#Llamadas servidor
@app.route('/users/servers/<int:id_usuario>', methods=['GET'])
def obtener_user_servidor(id_usuario):
    servidores = datos.obtener_servidor(id_usuario)
    if servidores:
        return jsonify(servidores), 200
    else:
        return jsonify({'message': 'No se encontraron servidores'}), 404
#Agrega un servidor 
@app.route('/users/<int:id_usuario>/servers', methods=['POST'])
def agregar_servidor(id_usuario):
    data = request.get_json()
    nombre=data.get('nombre', '')
    if datos.agregar_servidor(id_usuario, nombre):
        return jsonify({'message': f'Servidor "{nombre}" agregado al usuario con ID {id_usuario}'}), 201
    else:
        return jsonify({'message': 'Error al agregar el servidor'}), 500
#Busqueda servidor por nombre 
@app.route('/servidores/<nombre_servidor>', methods=['GET'])
def buscar_servidor(nombre_servidor):
    servidor = datos.obtener_servidor_por_nombre(nombre_servidor)
    if servidor:
        return jsonify(servidor), 200
    else:
        return jsonify({'message': 'No se encuentra el servidor'}), 404


    
#Funcion que agrega canales a un servidor
@app.route('/users/<int:id_usuario>/servidores/<int:id_servidor>/canales', methods=['POST'])
def agregar_canal(id_usuario, id_servidor):
    data = request.get_json()
    nombre = data.get('nombre', '')

    if not nombre:
        return jsonify({'message': 'El nombre del canal es requerido'}), 400

    if datos.agregar_canales(nombre, id_servidor):
        return jsonify({'message': f'Canal "{nombre}" agregado correctamente al servidor con ID {id_servidor} para el usuario con ID {id_usuario+1}'}), 201
    else:
        return jsonify({'message': 'Error al agregar el canal'}), 500

# Obtener todos los canales de un servidor que corresponden a un usuario
@app.route('/users/servers/<int:id_usuario>/<int:id_servidor>', methods=['GET'])
def obtener_canales_usuario_servidor(id_usuario, id_servidor):
    canales = datos.obtener_canales_usuario_servidor(id_usuario, id_servidor)
    if canales:
        return jsonify(canales), 200
    else:
        return jsonify({'message': 'No se encontraron canales para el usuario y servidor especificados'}), 404

@app.route('/canal/<int:id_canal>', methods=['GET'])
def obtener_chats_usuarios_canal(id_canal):
    chats_usuarios_canal = datos.obtener_chats_usuarios_canal(id_canal)
    if chats_usuarios_canal:
        return jsonify(chats_usuarios_canal), 200
    else:
        return jsonify({'message': 'No se encontraron chats y usuarios para el canal'}), 404

if __name__ == '__main__':
    app.run(debug=True)
