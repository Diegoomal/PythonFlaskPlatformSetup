from flask import Blueprint, request, jsonify, session
from .models import User
from . import db, bcrypt

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Verifica se o usuário já existe
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'User already exists'}), 400

    # Cria novo usuário
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    # Valida usuário e senha
    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401

    session['user_id'] = user.id
    return jsonify({'message': 'Login successful'}), 200
