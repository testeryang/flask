from flask import Blueprint, render_template, abort, redirect, url_for

blog = Blueprint('blog', __name__)

@blog.route('/test')
def index():
    return '<h1>hello,this is admin blueprint</h1>'