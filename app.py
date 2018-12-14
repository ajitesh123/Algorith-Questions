import datetime
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", headline="Home Page")

@app.route("/<string:name>")
def hello(name):
    return f"Hello, {name}!"

@app.route("/isnewyear")
def isnewyear():
    now=datetime.datetime.now()
    new_year=now.month==1 and now.day==1
    return render_template("isyear.html", new_year=new_year)
