"""Greeting Flask app."""
from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

#route for your registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user:
            return redirect(url_for('login'))

        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('register.html')

#route to login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email, password=password).first()
        if user:
            session['email'] = email

            return redirect(url_for('index'))

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/')
def index():
    # Check if the user is logged in
    if 'email' in session:
        return 'Welcome, ' + session['email'] + '!'

    return redirect(url_for('login'))



#debug off
if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0', port = 5000)

