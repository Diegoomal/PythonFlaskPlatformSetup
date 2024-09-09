import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from dotenv import load_dotenv

# Carrega variáveis do .env
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

    # Registra blueprint de autenticação
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
