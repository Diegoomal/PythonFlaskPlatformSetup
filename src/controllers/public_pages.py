from flask import Blueprint, render_template, redirect, url_for, session        # type: ignore

public_pages = Blueprint('public_pages', __name__)

@public_pages.route('/')
def root():
    return render_template('index.html')

@public_pages.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('dashboard.html')
