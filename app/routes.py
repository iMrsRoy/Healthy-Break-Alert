from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.models import User
from app.forms import LoginForm, RegistrationForm

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
main_bp = Blueprint('main', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))
    
    return render_template('login.html', title='Sign In', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html', title='Register', form=form)

@main_bp.route('/')
@main_bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')



# from flask import render_template, request, redirect, url_for, session
# from app import app, db
# from app.model import User

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         email = request.form["email"]
#         password = request.form["password"]
#         user = User(email=email, password=password)
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for("login"))

#     return render_template("register.html")

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         email = request.form["email"]
#         password = request.form["password"]
#         user = User.query.filter_by(email=email).first()
#         if user and user.password == password:
#             session["email"] = email
#             return redirect(url_for("dashboard"))

#     return render_template("login.html")

# @app.route("/dashboard")
# def dashboard():
#     email = session.get("email")
#     if email:
#         user = User.query.filter_by(email=email).first()
#         return render_template("dashboard.html", user=user)

#     return redirect(url_for("login"))

# @app.route("/logout")
# def logout():
#     session.pop("email", None)
#     return redirect(url_for("login"))



