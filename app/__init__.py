from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.user_bp import user_bp
from .routes.server_bp import server_bp
from .routes.messsage_bp import message_bp
from .routes.channel_bp import channel_bp

from .routes.error_handlers import errors

from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config['UPLOAD_FOLDER'] = 'uploads'  # Carpeta donde se guardarán las imágenes

    CORS(app, supports_credentials=True)

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(user_bp, url_prefix = '/users')
    app.register_blueprint(server_bp, url_prefix = '/servers')
    app.register_blueprint(message_bp, url_prefix = '/messages')
    app.register_blueprint(channel_bp, url_prefix = '/channels')

    app.register_blueprint(errors)

    return app