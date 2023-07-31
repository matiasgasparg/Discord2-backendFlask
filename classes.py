
class User:
    def __init__(self, user_id, name, email, username, password, datebirth):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.datebirth = datebirth

    def verify_password(self, password):
        return self.password == password