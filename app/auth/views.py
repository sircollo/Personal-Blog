from flask import render_template,redirect,request,url_for,flash,session
from . import auth
from ..models import User 
from .forms import LoginForm
from flask_login import login_user
from .. import db


@auth.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if request.method == 'POST':
    if request.form.get('email') == "collotests@gmail.com" and request.form.get('password') == 'tests':
      session['logged_in'] = True
      return redirect("/admin")
    else:
      flash("Invalid username or password")     
      
  return render_template('auth/login.html', login_form = form)
    

    