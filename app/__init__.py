from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from app.models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from app.routes import auth_bp, main_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    
    return app


# # import files in the sys
# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # create the database instance
# db = SQLAlchemy(app)

# # create the database tables
# with app.app_context():
#     db.create_all()

# # Import other modules and define routes/views here
# from app import routes


# if __name__ == '__main__':
#     app.run()
