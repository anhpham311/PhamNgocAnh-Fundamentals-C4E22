import os
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to C4E web module - enjoy!!"

@app.route("/quan")
def Hello_quan():
    return "Hello quan"

@app.route("/praise/annie")
def praise_linh():
    return "Annie is awesome"

@app.route("/praise/<name>")
def praise(name):
    return name + " is awesome"


@app.route("/add/<int:x>/<int:y>")
def add(x,y):
    s = x + y
    return str(s) #html chi co loai la string

@app.route("/question")
def show_question():
    return render_template("question.html")

@app.route("/about-me")
def about_me():
    return render_template("about_me.html")

@app.route("/school")
def school():
    return redirect("https://techkids.vn/khoa-hoc-lap-trinh/code-for-everyone")

if __name__ == "__main__": #set up server
    app.run(debug=True)

