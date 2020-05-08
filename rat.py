from flask import (Flask, render_template, abort, jsonify, request, redirect, url_for)


app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template(
        "welcome.html", text1 = "Wstawiony text")
