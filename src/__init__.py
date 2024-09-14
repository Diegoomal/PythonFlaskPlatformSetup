import os
from datetime import timedelta

from dotenv import load_dotenv                                                  # type: ignore
load_dotenv()

from flask import Flask                                                         # type: ignore
from flask_bcrypt import Bcrypt                                                 # type: ignore
from flask_migrate import Migrate                                               # type: ignore
from flask_login import LoginManager                                            # type: ignore
from flask_sqlalchemy import SQLAlchemy                                         # type: ignore


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configurações do app
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)

    db.init_app(app)
    migrate = Migrate(app, db)

    # Inicializar o login manager
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Define a página de login

    # Register blueprint de autenticação
    from .controllers.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Register blueprint de páginas públicas
    from .controllers.public_pages import public_pages as public_pages_blueprint
    app.register_blueprint(public_pages_blueprint)

    return app

app = create_app()
