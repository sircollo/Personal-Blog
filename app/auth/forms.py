from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo,length
from ..models import User
from wtforms import ValidationError


class LoginForm(FlaskForm):
  email = StringField('E-mail',validators=[DataRequired(),Email()])
  password = PasswordField('Password',validators =[DataRequired()])
  remember = BooleanField('Remember me')
  submit = SubmitField('Login')
  

