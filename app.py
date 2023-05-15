from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


# import files in the sys
# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# """Greeting Flask app."""
# from flask import Flask, render_template, request, redirect, session
# from app.model import db
# from app.model import User
# from app.forms import RegistrationForm, LoginForm

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SECRET_KEY'] = 'some-secret-string'
# db.init_app(app)

# @app.route('/')
# def index():
#     if 'username' in session:
#         return 'Logged in as ' + session['username'] + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
#     return "You are not logged in <br><a href = '/login'></b>click here to log in</b></a>"

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         email = form.email.data
#         password = form.password.data
#         user = User.query.filter_by(email=email).first()
#         if user is not None and user.check_password(password):
#             session['username'] = email
#             return redirect('/')
#         else:
#             return 'Invalid email or password'
#     return render_template('login.html', form=form)

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         email = form.email.data
#         password = form.password.data
#         user = User(email=email, password=password)
#         db.session.add(user)
#         db.session.commit()
#         return redirect('/')
#     return render_template('register.html', form=form)

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect('/')



#debug off
if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0', port = 5000)

