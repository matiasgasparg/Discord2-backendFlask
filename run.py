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
        
if __name__ == '__main__':
    app.run(debug=True)
