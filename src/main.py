from flask import render_template, redirect, url_for, session                   # type: ignore

from . import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
