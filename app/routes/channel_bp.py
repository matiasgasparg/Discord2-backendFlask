from flask import Blueprint

from ..controllers.channel_controller import channelController

channel_bp = Blueprint('channel_bp', __name__)

channel_bp.route('/<int:id_usuario>/<int:id_servidor>', methods=['POST'])(channelController.create)
channel_bp.route('/<int:id_canal>', methods=['GET'])(channelController.get_chat_user)
