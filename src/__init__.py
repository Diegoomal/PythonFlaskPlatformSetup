import os
from flask import Flask                                                         # type: ignore
from flask_sqlalchemy import SQLAlchemy                                         # type: ignore
from flask_bcrypt import Bcrypt                                                 # type: ignore
from flask_migrate import Migrate                                               # type: ignore

# Carrega variáveis do .env
from dotenv import load_dotenv                                                  # type: ignore
load_dotenv()


db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    # Configurações do app
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprint de authentication
    from .controllers.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Register blueprint de public pages
    from .controllers.public_pages import _public_pages_ as public_pages_blueprint
    app.register_blueprint(public_pages_blueprint)

    return app
