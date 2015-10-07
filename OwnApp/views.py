__author__ = 'Work'

from OwnApp import app
from flask import render_template

@app.route('/')
def hello_world():
    return render_template("base.html")

@app.route("/about/")
def about():
    return render_template("about.html")