from flask import render_template,request,redirect,url_for
from . import main
from ..models import User

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
    title = 'Welcome to the foodie app'
    return render_template("search.html")
