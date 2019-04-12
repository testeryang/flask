from flask import Flask, request, Blueprint
from flask_apscheduler import APScheduler

import app

timer = Blueprint('timer', __name__)
scheduler = APScheduler()

def task1(a, b):
    print(str(a) + ' ' + str(b))

@timer.route('/pause')
def pausetask(id):  # 暂停
    scheduler.pause_job(id)
    return "Success!"

@timer.route('/resume')
def resumetask(id):  # 恢复
    scheduler.resume_job(id)
    return "Success!"

@timer.route('/gettask')
def get_task(id):  # 获取
    jobs = scheduler.get_jobs()
    print(jobs)
    return '111'

def remove_task(id):  # 移除
    scheduler.delete_job(id)
    return 111

@timer.route('/addjob', methods=['GET', 'POST'])
def addtask():
    scheduler.add_job(func=task1, id='1', args=(1, 2), trigger='interval', seconds=5, replace_existing=True)
    return 'sucess'

# app.app.config.from_object('config')
# scheduler.init_app(app=app)
# scheduler.start()
