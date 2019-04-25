from flask import Flask, render_template, url_for, Blueprint, session, current_app
import pymysql
import traceback
import json
from flask import request
from flask_apscheduler import APScheduler

from test.jira import jiratest
from test.video import video
from test.timers import timers
import config

def job_1():
    print(111)

app = Flask(__name__)

@app.errorhandler(404)
def miss404(e):
    return render_template('404.html'),404
@app.errorhandler(500)
def miss500(e):
    return render_template('505.html'),500
app.config['SECRET_KEY']='000000'
app.secret_key='1234567890!@#$%^&*()'

app.register_blueprint(video,url_prefix='/video')
app.register_blueprint(jiratest,url_prefix='/jiratest')
app.register_blueprint(timers,url_prefix='/timers')

@app.route("/echarts", methods=['GET', 'POST'])
def my_mysql():
    db = pymysql.connect("localhost", "root", "root", "pythontest")
    cursor = db.cursor()
    sql = "select `value` from pachong Order By time Desc"
    try:
        # 执行sql语句
        cursor.execute(sql)
        list =cursor.fetchmany(30)
        print(list)
        list2=[]
        for value in list:
            print(value[0])
            list2.append(value[0])
        print(list2)
        # 提交到数据库执行
        db.commit()
        #注册成功之后跳转到登录页面
        listvalue=json.dumps(list2)
        print(listvalue)
        return listvalue
    except:
        #抛出错误信息
        traceback.print_exc()
        # 如果发生错误则回滚
        db.rollback()
        return '注册失败'
    # 关闭数据库连接
    db.close()
#默认路径访问登录页面
@app.route('/')
def login():
    return render_template('login.html')
@app.route('/products')
def products():
    return render_template('products.html')
@app.route('/accounts')
def accounts():
    return render_template('accounts.html')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/login',methods=["GET","POST"])
def getLoginRequest():
#查询用户名及密码是否匹配及存在
    #连接数据库,此前在数据库中创建数据库TESTDB
    db = pymysql.connect("localhost","root","root","pythontest" )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "select * from user where username='"+request.form['username']+"' and password='"+request.form['password']+"'"
    # get  request.args.get
    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(len(results))
        if len(results)==1:
            username=request.form['username']
            session['username'] = username

            return render_template('index.html',username=username)
        else:
            return '用户名或密码不正确'
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
    # 关闭数据库连接
    db.close()
@app.route("/logout")
def logout():
    # session.pop('username')
    return render_template("login.html")

if __name__ == '__main__':
    app.config.from_object(config)
    scheduler = APScheduler()
    scheduler.init_app(app)

    scheduler.start()
    app.run(host="0.0.0.0",port="4000")


