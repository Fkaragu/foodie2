from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post Comment')

class PitchFormL(FlaskForm):
    pitch = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')
