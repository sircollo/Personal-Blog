from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField,TextAreaField
from wtforms.validators import DataRequired

class CommentsForm(FlaskForm):
    comment = TextAreaField('Add a comment',validators = [DataRequired()])
    
    submit = SubmitField('Submit')
    
class SubscribeForm(FlaskForm):
    username = StringField('Name',validators = [DataRequired()])
    email = StringField('Email',validators = [DataRequired()])    
    submit = SubmitField('Subscribe')