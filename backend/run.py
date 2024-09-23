import os, sys

from flask import Flask
from app.database import db #import database setup
from app.routes.main_routes import main_bp as main_blueprint #Import the blueprint from the routes

#create and configure flask app here
def create_app():
    app = Flask(__name__)

    #Database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/Laundry_Decider'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #Initialize SQLAlchemy in app
    db.init_app(app)

    #Register Blueprints/routes
    app.register_blueprint(main_blueprint)

    return app

app = create_app()

if __name__ == "__main__":
      app.run(debug=True)

#Entry point to run the app