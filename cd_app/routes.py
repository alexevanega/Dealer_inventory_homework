from re import template
from cd_app import app
from flask import render_template

@app.route('/')
def homePage():
    return render_template('home.html', title='Dealer Home Page')

