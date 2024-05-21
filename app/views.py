from flask import Blueprint, render_template, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    return render_template("homepage.html")

@views.route('/user_input', methods=['GET'])
def user_input():
    return redirect(url_for('views.homepage'))