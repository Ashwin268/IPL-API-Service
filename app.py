from flask import Flask, jsonify,request
import ipl

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>WELCOME TO IPL API SERVICE</h1>'

@app.route('/api/teams')
def teams():
    all_teams = ipl.teams_api()
    return jsonify(all_teams)

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