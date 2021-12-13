from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import check_password_hash

from .forms import userForm, LoginForm
from cd_app.models import User

from flask_login import login_user, logout_user,login_required,current_user

auth = Blueprint('authenticate',__name__,template_folder='auth_templates')

from cd_app.models import db

@auth.route('/login', methods=['GET','POST'])
def logIn():
    log_form = LoginForm()
    if request.method == 'POST' and log_form.validate():
        email = log_form.email.data
        password = log_form.password.data 
        remember_me = log_form.remember_me.data

        user = User.query.filter_by(email=email).first()

        if user is None or not check_password_hash(user.password, password):
            return redirect(url_for('authenticate.logIn'))

        login_user(user,remember=remember_me)
        print(current_user)
        return redirect(url_for('homePage'))


    return render_template('log_in.html', form=log_form, title='Log In')

@auth.route('/signup', methods=["POST","GET"])
def signUp():
    auth_form = userForm()
    if request.method == 'POST':
        if auth_form.validate():
            first = auth_form.first_name.data
            last = auth_form.last_name.data
            email = auth_form.email.data
            password = auth_form.password.data

            new_user = User(first,last,email,password)

            db.session.add(new_user)
            db.session.commit()
            
            return redirect(url_for('homePage'))
            
    return render_template('sign_up.html', form=auth_form, title='Sign Up')

@auth.route('/logout')
def logOut():
    logout_user()
    return redirect(url_for('authenticate.logIn'))