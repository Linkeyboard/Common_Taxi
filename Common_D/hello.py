from flask import Flask,render_template,url_for,session,request,session,Blueprint
from database import db_session,init_db
from models import User
import json
import requests
from get_accesstoken import access_token
import random

app = Flask(__name__,static_url_path='/lk/static')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
webapp = Blueprint('webapp', __name__,url_prefix='/lk')


@webapp.route('/')
def index():
    session['test'] = 'exist'
    session['area'] = 1
    CODE = request.values.get('code')
    if CODE and CODE not in session:
        session[CODE] = True
        OPENID = requests.get("https://api.weixin.qq.com/sns/oauth2/access_token?appid=wxdbf87277a6a9e2c3&secret=b98898bcfe966fc2c50acaf8d6a87fc3&code="+CODE+"&grant_type=authorization_code").json()
        #print(OPENID)
        openid = OPENID.get('openid')
        if openid:
            print('openid:',openid)
            session['openid'] = openid
    return render_template('index.html',Session = session)

@webapp.route('/test')
def test():
    session['area'] = 2
    return render_template('test.html', Session = session)

@webapp.route('/hello')
def hello_world():
    return 'hello world!'

@webapp.route('/my')
def My():
    session['area'] = 3
    #print(session.get('test',None))
    print('get-openid:',session.get('openid',None))
    if 'openid' in session:
        information = requests.get("https://api.weixin.qq.com/cgi-bin/user/info?access_token="+access_token+"&openid="+session['openid']+"&lang=zh_CN")

        return render_template('my.html', Session = session, information = information.json())
    return 'No openid'

@webapp.route('/maptest')
def Maptest():
    return render_template('maptest.html', Session = session)

@webapp.route('/mapserch')
def Mapserch():
    return render_template('mapserch.html', Session = session)



app.register_blueprint(webapp)
app.run(debug = True, host ='0.0.0.0', port=8008) 

