from flask import Flask, jsonify, request,send_from_directory
from classes import User
from flask_cors import CORS
import datos 
import mysql.connector
from mysql.connector import errors
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

CORS(app)  # Agregamos CORS a la aplicación
app.config['UPLOAD_FOLDER'] = 'uploads'  # Carpeta donde se guardarán las imágenes

users = []

@app.route('/users', methods=['GET'])
def obtener_todos_los_usuarios():
    usuarios = datos.obtener_usuarios()
    return jsonify(usuarios), 200

@app.route('/users/create', methods=['POST'])
def crear_usuario():
    try:
        data = request.json
        name = data['name']
        username = data['username']
        email = data['email']
        password = data['password']
        datebirth = data['datebirth']

        # Verificar si ya existe un usuario con el mismo username y/o email
        if datos.verificar_usuario_existente(username,email):
            return jsonify({'message': 'Ya existe un usuario con el mismo username y/o email'}), 400

        # Si no existe, crear el usuario
        if datos.crear_usuario(name, username, email, password, datebirth):
            return jsonify({'message': 'Usuario creado exitosamente'}), 201
        else:
            return jsonify({'message': 'Error al crear usuario'}), 500
    except Exception as e:
        return jsonify({'message': 'Error en la solicitud'}), 400

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
    field_to_update = data.get('field')  # Campo que se desea actualizar
    value = data.get('value')  # Nuevo valor para el campo

    valid_fields = ['username', 'email', 'name', 'password']  # Lista de campos válidos

    if field_to_update in valid_fields:
        if datos.actualizar_usuario_por_campo(id_usuario, field_to_update, value):
            return jsonify({'message': f'{field_to_update.capitalize()} actualizado exitosamente'}), 200
        else:
            return jsonify({'message': f'Error al actualizar {field_to_update}'}), 500
    else:
        return jsonify({'message': 'Campo no válido para actualización'}), 400


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
        # Agregar la imagen y el nombre del usuario al objeto JSON de respuesta
        response_data = {
            'message': 'Login successful',
            'id_usuario': user['id_usuario'],
            'img_perfil': user.get('img_perfil', ''),
            'username': user.get('username', '')
        }
        return jsonify(response_data), 200
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
    descripcion=data.get('descripcion','')
    if datos.agregar_servidor(id_usuario, nombre,descripcion):
        return jsonify({'message': f'Servidor "{nombre}" agregado al usuario con ID {id_usuario} y la descripcion {descripcion}'}), 201
    else:
        return jsonify({'message': 'Error al agregar el servidor'}), 500


    
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
    return jsonify(chats_usuarios_canal), 200

@app.route('/users/servers/<int:id_usuario>/<int:id_servidor>/canales/<int:id_canal>/messages', methods=['POST'])
def enviar_mensaje(id_usuario, id_servidor, id_canal):
    data = request.get_json()
    mensaje = data.get('mensaje', '')
    fecha_hora=data.get('fecha_Hora','')

    if not mensaje:
        return jsonify({'message': 'El mensaje no puede estar vacío'}), 400

    if datos.enviar_mensaje(id_usuario, id_servidor, id_canal, mensaje):
        return jsonify({'message': 'Mensaje enviado exitosamente'}), 201
    else:
        return jsonify({'message': 'Error al enviar el mensaje'}), 500
@app.route('/servidores/<nombre_servidor>', methods=['GET'])
def buscar_servidor(nombre_servidor):
    servidor = datos.obtener_servidor_por_nombre(nombre_servidor)
    if servidor:
        cantidad_usuarios = datos.obtener_cantidad_usuarios_servidor(servidor['idservidor'])
        servidor['cantidad_usuarios'] = cantidad_usuarios
        return jsonify(servidor), 200
    else:
        return jsonify({'message': 'No se encuentra el servidor'}), 404

@app.route('/servidores', methods=['GET'])
def obtener_todos_los_servidores():
    servidores = datos.obtener_todos_los_servidores()
    for servidor in servidores:
        cantidad_usuarios = datos.obtener_cantidad_usuarios_servidor(servidor['idservidor'])
        servidor['cantidad_usuarios'] = cantidad_usuarios
    
    return jsonify(servidores), 200
@app.route('/users/servidores/<int:id_usuario>/<int:id_servidor>', methods=['POST'])
def unirse_al_servidor(id_usuario, id_servidor):
    try:
        if datos.existe_relacion_usuario_servidor(id_usuario, id_servidor):
            return jsonify({'message': 'El usuario ya está unido a este servidor'}), 409

        if datos.unirse_a_servidor(id_usuario, id_servidor):
            return jsonify({'message': 'Usuario unido exitosamente al servidor'}), 200
        else:
            return jsonify({'message': 'Error al unirse al servidor'}), 500
    except Exception as e:
        return jsonify({'message': 'Error en el servidor'}), 500

@app.route('/users/servers/<int:id_usuario>/canales/<int:id_canal>/messages/<int:id_mensaje>', methods=['PUT'])
def editar_mensaje(id_usuario, id_canal, id_mensaje):
    try:
        data = request.get_json()
        nuevo_mensaje = data.get('nuevo_mensaje', '')

        if not nuevo_mensaje:
            return jsonify({'message': 'El nuevo mensaje no puede estar vacío'}), 400

        # Verificar si el mensaje pertenece al usuario y al canal especificados
        mensajes_usuario_canal = datos.obtener_chats_usuarios_canal(id_canal)
        mensaje_a_editar = next((mensaje for mensaje in mensajes_usuario_canal if mensaje['idchat'] == id_mensaje), None)

        if mensaje_a_editar and mensaje_a_editar['id_usuario'] == id_usuario:
            if datos.editar_mensaje(id_mensaje, nuevo_mensaje):
                return jsonify({'message': 'Mensaje editado exitosamente'}), 200
            else:
                return jsonify({'message': 'Error al editar el mensaje'}), 500
        else:
            return jsonify({'message': 'No se puede editar el mensaje. No se encontró el mensaje o no tienes permiso'}), 403
    except Exception as e:
        return jsonify({'message': 'Error en el servidor'}), 500

@app.route('/upload/<int:user_id>', methods=['POST'])
def upload_file(user_id):
    if 'photo' not in request.files:
        return jsonify({'message': 'No se proporcionó ninguna imagen'}), 400

    photo = request.files['photo']
    if photo.filename == '':
        return jsonify({'message': 'Nombre de archivo vacío'}), 400

    filename = f'{user_id}_{secure_filename(photo.filename)}'  # Genera un nombre único usando el ID del usuario
    photo.save(os.path.join('uploads', filename))  # Guarda la imagen en la carpeta uploads

    # Actualiza el campo image_url en la base de datos con el enlace de la imagen
    img_perfil = f'http://127.0.0.1:5000/get_image/{filename}' 
    datos.actualizar_usuario_por_campo(user_id, 'img_perfil', img_perfil)

    return jsonify({'message': 'Imagen subida correctamente'}), 200



@app.route('/get_image/<image_name>')
def get_image(image_name):
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
    return send_from_directory(app.config['UPLOAD_FOLDER'], image_name)
if __name__ == '__main__':
    app.run(debug=True)
