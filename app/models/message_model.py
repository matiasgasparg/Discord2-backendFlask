from ..database import DatabaseConnection
from .date_model import Message_date
class Message(Message_date):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    @classmethod
    def send(cls,id_usuario, id_servidor, id_canal, mensaje):
        # Insertar el mensaje en la tabla 'chat' con fecha y hora actuales
        query_insert_message = "INSERT INTO chat (mensaje, fecha_hora) VALUES (%s, NOW())"
        param = mensaje,
        result = DatabaseConnection.execute_query(query_insert_message,params=param)
        id_message_insert = result.lastrowid
        
        # Insertar la relación entre el usuario, canal y mensaje en la tabla 'usuario-canales-chats'
        query_insert_relation = "INSERT INTO `usuario-canales-chats` (iduser, idcanal, idchat) VALUES (%s, %s, %s)"
        params = id_usuario,id_canal,id_message_insert
        DatabaseConnection.execute_query(query_insert_relation,params=params)
        
    @classmethod
    def edit(cls,id_mensaje,nuevo_contenido):
        query = "UPDATE chat SET mensaje = %s WHERE idchat = %s"
        params = nuevo_contenido,id_mensaje
        DatabaseConnection.execute_query(query,params=params)
        return True
        