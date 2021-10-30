from flask import Blueprint, Flask, redirect, render_template, url_for, session, request

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route("/", methods=['GET', 'POST'])
def know_home():
  return render_template("layout.html", title='Add records')
