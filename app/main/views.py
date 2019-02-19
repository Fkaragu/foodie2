from flask import render_template,request,redirect,url_for
from . import main
from ..models import User
from .forms import CommentForm

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to the foodie app'
    return render_template("index.html")

@main.route('/options')
def options():
    '''
    View root page function that returns the index page and its data
    '''
    comment_form = CommentForm()
    return render_template("search.html", comment_form = comment_form)
