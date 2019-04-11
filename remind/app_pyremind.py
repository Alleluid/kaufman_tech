import os

from flask import Flask, request
from flask.templating import render_template
from app import app, STATIC_DIR, TEMPLATE_DIR

@app.route('/pyremind')
def pyremind():
    return render_template("pyremind.html")


@app.route("/pyremind/auth")
def pyremind_test():
    return render_template("auth.html")
