from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
from flask_session  import Session
from datetime import datetime
import os

app = Flask(__name__)
SESSION_TYPE='filesystem'
app.config.from_object(__name__)
Session(app)
app.config['SECRET_KEY'] = 'c1ecc4ba444d91d97d0da200bdde1da7'  #To protect from attacks  python -m secrets  "secrets.token_hex(16)"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://operator:tej1nder@db:3306/Server' ##MariaDB entry
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'   #use Sqlite location for SQLAlchemy
db = SQLAlchemy(app)  ##Instantiate DB, python > from app import db, db.create_all()

# login_manager = LoginManager()
# login_manager.init_app(app)

from website.books.book_views import book_blueprint
from website.know.know_views import know_blueprint
from website.simple_session.session_view import simple_blueprint
from website.efforts.efforts_views import effort_blueprint
from website.home.home_views import home_blueprint
#app.register_blueprint(book_blueprint)
#app.register_blueprint(know_blueprint)
app.register_blueprint(simple_blueprint)
app.register_blueprint(effort_blueprint)
app.register_blueprint(home_blueprint)
