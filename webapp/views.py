from webapp import app
from flask import render_template

@app.route('/')
def home():
    context = {
    }
    return render_template('home.html', **context)
