from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
       return render_template("index.html") 
