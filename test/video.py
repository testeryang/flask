from flask import Blueprint, render_template, abort, redirect, url_for

video = Blueprint('video', __name__)

@video.route('/test')
def index():
    return '<h1>hello,this is admin blueprint</h1>'

@video.route('/001')
def tt():
    return render_template("video.html")
# if __name__ == '__main__':
#     print(2222)