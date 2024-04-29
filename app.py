from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("rank")

@app.route("/rank")
def rank():
    return render_template("rank.html")