from . import db
from flask_login import UserMixin                                               # type: ignore
from flask_bcrypt import generate_password_hash, check_password_hash            # type: ignore

class User(UserMixin, db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(150), nullable=False, unique=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    roles = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def has_role(self, role):
        return role in self.roles.split(',')

    def add_role(self, role):
        if self.roles is not None:
            roles_list = self.roles.split(',')
            if role not in roles_list:
                roles_list.append(role)
                self.roles = ','.join(roles_list)
        else: 
            roles_list = []
            roles_list.append(role)
            self.roles = ','.join(roles_list)

    def remove_role(self, role):
        roles_list = self.roles.split(',')
        if role in roles_list:
            roles_list.remove(role)
            self.roles = ','.join(roles_list)

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return f'User({self.username})'

    def __eq__(self, other):
        if isinstance(other, User):
            return self.id == other.id
        return False
