from flask import render_template, request, jsonify
from . import create_app

app = create_app()

@app.route('/')
def homepage():
    return render_template('homepage.html')
