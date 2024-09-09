from flask import Blueprint, request, jsonify, session, render_template, redirect, url_for # type: ignore
from ..models import User
from .. import db, bcrypt

_public_pages_ = Blueprint('public_pages', __name__)

@_public_pages_.route('/', methods=["GET"])
def root():
    return render_template('index.html')

@_public_pages_.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')
