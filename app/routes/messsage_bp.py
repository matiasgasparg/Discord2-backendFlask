from flask import Blueprint

from ..controllers.message_controller import messageController

message_bp = Blueprint('message_bp', __name__)

message_bp.route('/<int:id_usuario>/<int:id_servidor>/<int:id_canal>', methods=['POST'])(messageController.send_message)
message_bp.route('/<int:id_usuario>/<int:id_canal>/<int:id_mensaje>', methods=['PUT'])(messageController.edit_message)
message_bp.route('/<int:id_usuario>/<int:id_canal>/<int:id_mensaje>', methods=['DELETE'])(messageController.delete)