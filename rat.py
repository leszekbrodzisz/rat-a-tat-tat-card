from flask import (Flask, render_template, abort, jsonify, request, redirect, url_for)


players = {
  "player1": "P1",
  "player2": "P2",
  "player3": "P3",
  "player4": "P4",
}

results = {
  "player1": 0,
  "player2": 0,
  "player3": 0,
  "player4": 0,
}

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def velcome():
    if request.method == "POST":
        #something will come here
        players["player1"] = request.form["form_p1_name"]
        players["player2"] = request.form["form_p2_name"]
        players["player3"] = request.form["form_p3_name"]
        players["player4"] = request.form["form_p4_name"]

        return (redirect(url_for('tours_run', players=players, results=results)))
    else:
        return render_template("welcome.html", text1 = "Wstawiony text RRRRR")

@app.route('/tours_run', methods=["GET", "POST"])
def tours_run():
    if request.method == "POST":
        #something will come here
        results["player1"] = 1

        #return (redirect(url_for('tours_run', players=players, results=results)))
    else:
        return render_template("tours_run.html", players = players, results = results )