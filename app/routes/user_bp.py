from flask import Blueprint

from ..controllers.user_controller import userController

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(userController.get_all) #'/user'
user_bp.route('/<int:id_usuario>', methods=['GET'])(userController.get) #'/user/<int:id_usuario>'
user_bp.route('/', methods=['POST'])(userController.create) #'/user'
user_bp.route('/<int:id_usuario>', methods=['PUT'])(userController.update) #'/user/<int:id_usuario>'
user_bp.route('/<int:id_usuario>', methods=['DELETE'])(userController.delete) #'/user/<int:id_usuario>'
user_bp.route('/login', methods=['POST'])(userController.login)
user_bp.route('/upload/<int:user_id>', methods=['POST'])(userController.upload_file)
user_bp.route('/get_image/<image_name>')(userController.get_image) #revisar
