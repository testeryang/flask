from flask import Blueprint
from flask_apscheduler import APScheduler

timers = Blueprint('timers', __name__)
scheduler = APScheduler()
scheduler.start()

def add_job():
    print("这是定时任务")

@timers.route('/pause')
def pausetask(id):  # 暂停
    scheduler.pause_job(id)
    return "Success!"

@timers.route('/resume')
def resumetask(id):  # 恢复
    scheduler.resume_job(id)
    return "Success!"

@timers.route('/gettask')
def get_task(id):  # 获取
    jobs = scheduler.get_jobs()
    print(jobs)
    return '111'

def remove_task(id):  # 移除
    scheduler.delete_job(id)
    return 111



