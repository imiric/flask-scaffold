from flask import render_template

def home():
    context = {
    }
    return render_template('home.html', **context)
