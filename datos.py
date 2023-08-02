import mysql.connector
from mysql.connector import errors
import config
def conectar():
    """Conectar con la base de datos y devolver un obj conexion."""
    try:
        conn = mysql.connector.connect(**config.credenciales)
    except errors.DatabaseError as err:
        print("Error al conectar.", err)
    else:
        return conn

def crear_usuario(name,username,email,password,datebirth):
    try:
        connection = conectar()
        cursor = connection.cursor()

        sql = "INSERT INTO usuarios (name,username,email,password,datebirth) VALUES (%s, %s, %s, %s, %s)"
        val = (name,username,email,password,datebirth)

        cursor.execute(sql, val)

        connection.commit()
        cursor.close()
        connection.close()

        return True
    except Exception as e:
        print("Error al crear usuario:", e)
        return False

# Función para obtener todos los usuarios de la base de datos
def obtener_usuarios():
    try:
        connection = conectar()
        cursor = connection.cursor()

        sql = "SELECT * FROM usuarios"
        cursor.execute(sql)

        usuarios = []
        for (id_usuario, name,username,email,password,datebirth) in cursor:
            usuario = {
                'id_usuario': id_usuario,
                'name': name,
                'username': username,
                'email':email,
                'password': password,
                'datebirth': datebirth
            }
            usuarios.append(usuario)

        cursor.close()
        connection.close()

        return usuarios
    except Exception as e:
        print("Error al obtener usuarios:", e)
        return []

# Función para obtener un usuario por su ID de la base de datos
def obtener_usuario_por_id(id_usuario):
    try:
        connection = conectar()
        cursor = connection.cursor()

        sql = "SELECT * FROM usuarios WHERE id_usuario = %s"
        val = (id_usuario,)
        cursor.execute(sql, val)

        usuario = cursor.fetchone()

        cursor.close()
        connection.close()

        if usuario:
            return {'id_usuario': usuario[0], 'nombre': usuario[1], 'email': usuario[2], 'contraseña': usuario[3], 'fecha_creacion': usuario[4]}
        else:
            return None
    except Exception as e:
        print("Error al obtener usuario:", e)
        return None

# Función para actualizar un usuario por su ID en la base de datos
def actualizar_usuario(id_usuario, nombre, email, contraseña):
    try:
        connection = conectar()
        cursor = connection.cursor()

        sql = "UPDATE usuarios SET nombre = %s, email = %s, contraseña = %s WHERE id_usuario = %s"
        val = (nombre, email, contraseña, id_usuario)
        cursor.execute(sql, val)

        connection.commit()
        cursor.close()
        connection.close()

        return True
    except Exception as e:
        print("Error al actualizar usuario:", e)
        return False

# Función para eliminar un usuario por su ID de la base de datos
def eliminar_usuario(id_usuario):
    try:
        connection = conectar()
        cursor = connection.cursor()

        sql = "DELETE FROM usuarios WHERE id_usuario = %s"
        val = (id_usuario,)
        cursor.execute(sql, val)

        connection.commit()
        cursor.close()
        connection.close()

        return True
    except Exception as e:
        print("Error al eliminar usuario:", e)
        return False