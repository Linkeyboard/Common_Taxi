from flask import Flask,render_template,url_for,session,request,session,Blueprint,redirect
from database import db_session,init_db
from models import User,Stu,Order,Join
import json
import requests
from get_accesstoken import access_token
import random
from bs4 import BeautifulSoup


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
            information = requests.get("https://api.weixin.qq.com/cgi-bin/user/info?access_token="+access_token+"&openid="+session['openid']+"&lang=zh_CN")
            print(information.json())
            if information:
                session['nickname'] = information.json()['nickname']
                session['headimgurl'] = information.json()['headimgurl']
                print(session['nickname'],session['headimgurl'])
            Student = Stu.query.filter_by(openid = openid).first()
            if Student:
                session['stuid'] = Student.stuid
                return redirect('/lk/mapserch')
    return render_template('index.html',Session = session)

@webapp.route('/login', methods=['POST'])
def login():
    data = {}
    data['stuid'] = request.form['stuid']
    data['pwd'] = request.form['pwd']
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
    res = requests.post('http://222.194.15.1:7777/pls/wwwbks/bks_login2.login',data, headers = headers)
    soup = BeautifulSoup(res.text,"html.parser")
    if soup.title:
        newStu = Stu(session['openid'], data['stuid'],session['nickname'],session['headimgurl'])
        session['stuid'] = data['stuid']
        db_session.add(newStu)
        db_session.commit()
        return "Successful"
    return "Fail"

@webapp.route('/test')
def test():
    session['area'] = 2
    return render_template('test.html', Session = session)

@webapp.route('/hello')
def hello_world():
    return 'hello world!'

@webapp.route('/my')
def My():
    if 'openid' not in session:
        session['openid'] = 'oqK-bxCCAxRaEHslFrJ7_UGQ8JNM'
    session['area'] = 3
    #print(session.get('test',None))
    print('get-openid:',session.get('openid',None))
    if 'openid' in session:
        information = requests.get("https://api.weixin.qq.com/cgi-bin/user/info?access_token="+access_token+"&openid="+session['openid']+"&lang=zh_CN")
        return render_template('my.html', Session = session, information = information.json())
    return 'No openid'

@webapp.route('/maptest')
def Maptest():
    session['area'] = 2
    return render_template('maptest.html', Session = session)

@webapp.route('/mapserch')
def Mapserch():
    session['area'] = 1
    return render_template('mapserch.html', Session = session)




@webapp.route('/selector')
def selector():
    session['area'] = 2
    return render_template('selector.html', Session = session)


@webapp.route('/newcommontaxi')
def newcommontaxi():
    session['area'] = 2
    return render_template('newcommontaxi.html', Session = session)


@webapp.route('/personalinformation')
def personalinformation():
    session['area'] = 3
    if 'stuid' not in session:
        session['stuid'] = 'XXXXXXX'
    if 'openid' not in session:
        session['openid'] = 'oqK-bxCCAxRaEHslFrJ7_UGQ8JNM'
    user = User.query.filter_by(openid = session['openid']).first()
    has_logged = 0
    if user:
        has_logged = 1
        session['name'] = user.name
        session['wechatid'] = user.wechatid
        session['sex'] = user.sex
        session['phone'] = user.phone
    information = requests.get("https://api.weixin.qq.com/cgi-bin/user/info?access_token="+access_token+"&openid="+session['openid']+"&lang=zh_CN")
    return render_template('personalinformation.html', Session = session , has_logged = has_logged, information = information.json())

@webapp.route('/changeinformation',methods=['POST'])
def changeinformation():
    session['area'] = 3
    user = User(session['openid'], request.form['stuname'],request.form['phone'],session['stuid'],request.form['wechatid'],int(request.form['sex']))
    olduser = User.query.filter_by(openid=session['openid']).first()
    if olduser:
        db_session.delete(olduser)
    db_session.add(user)
    db_session.commit()
    return ""


@webapp.route('/addtaxi',methods=['POST'])
def addtaxi():
    if 'openid' not in session:
        session['openid'] = 'oqK-bxCCAxRaEHslFrJ7_UGQ8JNM'
    neworder = Order(session['openid'] ,request.form['fromwhere'],request.form['towhere'],request.form['whenis'])
    db_session.add(neworder)
    db_session.commit()
    return ""



@webapp.route('/showcommontaxi')
def showcommontaxi():
    orderlist = Order.query.filter(Order.countis < 5).all()
    print('orderlist',orderlist)
    data = {}
    datasend = []
    for i in orderlist:
        data = {}
        stutmp = Stu.query.filter_by(openid = i.openid).first()
        if stutmp:
            data['openid'] = stutmp.openid
            data['nickname'] = stutmp.nickname
            data['headimgurl'] = stutmp.headimgurl
            data['towhere'] = i.towhere
            data['fromwhere'] = i.fromwhere
            data['whenis'] = i.whenis
            data['countis'] = i.countis
            data['id'] = i.id
            data['openid'] = i.openid
            datasend.append(data)
    print('datasend',datasend)
    return render_template('showcommontaxi.html', Session = session, data = datasend)

@webapp.route('/taxidetail/<tmpid>',methods=['POST','GET'])
def taxidetail(tmpid):
    findorder = Order.query.filter_by(id=tmpid).first()
    who = Stu.query.filter_by(openid=findorder.openid).first()
    data={}
    data['headimgurl'] = who.headimgurl
    data['nickname'] = who.nickname
    data['towhere'] = findorder.towhere
    data['fromwhere'] = findorder.fromwhere
    data['whenis'] = findorder.whenis
    data['countis'] = findorder.countis + 1
    data['id'] = findorder.id
    data['openid'] = who.openid
    if Join.query.filter_by(followid = tmpid,openid = session['openid']).first():
        return render_template('mydetail.html',Session = session, data = data)
    else:
        return render_template('detail.html',Session = session, data = data)


@webapp.route('/mytaxidetail/<tmpid>',methods=['POST','GET'])
def mytaxidetail(tmpid):
    findorder = Order.query.filter_by(id=tmpid).first()
    who = Stu.query.filter_by(openid=findorder.openid).first()
    data={}
    data['headimgurl'] = who.headimgurl
    data['nickname'] = who.nickname
    data['towhere'] = findorder.towhere
    data['fromwhere'] = findorder.fromwhere
    data['whenis'] = findorder.whenis
    data['countis'] = findorder.countis + 1
    data['id'] = findorder.id
    data['openid'] = who.openid
    return render_template('mydetail.html',Session = session, data = data)

# @webapp.route('/showdetail')
# def showdetail():

@webapp.route('/addfollow',methods=['POST'])
def addfollow():
    if 'openid' not in session:
        session['openid'] = 'oqK-bxCCAxRaEHslFrJ7_UGQ8JNM'
    newjoin = Join(session['openid'],request.form['followid'])
    findjoin = Join.query.filter_by(openid = session['openid'], followid = request.form['followid']).first()
    if not findjoin:
        db_session.add(newjoin)
        Order.query.filter_by(id = request.form['followid']).update({Order.countis:Order.countis+1})
        db_session.commit()
        return "success"
    else:
        return "fail"

@webapp.route('/mytaxi')
def mytaxi():
    if 'openid' not in session:
        session['openid'] = 'oqK-bxCCAxRaEHslFrJ7_UGQ8JNM'
    print(session['openid'])
    myorder = Order.query.filter_by(openid = session['openid']).all()
    data = {}
    datasend = []
    for i in myorder:
        data = {}
        stutmp = Stu.query.filter_by(openid = i.openid).first()
        if stutmp:
            data['openid'] = stutmp.openid
            data['nickname'] = stutmp.nickname
            data['headimgurl'] = stutmp.headimgurl
            data['towhere'] = i.towhere
            data['fromwhere'] = i.fromwhere
            data['whenis'] = i.whenis
            data['countis'] = i.countis
            data['id'] = i.id
            datasend.append(data)
    print('datasend',datasend)
    return render_template('showcommontaxi.html', Session = session, data = datasend)


@webapp.route('/myjoin')
def myjoin():
    print('openid',session['openid'])
    tmpjoin = Join.query.filter_by(openid = session['openid']).all()
    data = {}
    datasend = []
    for i in tmpjoin:
        data = {}
        tmporder = Order.query.filter_by(id = i.followid).first()
        if tmporder:
            data['towhere'] = tmporder.towhere
            data['fromwhere'] = tmporder.fromwhere
            data['whenis'] = tmporder.whenis
            data['countis'] = tmporder.countis
            data['id'] = tmporder.id
            tmpstu = Stu.query.filter_by(openid = tmporder.openid).first()
            if tmpstu:
                data['headimgurl'] = tmpstu.headimgurl
                data['nickname'] = tmpstu.nickname
            datasend.append(data)
    return render_template('showcommontaxi.html', Session = session, data = datasend)


@webapp.route('/addhome/<how>')
def addhome(how):
    session['area'] = 2
    return render_template('addhome.html', Session = session,how = how)



app.register_blueprint(webapp)
app.run(debug = True, host ='0.0.0.0', port=8008) 

