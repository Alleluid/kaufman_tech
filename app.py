import os

from flask import Flask, request
from flask.templating import render_template
from flask_login import LoginManager
from util import get_key_from_file, User

STATIC_DIR = os.path.abspath("static/")
TEMPLATE_DIR = os.path.abspath("templates/")

app = Flask(__name__)
app.secret_key = get_key_from_file()

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    return render_template("home.html")


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        passwd = request.form['passwd']


@app.route('/auth')
def authenticate():
    return render_template("auth.html")


@app.route('/test')
def testing():
    return render_template("testingJS.html")


@app.route('/ajax')
def ajax():
    return render_template("ajax.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


import remind.app_pyremind

if __name__ == '__main__':
    app.run()
