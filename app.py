import os

from flask import Flask
from api.tasks import tasks
from api.auth import auth_bp

from extensions import db, jwt
from models.tasks import Tasks
from models.users import Users

def create_app(db_url=None):

    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")
    #returns SQL debuging - queries in the server logs
    app.config['SQLALCHEMY_ECHO'] = os.getenv("FLASK_SQLALCHEMY_ECHO") 
    # Set the secret key for JWT
    app.config['JWT_SECRET_KEY'] = os.getenv("FLASK_JWT_SECRET_KEY")
    #register blueprints
    app.register_blueprint(tasks)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    #initialize extensions
    db.init_app(app) 
    jwt.init_app(app)

    
    # Run setup code during app creation
    with app.app_context():
        db.create_all() # Create tables during app initialization
    
    # @app.before_request # this runs every time i make a request not only the first time
    # def create_table():
    #     db.create_all()

    return app 