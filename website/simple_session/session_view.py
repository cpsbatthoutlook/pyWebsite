from website import app
from flask import Flask, Blueprint, request, url_for, redirect, render_template
from flask_session import Session

simple_blueprint = Blueprint('simple', __name__)

@simple_blueprint.route("/", methods=['GET', 'POST'])
def simple_home():    
    return render_template('layout.html', title="Hi", simple_message="Welcome to this page" )

