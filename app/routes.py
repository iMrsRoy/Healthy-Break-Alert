from flask import render_template
from flask import current_app as app

@app.route('/')
def index():
    return render_template('templates/index.html')

@app.route('/login')
def login():
    return render_template('templates/login.html')



