from ..models.channel_model import Channel
from flask import request,jsonify
# from decimal import Decimal
from ..models.exceptions import userNotFound,CustomException,InvalidDataError,duplicateError

class channelController:
    @classmethod
    def create(cls,id_usuario,id_servidor):
        data = request.get_json()
        name = data.get('nombre', '')
        if not name:
            raise duplicateError
        Channel.create(name, id_servidor)
        return jsonify({'message': f'Canal "{name}" agregado correctamente al servidor con ID {id_servidor} para el usuario con ID {id_usuario+1}'}), 201
   
    @classmethod
    def get_chat_user(cls,id_canal):
        chat_user_object= Channel.get_chat_user(id_canal)
        return chat_user_object, 200
    