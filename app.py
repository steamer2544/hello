from flask import Flask, render_template, request
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app) # turn on session

@app.route("/")
def index():
    return render_template("index.html")