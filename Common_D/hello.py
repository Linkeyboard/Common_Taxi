from flask import Flask,render_template,url_for,session
from database import db_session,init_db
from models import User


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    session['area'] = 1
    return render_template('index.html',Session = session)

@app.route('/test')
def test():
    session['area'] = 2
    return render_template('test.html', Session = session)

@app.route('/hello')
def hello_world():
    return 'hello world!'

@app.route('/my')
def My():
    session['area'] = 3
    return render_template('my.html', Session = session)


@app.route('/maptest')
def Maptest():
    return render_template('maptest.html', Session = session)


if __name__ == '__main__':
    app.run(debug = True, host ='0.0.0.0') 

