from flask import Blueprint, render_template, request                           # type: ignore

public_pages = Blueprint('public_pages', __name__)

@public_pages.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
