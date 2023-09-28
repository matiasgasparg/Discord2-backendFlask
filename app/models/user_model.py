from ..database import DatabaseConnection
from app.models.date_model import User_date
class User(User_date):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    @classmethod
    def get(cls, id_usuario):
        """Get a user by id
        Args:
            - id_usuario (int): ID of the user
        Returns:
            - User: User object
        """

        query = """SELECT id_usuario, name, username, email,
        password, datebirth, img_perfil 
        FROM usuarios WHERE id_usuario = %s"""
        params = id_usuario,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(**dict(zip(['id_usuario', 'name', 'username', 'email', 'password', 'datebirth', 'img_perfil'], result)))
        return None

    @classmethod
    def get_all(cls):
        """Get all users
        Returns:
            - list: List of User objects
        """
        query = """SELECT id_usuario, name, username, email,
        password, datebirth, img_perfil 
        FROM usuarios"""
        results = DatabaseConnection.fetch_all(query)

        users = []
        if results is not None:
            for result in results:
                users.append(cls(**dict(zip(['id_usuario', 'name', 'username', 'email', 'password', 'datebirth', 'img_perfil'], result))))
        return users

    @classmethod
    def create(cls, user):
        try:

            """Create a new user
            Args:
                - user (User): User object
            """
            query = """INSERT INTO usuarios (name, username, email,
            password, datebirth, img_perfil) 
            VALUES (%s, %s, %s, %s, %s, %s)"""

            params = user.name, user.username, user.email, \
                     user.password, user.datebirth, user.img_perfil
            DatabaseConnection.execute_query(query, params=params)
            return True
        except Exception as e:
            print("Error al crear usuario:", e)
            return False

    @classmethod
    def update(cls,id_usuario, campo, nuevo_valor):
  
        if campo == 'name':
            query = "UPDATE usuarios SET name = %s WHERE id_usuario = %s"
        elif campo == 'username':
            query = "UPDATE usuarios SET username = %s WHERE id_usuario = %s"
        elif campo == 'email':
            query = "UPDATE usuarios SET email = %s WHERE id_usuario = %s"
        elif campo == 'password':  # Cambiado 'contraseña' a 'password'
            query = "UPDATE usuarios SET password = %s WHERE id_usuario = %s"
        elif campo == 'img_perfil':
            query = "UPDATE usuarios SET img_perfil = %s WHERE id_usuario = %s"
        else:
            raise ValueError("Campo no válido para actualización")
        print(nuevo_valor, id_usuario,query,campo)
        params = (nuevo_valor, id_usuario)

        DatabaseConnection.execute_query(query,params=params)

        return True

    @classmethod
    def delete(cls, id_usuario):
        """Delete a user
        Args:
            - id_usuario (int): ID of the user
        """
        query = "DELETE FROM usuarios WHERE id_usuario = %s"
        params = id_usuario,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def exists(cls, id_usuario):
        query = "SELECT COUNT(*) FROM usuarios WHERE id_usuario = %s"
        params = (id_usuario,)

        result = DatabaseConnection.fetch_one(query, params=params)
        return result[0] > 0 
    @classmethod
    def duplicate(cls,username,email):
        query = "SELECT COUNT(*) FROM usuarios WHERE username = %s OR email = %s"
        params = (username,email,)
        result = DatabaseConnection.fetch_one(query,params=params)
        count = result[0]  # Obtiene el valor del COUNT(*) en la consulta
        return count > 0 # Devuelve True si existe al menos un usuario con el mismo username o email


    