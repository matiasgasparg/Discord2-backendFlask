from ..database import DatabaseConnection
from .date_model import Server_date
class Server(Server_date):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    @classmethod
    def get(cls, id_usuario):
        query = """SELECT servidor.* FROM `usuarios-servidor` AS us JOIN `servidor` AS servidor ON us.id_server = servidor.idservidor WHERE us.id_user = %s"""
        params = (id_usuario,)
        results = DatabaseConnection.fetch_all(query, params=params)

        servers = []
        if results is not None:
            for result in results:
                servers.append(cls(**dict(zip(['idservidor', 'nombre', 'descripcion'], result))))
        return servers
     
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM servidor"
        results = DatabaseConnection.fetch_all(query)
        servers = []
        if results is not None:
            for result in results:
                servers.append(cls(**dict(zip(['idservidor', 'nombre', 'descripcion'], result))))
        return servers
    @classmethod
    def get_name(cls, nombre_servidor):
        try:
            query = "SELECT * FROM servidor WHERE nombre = %s"
            params = nombre_servidor,
            result = DatabaseConnection.fetch_one(query, params=params)
            servers = []
            if result:
                return {
                    'idservidor': result[0],
                    'nombre': result[1],
                    'descripcion':result[2]
                    # Puedes agregar más atributos del servidor aquí si es necesario
                }
            else:
                return None
        except Exception as e:
            print("Error al obtener el servidor por nombre:", e)
            return None
    @classmethod
    def get_cant_user(cls,id_servidor):
        try:
            query = "SELECT COUNT(id_user) FROM `usuarios-servidor` WHERE id_server = %s"
            param = id_servidor,
            result = DatabaseConnection.fetch_one(query, params=param)[0]

            if result is not None:
                return result
            else:
                return 0
        except Exception as e:
            print("Error al obtener la cantidad de usuarios del servidor:", e)
            return 0
        


    @classmethod
    def get_channel_user(cls,id_usuario,id_servidor):
        # Realizar la consulta SQL para obtener los canales del servidor que corresponden al usuario
        query = """SELECT c.* FROM canales AS c 
                JOIN id_canal_servidor AS p ON c.idcanal = p.idcanal 
                JOIN `usuarios-servidor` AS us ON p.idsv = us.id_server
                WHERE us.id_user = %s AND p.idsv = %s"""
        params = id_usuario,id_servidor
        results = DatabaseConnection.fetch_all(query,params=params)
        # Obtener los resultados de la consulta
        channels = []
        for channel in results:
            channel_dict = {
                'idcanal' : channel[0],
                'nombre' : channel[1]
                # Puedes agregar más atributos del canal aquí si es necesario
            }
            channels.append(channel_dict)
            
        # Formatear los datos de los canales en el formato esperado
        channel_format = [
            {'idCanal': channel['idcanal'], 'nombre': channel['nombre']}  # Agrega más atributos si es necesario
            for channel in channels
        ]
        return channel_format

        
    
    @classmethod
    def create(cls,id_usuario,nombre,descripcion):
        try:
        
            # Insertar el nuevo servidor en la tabla `servidor`
            query_insert_server = "INSERT INTO servidor (nombre,descripcion) VALUES (%s,%s)"
            params = (nombre, descripcion)
            result = DatabaseConnection.execute_query(query_insert_server,params=params)
            id_server_insert = result.lastrowid
            
            # Insertar la relación entre el usuario y el servidor en la tabla `usuarios-servidor`
            query_insert_relation = "INSERT INTO `usuarios-servidor` (id_user, id_server) VALUES (%s, %s)"
            params = (id_usuario, id_server_insert)
            DatabaseConnection.execute_query(query_insert_relation, params=params)
            return True
        except Exception as e:
            print(f"Error al agregar el servidor: {str(e)}")
            return False
    @classmethod
    def exists(cls,id_usuario,id_servidor):
        # Realizar la consulta SQL para verificar si ya existe una relación
        query = "SELECT iduserserver FROM `usuarios-servidor` WHERE id_user = %s AND id_server = %s"
        params = id_usuario,id_servidor
        result = DatabaseConnection.fetch_one(query,params=params)
        if result:
            return True # Ya existe una relación entre el usuario y el servidor
        return False     # No existe una relación entre el usuario y el servidor
    
    @classmethod
    def join(cls,id_usuario,id_servidor):
        # Insertar la relación entre el usuario y el servidor en la tabla `usuarios-servidor`
        query_insert_relation = "INSERT INTO `usuarios-servidor` (id_user, id_server) VALUES (%s, %s)"
        params = id_usuario,id_servidor
        DatabaseConnection.execute_query(query_insert_relation,params=params)
        