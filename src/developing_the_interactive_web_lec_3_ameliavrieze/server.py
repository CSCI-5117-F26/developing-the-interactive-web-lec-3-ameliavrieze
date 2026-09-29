from flask import Flask, redirect, request, render_template

app = Flask(__name__)
names = []

@app.route("/", methods=["GET"])
def guest_book():
    global names
    return render_template("guestbook.html", names=names)

@app.route("/add", methods=["POST"])
def add():
    global names
    name=request.form.get("name")
    if request.form.get("name"):
        names.append(name)
    return render_template("guestbook.html", names=names)

    