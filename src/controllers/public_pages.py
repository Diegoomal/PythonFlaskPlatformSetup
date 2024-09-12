from flask import Blueprint, render_template, redirect, url_for, session        # type: ignore

public_pages = Blueprint('public_pages', __name__)

@public_pages.route('/')
def index():
    return render_template('index.html')
