"""Greeting Flask app."""
from flask import Flask, request;
from flask import render_template, redirect, url_for, routes
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return redirect(url_for('home'))
    ''' , methods=['POST']
    email = request.form['email']
    password = request.form['password']
    # TODO: validate username and password'''

if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0', port = 5000)