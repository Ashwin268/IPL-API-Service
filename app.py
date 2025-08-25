from flask import Flask, jsonify,request
import ipl

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/api/teams')
def teams():
    teams = ipl.teams_api()
    return jsonify(teams)

@app.route('/api/compareTeams')
def compareTeams():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    return jsonify(ipl.compareTeamsApi(team1, team2))

@app.route('/api/teamRecords')
def teamRecords():
    team = request.args.get('team')
    return ipl.teamAPI(team)


app.run(debug=True)