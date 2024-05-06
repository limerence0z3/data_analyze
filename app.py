from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, redirect
from db import initDB

app = Flask(__name__)
initDB(app)

@app.route("/")
def index():
    return redirect("rank")

@app.route("/rank")
def rank():
    return render_template("rank.html")
