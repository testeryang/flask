from flask import Blueprint, render_template, abort, redirect, url_for

user = Blueprint('user', __name__)

@user.route('/test')
def index():
    return '<h1>hello,this is admin blueprint</h1>'

@user.route('/001')
def tt():
    return render_template("video.html")