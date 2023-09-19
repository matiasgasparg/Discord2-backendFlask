from ..models.user_model import User

from flask import Flask, jsonify, request,send_from_directory,current_app
from flask_cors import CORS

from decimal import Decimal
from ..models.exceptions import userNotFound,CustomException,InvalidDataError,duplicateError
from werkzeug.utils import secure_filename
import os
# app = Flask(__name__)

# CORS(app)  # Agregamos CORS a la aplicación
# app.config['UPLOAD_FOLDER'] = 'uploads'  # Carpeta donde se guardarán las imágenes

# users = []

class userController:
# Función para obtener un usuario por su ID de la base de datos
    @classmethod
    def get(cls, id_usuario):
            user = User.get(id_usuario)  # Aquí se espera un ID de usuario, no un objeto User
            if user is not None:
                return user.serialize(), 200
            else:
                # Si no se encuentra el user, lanza la excepción userNotFound
                raise userNotFound(id_usuario)
    @classmethod
    def get_all(cls):
        """Get all users"""
        user_objects = User.get_all()
        users = []
        for user in user_objects:
            users.append(user.serialize())
        return users, 200

    @classmethod
    def create(cls):
        """Create a new User"""
        data = request.json
        username = data['username']
        email = data['email']
        print(email)
        cls.validate_input_data(data)
        
        if User.duplicate(username,email):
            raise duplicateError()
            
        new_user = User(**data)

        User.create(new_user)

        return jsonify ({'message': 'Usuario creado satisfactoriamente'}),200
    @classmethod
    def update(cls, id_usuario):
        """Update a User"""
        data = request.json
        field_to_update = data.get('field')  # Campo que se desea actualizar
        value = data.get('value')  # Nuevo valor para el campo
        valid_fields = ['username', 'email', 'name', 'password']  # Lista de campos válidos

        if field_to_update in valid_fields:
            if User.update(id_usuario, field_to_update, value):
                return jsonify({'message': f'{field_to_update.capitalize()} actualizado exitosamente'}), 200
            else:
                raise userNotFound(id_usuario)
        else:
            return jsonify({'message': 'Campo no válido para actualización'}), 400
    
    @classmethod
    def login(cls):
        data = request.get_json()
        email = data.get('email', '')
        password = data.get('password', '')
        username = data.get('username', '')
        user = next((user for user in User.get_all() if user.email == email or user.username == username and user.password == password), None)

        if user:
            response_data = {
                'message': 'Login successful',
                'id_usuario': user.id_usuario,  # Corregido: Usar notación de punto en lugar de corchetes
                'img_perfil': user.img_perfil,  # Corregido: Usar notación de punto en lugar de corchetes
                'username': user.username  # Corregido: Usar notación de punto en lugar de corchetes
            }
            return jsonify(response_data), 200
        else:
            return jsonify({'message': 'Datos invalidos'}), 401
    @classmethod
    def delete(cls,id_usuario):
        """Delete a User"""
        if not User.exists(id_usuario):
            raise userNotFound(id_usuario)

        User.delete(id_usuario)
        return {'message': 'User deleted successfully'}, 204
    @staticmethod
    def validate_input_data(data):
        """Validate input data"""
        if len(data.get('name', '')) < 3:
            raise InvalidDataError("El Nombre debe tener al menos 3 caracteres")
    
        if len(data.get('password', '')) < 6:
            raise InvalidDataError("La password debe tener al menos 6 digitos")
    @classmethod
    def upload_file(cls,user_id):
        if 'photo' not in request.files:
            return jsonify({'message': 'No se proporcionó ninguna imagen'}), 400

        photo = request.files['photo']
        if photo.filename == '':
            return jsonify({'message': 'Nombre de archivo vacío'}), 400

        filename = f'{user_id}_{secure_filename(photo.filename)}'  # Genera un nombre único usando el ID del usuario
        photo.save(os.path.join('uploads', filename))  # Guarda la imagen en la carpeta uploads

        # Actualiza el campo image_url en la base de datos con el enlace de la imagen
        img_perfil = f'http://127.0.0.1:5000/users/get_image/{filename}' 
        User.update(user_id, 'img_perfil', img_perfil)

        return jsonify({'message': 'Imagen subida correctamente'}), 200
    @classmethod
    def get_image(cls,image_name):
        image_path = os.path.join('../uploads', image_name)
        return send_from_directory('../uploads', image_name)
    
    
