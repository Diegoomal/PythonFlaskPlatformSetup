from . import app
from asgiref.wsgi import WsgiToAsgi                                             # type: ignore
from flask_login import login_required, current_user                            # type: ignore
from flask import render_template, redirect, url_for, session, request, jsonify, flash # type: ignore


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'GET':
        return render_template('dashboard.html')


# if __name__ == '__main__':
#     app.run(port=5000, debug=True)


asgi_app = WsgiToAsgi(app)
