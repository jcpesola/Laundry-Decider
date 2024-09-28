from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Initialize SQLAlchemy object
db = SQLAlchemy()

# #function to manage databse sessions
# def init_db(app):
#     db.init_app(app)