from flask import Blueprint

from ..controllers.server_controller import serverController

server_bp = Blueprint('server_bp', __name__)

server_bp.route('/<int:id_usuario>',methods = ['GET'])(serverController.get)
server_bp.route('/', methods=['GET'])(serverController.get_all)
server_bp.route('/<int:id_usuario>', methods=['POST'])(serverController.create)
server_bp.route('/<nombre_servidor>', methods=['GET'])(serverController.get_name)
server_bp.route('/<int:id_usuario>/<int:id_servidor>', methods=['POST'])(serverController.join)
server_bp.route('/<int:id_usuario>/<int:id_servidor>', methods=['GET'])(serverController.get_channel_user)
