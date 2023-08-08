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
        for (id_usuario, name,username,email,password,datebirth,img_perfil) in cursor:
            usuario = {
                'id_usuario': id_usuario,
                'name': name,
                'username': username,
                'email':email,
                'password': password,
                'datebirth': datebirth,
                'img_perfil':img_perfil
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
            return {'id_usuario': usuario[0], 'name': usuario[1],'username':usuario[2],'email': usuario[3], 'contraseña': usuario[4], 'fecha_creacion': usuario[5],'img_perfil':usuario[6]}
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
        return 
#Funcion para obtener los servidores de los usuarios
def obtener_servidor(id_usuario):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Consulta SQL para obtener los servidores del usuario con el ID especificado
        sql = "SELECT servidor.* FROM `usuarios-servidor` AS us " \
              "JOIN `servidor` AS servidor ON us.id_server = servidor.idservidor " \
              "WHERE us.id_user = %s"

        cursor.execute(sql, (id_usuario,))

        # Obtener todos los registros de servidores del usuario
        servidores = cursor.fetchall()

        # Cerrar la conexión y el cursor
        cursor.close()
        connection.close()

        return servidores

    except Exception as e:
        print("Error al obtener los servidores:", e)
        return []

def agregar_servidor(id_usuario, nombre_servidor,descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        # Insertar el nuevo servidor en la tabla `servidor`
        sql_insert_servidor = "INSERT INTO servidor (nombre,descripcion) VALUES (%s,%s)"
        cursor.execute(sql_insert_servidor, (nombre_servidor,descripcion))
        id_servidor_insertado = cursor.lastrowid

        # Insertar la relación entre el usuario y el servidor en la tabla `usuarios-servidor`
        sql_insert_relacion = "INSERT INTO `usuarios-servidor` (id_user, id_server) VALUES (%s, %s)"
        cursor.execute(sql_insert_relacion, (id_usuario, id_servidor_insertado))

        conexion.commit()
        cursor.close()
        conexion.close()

        return True
    except Exception as e:
        print(f"Error al agregar el servidor: {str(e)}")
        return False
# Función para obtener todos los usuarios de la base de datos
def obtener_todos_los_servidores():
    try:
        connection = conectar()
        cursor = connection.cursor()

        sql = "SELECT * FROM servidor"
        cursor.execute(sql)

        servidores = []
        for (idservidor,nombre,descripcion) in cursor:
            servidor = {
                'idservidor': idservidor,
                'nombre': nombre,
                'descripcion': descripcion,
        
            }
            servidores.append(servidor)

        cursor.close()
        connection.close()

        return servidores
    except Exception as e:
        print("Error al obtener los servidores:", e)
        return []

def obtener_servidor_por_nombre(nombre_servidor):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        # Realizar la consulta SQL para obtener el servidor por su nombre
        sql = "SELECT * FROM servidor WHERE nombre = %s"
        values = (nombre_servidor,)
        cursor.execute(sql, values)

        # Obtener el resultado de la consulta
        servidor = cursor.fetchone()

        # Cerrar la conexión con la base de datos
        cursor.close()
        conexion.close()

        if servidor:
            return {
                'idservidor': servidor[0],
                'nombre': servidor[1],
                'descripcion':servidor[2]
                # Puedes agregar más atributos del servidor aquí si es necesario
            }
        else:
            return None
    except Exception as e:
        print("Error al obtener el servidor por nombre:", e)
        return None

def agregar_canales(nombre, id_servidor):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        # Consulta SQL para insertar el nuevo canal en la tabla 'canales'
        consulta_canales = "INSERT INTO canales (nombre) VALUES (%s)"
        valores_canales = (nombre,)
        cursor.execute(consulta_canales, valores_canales)
        canal_id = cursor.lastrowid  # Obtenemos el ID del canal recién insertado

        # Consulta SQL para insertar la vinculación entre el canal y el servidor en la tabla 'id_canal_servidor'
        consulta_id_canal_servidor = "INSERT INTO id_canal_servidor (idsv, idcanal) VALUES (%s, %s)"
        valores_id_canal_servidor = (id_servidor, canal_id)
        cursor.execute(consulta_id_canal_servidor, valores_id_canal_servidor)

        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print("Error al agregar el canal:", e)
        conexion.rollback()
        return False

def obtener_canales_usuario_servidor(id_usuario, id_servidor):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        # Realizar la consulta SQL para obtener los canales del servidor que corresponden al usuario
        sql = "SELECT c.* FROM canales AS c " \
              "JOIN id_canal_servidor AS p ON c.idcanal = p.idcanal " \
              "JOIN `usuarios-servidor` AS us ON p.idsv = us.id_server " \
              "WHERE us.id_user = %s AND p.idsv = %s"
        values = (id_usuario, id_servidor)
        cursor.execute(sql, values)

        # Obtener los resultados de la consulta
        canales = []
        for canal in cursor.fetchall():
            canal_dict = {
                'idcanal': canal[0],
                'nombre': canal[1]
                # Puedes agregar más atributos del canal aquí si es necesario
            }
            canales.append(canal_dict)

        # Cerrar la conexión con la base de datos
        cursor.close()
        conexion.close()

        # Formatear los datos de los canales en el formato esperado
    # Formatear los datos de los canales en el formato esperado
        canales_formateados = [
            {'idCanal': canal['idcanal'], 'nombre': canal['nombre']}  # Agrega más atributos si es necesario
            for canal in canales
        ]

        return canales_formateados
    except Exception as e:
        print("Error al obtener los canales del servidor:", e)
        return None
def obtener_chats_usuarios_canal(id_canal):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        # Realizar la consulta SQL para obtener los chats y usuarios del canal
        sql = "SELECT u.img_perfil as imagen, u.username AS username, c.mensaje AS mensaje, c.fecha_hora AS fecha_hora " \
              "FROM usuarios AS u " \
              "JOIN `usuario-canales-chats` AS ucc ON u.id_usuario = ucc.iduser " \
              "JOIN chat AS c ON ucc.idchat = c.idchat " \
              "WHERE ucc.idcanal = %s"
        values = (id_canal,)
        cursor.execute(sql, values)

        # Obtener los resultados de la consulta
        chats_usuarios_canal = []
        for (imagen,usuario, mensaje, fecha_hora) in cursor.fetchall():
            chat_usuario_dict = {
                'imagen':imagen,
                'usuario': usuario,
                'mensaje': mensaje,
                'fecha_hora': fecha_hora,
            }
            chats_usuarios_canal.append(chat_usuario_dict)

        # Cerrar la conexión con la base de datos
        cursor.close()
        conexion.close()

        return chats_usuarios_canal
    except Exception as e:
        print("Error al obtener los chats y usuarios del canal:", e)
        return None

def enviar_mensaje(id_usuario, id_servidor, id_canal, mensaje):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Insertar el mensaje en la tabla 'chat' con fecha y hora actuales
        sql_insert_mensaje = "INSERT INTO chat (mensaje, fecha_hora) VALUES (%s, NOW())"
        cursor.execute(sql_insert_mensaje, (mensaje,))
        id_mensaje_insertado = cursor.lastrowid

        # Insertar la relación entre el usuario, canal y mensaje en la tabla 'usuario-canales-chats'
        sql_insert_relacion = "INSERT INTO `usuario-canales-chats` (iduser, idcanal, idchat) VALUES (%s, %s, %s)"
        cursor.execute(sql_insert_relacion, (id_usuario, id_canal, id_mensaje_insertado))

        connection.commit()
        cursor.close()
        connection.close()

        return True
    except Exception as e:
        print("Error al enviar el mensaje:", e)
        return False
def obtener_cantidad_usuarios_servidor(id_servidor):
    try:
        connection = conectar()
        cursor = connection.cursor()

        sql = "SELECT COUNT(id_user) FROM `usuarios-servidor` WHERE id_server = %s"
        cursor.execute(sql, (id_servidor,))
        cantidad_usuarios = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return cantidad_usuarios
    except Exception as e:
        print("Error al obtener la cantidad de usuarios del servidor:", e)
        return 0
def unirse_a_servidor(id_usuario, id_servidor):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        # Insertar la relación entre el usuario y el servidor en la tabla `usuarios-servidor`
        sql_insert_relacion = "INSERT INTO `usuarios-servidor` (id_user, id_server) VALUES (%s, %s)"
        cursor.execute(sql_insert_relacion, (id_usuario, id_servidor))

        conexion.commit()
        cursor.close()
        conexion.close()

        return True
    except Exception as e:
        print("Error al unirse al servidor:", e)
        conexion.rollback()
        return False