from . import db
from flask_login import UserMixin                                               # type: ignore
from flask_bcrypt import generate_password_hash, check_password_hash            # type: ignore

class User(UserMixin, db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(150), nullable=False, unique=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return f'User({self.username})'

    def __eq__(self, other):
        if isinstance(other, User):
            return self.id == other.id
        return False
