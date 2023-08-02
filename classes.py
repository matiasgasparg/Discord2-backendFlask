
class User:
    def __init__(self, id_usuario, name, email, username, password, datebirth):
        self.id_usuario = id_usuario
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.datebirth = datebirth

    def verify_password(self, password):
        return self.password == password