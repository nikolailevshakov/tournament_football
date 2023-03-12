from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/health", methods=["GET"])
def health():
    return "OK"


@app.route("/results")
def results():
    return render_template('results.html')


@app.route("/season")
def season():
    return render_template('season.html')
