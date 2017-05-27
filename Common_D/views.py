from flask import Flask 
from hello import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/hello')
def hello_world():
    return 'hello world!'