import os
from flask import Flask                                                         # type: ignore
from flask_migrate import Migrate                                               # type: ignore
from flask_sqlalchemy import SQLAlchemy                                         # type: ignore


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
