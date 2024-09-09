from flask import Blueprint, request, jsonify, session, render_template, redirect, url_for  # type: ignore
from ..models import User
from .. import db, bcrypt

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
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

        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()

        # Valida usuário e senha
        if not user or not user.check_password(password):
            return jsonify({'message': 'Invalid credentials'}), 401

        session['user_id'] = user.id
        return redirect(url_for('public_pages.dashboard'))

    return render_template('login.html')
