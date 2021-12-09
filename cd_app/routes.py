from re import template
from cd_app import app
from flask import render_template


@app.route('/')
def homePage():
    return render_template('home.html', title='Car Collection Home Page')

@app.route('/about')
def aboutPage():
    return render_template('about.html', title="What We Do")

