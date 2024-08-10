from flask import Flask, render_template
from flask import request
from pymongo import MongoClient

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/instructions")
def instructions():
    return render_template("instructions.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)