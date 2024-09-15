from ..models import User
from .. import db, bcrypt, login_manager
from flask_login import login_user, logout_user, login_required, current_user   # type: ignore
from flask import Blueprint, request, jsonify, session, render_template, redirect, url_for  # type: ignore

from functools import wraps

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.has_role(role):
                return jsonify({'message': "forbidden—you don't have permission to access this resource"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator


auth = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'GET':
        return render_template('register.html')
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Verifica se o usuário já existe
        user = User.query.filter_by(username=username).first()
        if user:
            return jsonify({'message': 'User already exists'}), 400

        # Cria novo usuário
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.add_role('user')
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        # Valida usuário e senha
        if not user or not user.check_password(password):
            # return jsonify({'message': 'Invalid credentials'}), 401
            return render_template('login.html')

        login_user(user)
        return redirect(url_for('dashboard'))

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return render_template('index.html')
