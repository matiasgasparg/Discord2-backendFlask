class User_date:
    def __init__(self, **kwargs):
        self.id_usuario = kwargs.get('id_usuario')
        self.name = kwargs.get('name')
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.datebirth = kwargs.get('datebirth')
        self.img_perfil = kwargs.get('img_perfil')

    def serialize(self):
        return {
            "id_usuario": self.id_usuario,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "datebirth": str(self.datebirth),
            "img_perfil": self.img_perfil
        }

class Server_date:
    def __init__(self, **kwargs):
        self.idservidor = kwargs.get('idservidor')
        self.nombre = kwargs.get('nombre')
        self.descripcion = kwargs.get('descripcion')
    
    def serialize(self):
        return {
            "idservidor": self.idservidor,
            "nombre": self.nombre,
            "descripcion": self.descripcion
        }
class Channel_date:
    def __init__(self, **kwargs):
        self.idcanal = kwargs.get('idcanal')
        self.nombre = kwargs.get('nombre')
    def serialize(self):
        return {
            "idcanal": self.idcanal,
            "nombre": self.nombre
        }
class Message_date:
    def __init__(self, **kwargs):
        self.idchat=kwargs.get('idchat')
        self.mensaje=kwargs.get('mensaje')
        self.fecha_hora=kwargs.get('fecha_hora')
    def serialize(self):
        return {
            "idchat": self.idchat,
            "mensaje": self.mensaje,
            "fecha_hora": self.fecha_hora

        }
 
