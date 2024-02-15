from flask import Flask, render_template, url_for, redirect, flash

app = Flask(__name__)


@app.route('/', methods=["GET"])
def root():
    flash("test")
    return redirect(url_for("base"))


@app.route('/home', methods=["GET"])
def home():
    return render_template("home.html")


@app.route('/login', methods=["GET", "POST"])
def base():
    return render_template("auth.html")


app.run(host='127.0.0.1', port=80, debug=True)
