import pandas as pd
import numpy as np
import json

# ipl_matches = "content/ipl-matches.csv"
# matches = pd.read_csv(ipl_matches)

matches = pd.read_csv("content/ipl_matches_cleaned.csv")


print(matches.head())

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

def teams_api():
    teams = list(set(list(matches.Team1) + list(matches.Team2)))
    return {
        'teams' : teams
    }

def compareTeamsApi(Team1, Team2):
    total_matches = matches[
        ((matches['Team1'] == Team1) & (matches['Team2'] == Team2)) |
        ((matches['Team1'] == Team2) & (matches['Team2'] == Team1))
    ]

    win_counts = total_matches['WinningTeam'].value_counts()

    matches_won_team1 = win_counts.get(Team1, 0)
    matches_won_team2 = win_counts.get(Team2, 0)

    draws = total_matches.shape[0] - (matches_won_team1 + matches_won_team2)

    result = {
        'total_matches': str(total_matches.shape[0]),
        Team1: str(matches_won_team1),
        Team2: str(matches_won_team2),
        'draws': str(draws)
    }
    return result


def allRecord(team):
    team_df = matches[(matches['Team1'] == team) | (matches['Team2'] == team)].copy()
    mp = team_df.shape[0]
    won = team_df[team_df.WinningTeam == team].shape[0]
    draw = team_df[team_df.WinningTeam.isnull()].shape[0]
    loss = mp - won - draw
    title = team_df[(team_df.match_type == 'Final') & (team_df.WinningTeam == team)].shape[0]
    return {
            'matchesPlayed': mp,
            'won': won,
            'loss': loss,
            'draw': draw,
            'title': title
        }

def teamAPI(team, matches=matches):
    #df = matches[(matches['Team1'] == team) | (matches['Team2'] == team)].copy()
    self_record = allRecord(team)
    TEAMS = teams_api()['teams']
    against = {team2: compareTeamsApi(team, team2) for team2 in TEAMS if team2 != team}
    count = len(against)
    data = {team: {'overall': self_record,
                   'against': against,
                   'against_count': count}}
    return data