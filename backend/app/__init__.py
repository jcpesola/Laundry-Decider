from flask import Flask
from .database import db #import database setup

#create and configure flask app here
def create_app():
    app = Flask(__name__)

    #Database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/Laundry_Decider'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #Initialize SQLAlchemy in app
    db.init_app(app)

    #Import and register Blueprints/routes
    #from .routes import main
    #app.register_blueprint(main)

    return app