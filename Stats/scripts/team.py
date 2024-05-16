from nba_api.stats.endpoints import teamplayerdashboard
from nba_api.stats.endpoints import teamgamelog, teamdetails
from nba_api.stats.static import teams


def details(nickname):
    team = [team for team in teams.get_teams() if team["nickname"] == nickname][0]

    team_details = teamdetails.TeamDetails(team_id=team["id"])
    team_details_df = team_details.get_data_frames()[0]

    for index, row in team_details_df.iterrows():
        df = {'name': team['full_name'], 'coach': row['HEADCOACH'], 'manager': row['GENERALMANAGER'],
              'owner': row['OWNER'], 'arena': row['ARENA']}
        return df


def get_roster(nickname):
    team = [team for team in teams.get_teams() if team["nickname"] == nickname][0]

    roster = teamplayerdashboard.TeamPlayerDashboard(team_id=team["id"])
    roster_df = roster.get_data_frames()[1]

    roster_df["PPG"] = round(roster_df["PTS"] / roster_df["GP"], 1)
    roster_df["RPG"] = round(roster_df["REB"] / roster_df["GP"], 1)
    roster_df["APG"] = round(roster_df["AST"] / roster_df["GP"], 1)
    roster_df["SPG"] = round(roster_df["STL"] / roster_df["GP"], 1)
    roster_df["BPG"] = round(roster_df["BLK"] / roster_df["GP"], 1)
    roster_df["MPG"] = round(roster_df["MIN"] / roster_df["GP"], 1)

    result = []
    for index, row in roster_df.iterrows():
        df = {'name': row['PLAYER_NAME'], 'PPG': row['PPG'], 'RPG': row['RPG'],
              'APG': row['APG'], 'FG_PCT': row['FG_PCT'], 'FG3_PCT': row['FG3_PCT'],
              'FT_PCT': row['FT_PCT'], 'SPG': row['SPG'], 'BPG': row['BPG'], 'MPG': row['MPG']}
        result.append(df)

    return sorted(result, key=lambda k: k['name'])


def games_played(nickname):
    team = [team for team in teams.get_teams() if team["nickname"] == nickname][0]

    calendar = teamgamelog.TeamGameLog(team_id=team["id"])
    calendar_df = calendar.get_data_frames()[0]
    result = []

    for index, row in calendar_df.iterrows():
        opponent = row['MATCHUP']
        opponent_team = [team for team in teams.get_teams() if team["abbreviation"] == opponent.split(" ")[2]][0]
        record = str(row["W"]) + "-" + str(row["L"])
        df = {'date': row['GAME_DATE'], 'opponent': opponent_team["nickname"], 'wl': row['WL'],
              'record': record, 'FG_PCT': row['FG_PCT'], 'FG3_PCT': row['FG3_PCT'],
              'FT_PCT': row['FT_PCT'], 'PTS': row['PTS'], 'REB': row['REB'], 'AST': row['AST']}
        result.append(df)

    return result


def get_id(nickname):
    team = [team for team in teams.get_teams() if team["nickname"] == nickname][0]

    return team["id"]
