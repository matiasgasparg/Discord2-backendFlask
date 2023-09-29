from ..models.message_model import Message
from ..models.channel_model import Channel
from flask import request,jsonify
# from decimal import Decimal
from ..models.exceptions import userNotFound,CustomException,InvalidDataError,duplicateError

class messageController:
    @classmethod
    def send_message(cls,id_usuario,id_servidor,id_canal):
        data = request.get_json()
        message = data.get('mensaje', '')
        date_hour=data.get('fecha_Hora','')
        if not message:
            raise duplicateError

        Message.send(id_usuario, id_servidor, id_canal, message)
        return jsonify({'message': 'Mensaje enviado exitosamente'}), 201
    @classmethod
    def edit_message(cls,id_usuario, id_canal, id_mensaje):
            data = request.get_json()
            new_message = data.get('nuevo_mensaje', '')

            if not new_message:
                return jsonify({'message': 'El nuevo mensaje no puede estar vacío'}), 400

            # Verificar si el mensaje pertenece al usuario y al canal especificados
            menssage_user_channel = Channel.get_chat_user(id_canal)
            edit_message = next((message for message in menssage_user_channel if message['idchat'] == id_mensaje), None)

            if edit_message and edit_message['id_usuario'] == id_usuario:
                if Message.edit(id_mensaje, new_message):
                    return jsonify({'message': 'Mensaje editado exitosamente'}), 200
                else:
                    return jsonify({'message': 'No se puede editar el mensaje. No se encontró el mensaje o no tienes permiso'}), 403
            
    @classmethod
    def delete(cls,id_usuario,id_canal,id_mensaje):
            # Verificar si el mensaje pertenece al usuario y al canal especificados
            menssage_user_channel = Channel.get_chat_user(id_canal)
            delete_message = next((message for message in menssage_user_channel if message['idchat'] == id_mensaje), None)

            if delete_message and delete_message['id_usuario'] == id_usuario:
                if Message.delete(id_mensaje):
                    return jsonify({'message': 'Mensaje ha sido eliminado'}), 200
                else:
                    return jsonify({'message': 'No se puede eliminar el mensaje. No se encontró el mensaje o no tienes permiso'}), 403

    