
from ..models.server_model import Server
from flask import request,jsonify
# from decimal import Decimal
from ..models.exceptions import userNotFound,CustomException,InvalidDataError,duplicateError

class serverController:
    @classmethod
    def get(cls, id_usuario):
        server_objects = Server.get(id_usuario)  # Aquí se obtiene una lista de instancias de la clase Server

        if server_objects:
            servers = [list(server.serialize().values()) for server in server_objects]
            return servers, 200
        else:
            return jsonify({'message': 'Servidores no encontrado para el usuario ingresado'}), 404

    @classmethod
    def get_all(cls):
        """Get all servers"""
        server_objects = Server.get_all()
        servers = []
        for server in server_objects:
            server_data = server.serialize()
            cant_user = Server.get_cant_user(server_data['idservidor'])
            server_data['cantidad_usuarios'] = cant_user
            servers.append(server_data)
        return jsonify(servers), 200
    @classmethod
    def create(cls,id_usuario):
        """Create a new Server"""

        data = request.get_json()
        nombre = data['nombre']
        descripcion = data['descripcion']
        if Server.create(id_usuario,nombre,descripcion):
           return jsonify({'message': f'Servidor "{nombre}" agregado al usuario con ID {id_usuario} y la descripcion {descripcion}'}), 201
        else:
            return jsonify({'message': 'Error al agregar el servidor'}), 500
        
        
    @classmethod
    def get_name(cls, nombre_servidor):
        server_objects = Server.get_name(nombre_servidor)  # Obtenemos una lista de instancias de la clase Server

        if server_objects:
            cantidad_usuarios=Server.get_cant_user(server_objects['idservidor'])
            server_objects['cantidad_usuarios'] = cantidad_usuarios
            return server_objects, 200
        else:
            return jsonify({'message': 'Servidor no encontrado'}), 404
        
    @classmethod
    def join(cls,id_usuario,id_servidor):
        if Server.exists(id_usuario, id_servidor):
            raise duplicateError
        Server.join(id_usuario, id_servidor)
        return {'message': 'Usuario unido exitosamente al servidor'}, 200
   
        
    @classmethod
    def get_channel_user(cls,id_usuario,id_servidor):
        channels = Server.get_channel_user(id_usuario,id_servidor)
        if channels:
            return jsonify(channels), 200
        else:
            return jsonify({'message': 'No se encontraron canales para el usuario y servidor especificados'}), 404
