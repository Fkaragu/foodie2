from . import main
from datetime import datetime
from ..models import User,Comment,Pitch
from .forms import CommentForm,PitchFormL
from flask_login import login_required, current_user
from flask import render_template,request,redirect,url_for



# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to the foodie app'
    return render_template("index.html")

@main.route('/options',methods = ['GET', 'POST'])
def Pickupline():

    pitch_form = PitchFormL()

    if pitch_form.validate_on_submit():
        pitch = pitch_form.pitch.data

        new_pitch = Pitch(pitch_content=pitch, user = current_user)
        new_pitch.save_pitch()

        #return redirect(url_for('index.html'))

    all_pitches = Pitch.get_all_pitches()

    title = 'Pickupline Pitch'

    return render_template("allfoods.html", pitch_form = pitch_form, pitches = all_pitches)

@main.route('/pitch/<int:id>',methods = ['GET','POST'])
def pitch(id):

    my_pitch = Pitch.query.get(id)
    comment_form = CommentForm()

    if id is None:
        abort(404)

    if comment_form.validate_on_submit():
        comment_data = comment_form.comment.data
        new_comment = Comment(comment_content = comment_data, pitch_id = id, user = current_user)
        new_comment.save_comment()

        return redirect(url_for('main.pitch',id=id))

    all_comments = Comment.get_comments(id)

    title = 'Comment Section'
    return render_template('pitch.html',pitch = my_pitch, comment_form = comment_form, comments = all_comments, title = title)
