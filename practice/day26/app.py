from flask import Flask, render_template, request, redirect, url_for
import os
from analyzer import analyze

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.route("/")
def home():
    techs = ["HTML", "CSS", "Flask", "Python"]
    name = "30 Days of Python Progamming"
    return render_template("home.html", techs = techs, name = name, title = "Home")

@app.route("/about")
def about():
    name = "30 Days of Python Programming"
    return render_template("about.html", name = name, title = "About")

@app.route("/result")
def result():
    content = request.args["content"]
    words, characters, frequency = analyze(content)
    return render_template("result.html", words = words, characters = characters, frequency = frequency)

@app.route("/post", methods = ["GET", "POST"])
def post():
    name = "Text Analyzer"
    if request.method == "GET":
        return render_template("post.html", name = name, title = name)
    if request.method == "POST":
        content = request.form["content"]
        return redirect(url_for("result", content = content))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug = True, host = "0.0.0.0", port = port)