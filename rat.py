from flask import (Flask, render_template, abort, jsonify, request, redirect, url_for, session)
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired
from wtforms.validators import NumberRange
from wtforms.validators import Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)

app.config['SECRET_KEY'] = 'sekretny_klucz'

# deklarujemy zmienne do programu zmienne
TourCount = 1

#PlayersResults = {}
#PlayersResults.update({'GRACZ 1 ': 0})
#PlayersResults.update({'GRACZ 2 ': 0})

class UsersNumber(FlaskForm):

    #how_many_players = IntegerField('Podaj liczbę graczy i naciśnij przycisk:', validators=[InputRequired(message='Podanie liczby graczy jest konmiczene')])
    how_many_players = IntegerField('Podaj liczbę graczy:',
                                    validators=[InputRequired(message='Podanie liczby graczy jest konmiczene')
                                                , NumberRange(min=2, max=10, message='Dozwolona liczba graczy od %(min) do %(max)')
                                                ]
                                    )

class Players(FlaskForm):
    PL = StringField('Nazwa Gracza',
                                    validators=[InputRequired(message='Podanie nazwy gracza jest konieczne')
                                                 , Length(min=2, max=21, message = '2 liczba liter od %(min)a do %(max)d AAA')
                                                 ]
                                    )


@app.route('/', methods=["GET", "POST"])
def welocome():
    #session.clear()
    session.permanent = True
    form = UsersNumber()
    if 'PlayersNumber' not in session:
        session['PlayersNumber'] = 0
    if 'PlayersResults' not in session:
        session['PlayersResults'] = {}
        #session['PlayersResults'].update({'GRACZ 1 ': 0})
    if form.validate_on_submit():
        session['PlayersNumber'] = form.how_many_players.data
        return redirect(url_for('add_players'))

    return render_template("welcome.html", form=form, PlayersResults=session['PlayersResults']
                           , TextToDisplay = 'sesja PLnr: ' + str(session['PlayersNumber']) + ' sesja PLres: ' + str(session['PlayersResults']) + ' all_user_agent: '+ str(request.user_agent) + ' browser:' + str(request.user_agent.browser) + ' ver:' + str(request.user_agent.version) + ' platform:' + str(request.user_agent.platform))

@app.route('/tours_run', methods=["GET", "POST"])
def tours_run():
    if request.method == "POST":
        #something will come here
        a=1


        #return (redirect(url_for('tours_run', players=players, results=results)))
    else:
        return render_template("tours_run.html")

@app.route('/add_players/', methods=["GET", "POST"])
def add_players():
    form = Players()
    if form.validate_on_submit():
        session['PlayersResults'].update({form.PL.data: 0})
        if len(session['PlayersResults']) == session['PlayersNumber']:
            return 'skończylismy podawanię graczy'
        #return 'przycisk z podania nazw graczy ' + str(form.PL.data) + ' ww ' + str(PlayersResults) + ' mamy zawodnikow:' + str(len(PlayersResults))
        return render_template("players_names.html"
                               , form=form
                               , PlayersNumber=session['PlayersNumber']
                               , PlayerAddingCount=len(session['PlayersResults'])
                               , PlayerAddingCount_and_1 =len(session['PlayersResults'])+1
                               , PlayersResults=session['PlayersResults']
                               )
    return render_template("players_names.html"
                           , form=form
                           , PlayersNumber=session['PlayersNumber']
                           , PlayerAddingCount=len(session['PlayersResults'])
                           , PlayerAddingCount_and_1 =len(session['PlayersResults'])+1
                           , PlayersResults=session['PlayersResults']
                           )