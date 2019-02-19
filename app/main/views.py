from flask import render_template,request,redirect,url_for
from . import main
from ..models import User
import requests
import json

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to the foodie app'
    return render_template("index.html")

@main.route('/search')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    random = requests.get('https://www.food2fork.com/api/search?key=ccdac9a346b2142bac88c41c214a941c').json

    return render_template("food.html", random = random)
