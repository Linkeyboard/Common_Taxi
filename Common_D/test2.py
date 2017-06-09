from flask import Flask, Blueprint

app=Flask(__name__,static_url_path='/lk/static')



webapp = Blueprint('webapp', __name__,url_prefix='/lk')

@webapp.route('/')
def Index():
    return "hello world"

app.register_blueprint(webapp)
app.run(host='0.0.0.0',port=8008)
