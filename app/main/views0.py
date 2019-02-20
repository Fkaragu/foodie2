from flask import render_template,request,redirect,url_for
from . import main
from ..models import User,Comment
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

    if id is None:
        abort(404)

    if comment_form.validate_on_submit():
        comment_data = comment_form.comment.data
        new_comment = Comment(c_content = comment_data, c_com_posted_on = datetime.now())
        new_comment.save_comment()

        return redirect(url_for('main.search',id=id))

    all_comments = Comment.get_all_blogs()

    return render_template('search.html',comment_form = comment_form, comments = all_comments)
