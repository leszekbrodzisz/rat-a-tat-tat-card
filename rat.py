from flask import (Flask, render_template, abort, jsonify, request, redirect, url_for)
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap
#from babel import Babel

app = Flask(__name__)
#babel = Babel(app)
Bootstrap(app)

app.config['SECRET_KEY'] = 'sekretny_klucz'


class UsersNumber(FlaskForm):
    WTF_I18N_ENABLED = True
    class Meta:
        #locales = ['pl_PL', 'pl']
        #WTF_I18N_ENABLED ustawic na false???

        locales = ['es_ES', 'es']
    how_many_players = IntegerField('Podaj liczbę graczy i naciśnij przycisk pojniżej:', validators=[InputRequired(message='Podanie liczby graczy jest konmiczene')])



@app.route('/', methods=["GET", "POST"])
def welocome():
    form = UsersNumber()
    if form.validate_on_submit():
        return 'jest przycisk'

    return render_template("welcome.html", form=form)

@app.route('/tours_run', methods=["GET", "POST"])
def tours_run():
    if request.method == "POST":
        #something will come here
        a=1


        #return (redirect(url_for('tours_run', players=players, results=results)))
    else:
        return render_template("tours_run.html")