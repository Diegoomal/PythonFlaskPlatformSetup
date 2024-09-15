from . import app
from .controllers.auth import role_required
from asgiref.wsgi import WsgiToAsgi                                             # type: ignore
from flask_login import login_required, current_user                            # type: ignore
from flask import render_template, redirect, url_for, session, request, jsonify, flash # type: ignore


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'GET':
        return render_template('dashboard.html')


@app.route('/admin')
@login_required
@role_required('admin')
def admin_panel():
    return render_template('admin.html')


@app.route('/user')
@login_required
@role_required('user')
def user_panel():
    return render_template('user.html')


# if __name__ == '__main__':
#     app.run(port=5000, debug=True)


asgi_app = WsgiToAsgi(app)
