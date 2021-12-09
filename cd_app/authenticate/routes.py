from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user,login_required,current_user

from cd_app.models import db
from .forms import userForm
from cd_app.models import User

auth = Blueprint('authenticate',__name__,template_folder='auth_templates')

@auth.route('/login')
def logIn():
    return render_template('log_in.html')

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
            
    return render_template('sign_up.html', form=auth_form)