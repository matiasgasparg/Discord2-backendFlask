from ..database import DatabaseConnection
from .date_model import Channel_date
class Channel(Channel_date):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    @classmethod
    def create(cls,nombre,id_servidor):
        # Consulta SQL para insertar el nuevo canal en la tabla 'canales'
        query_channel = "INSERT INTO canales (nombre) VALUES (%s)"
        param = nombre,
        result = DatabaseConnection.execute_query(query_channel,params=param)
        id_channel = result.lastrowid
        
        # Consulta SQL para insertar la vinculación entre el canal y el servidor en la tabla 'id_canal_servidor'
        query_id_channel_server = "INSERT INTO id_canal_servidor (idsv, idcanal) VALUES (%s, %s)"
        params = id_servidor,id_channel
        DatabaseConnection.execute_query(query_id_channel_server,params=params)
        
    @classmethod
    def get_chat_user(cls, id_canal):
        # Realizar la consulta SQL para obtener los chats y usuarios del canal
        query = """SELECT u.id_usuario AS id_usuario, u.img_perfil AS imagen, u.username AS username, c.idchat AS idchat, c.mensaje AS mensaje, c.fecha_hora AS fecha_hora
                   FROM usuarios AS u
                   JOIN `usuario-canales-chats` AS ucc ON u.id_usuario = ucc.iduser
                   JOIN chat AS c ON ucc.idchat = c.idchat
                   WHERE ucc.idcanal = %s"""
        param = id_canal,
        results = DatabaseConnection.fetch_all(query, params=param)
        
        # Obtener los resultados de la consulta
        chat_user_channel = []
        if results is not None:
            for result in results:
                chat_user_channel.append({
                    'id_usuario': result[0],
                    'imagen': result[1],
                    'usuario': result[2],
                    'idchat': result[3],
                    'mensaje': result[4],
                    'fecha_hora': result[5]
                })
            return chat_user_channel
        else:
            return False
    
                
        