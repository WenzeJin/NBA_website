from nba_api.stats.endpoints import commonplayerinfo, playerdashboardbyyearoveryear
from nba_api.stats.static import players, teams


def player_info(name):
    player = [player for player in players.get_active_players() if player["full_name"] == name][0]

    player_data = commonplayerinfo.CommonPlayerInfo(player_id=player["id"])
    player_info_df = player_data.get_data_frames()[0]
    print(player_info_df[['BIRTHDATE', 'SCHOOL', 'COUNTRY', 'POSITION', 'HEIGHT', 'WEIGHT', 'DRAFT_YEAR',
                          'DRAFT_NUMBER', 'TEAM_NAME', 'SEASON_EXP']])
    p = player_info_df.iloc[0]['BIRTHDATE']
    # print(p.split("T")[0])

    for index, row in player_info_df.iterrows():
        df = {'name': name, 'birthdate': player_info_df.iloc[0]['BIRTHDATE'].split("T")[0], 'school': row['SCHOOL'],
              'country': row['COUNTRY'], 'position': row['POSITION'], 'height': row['HEIGHT'], 'weight': row['WEIGHT'],
              'draft_year': row['DRAFT_YEAR'], 'draft_number': row['DRAFT_NUMBER'], 'team': row['TEAM_NAME'],
              'experience': row['SEASON_EXP']}
        return df

def player_info_all(name):
    player = [player for player in players.get_players() if player["full_name"] == name][0]

    player_data = commonplayerinfo.CommonPlayerInfo(player_id=player["id"])
    player_info_df = player_data.get_data_frames()[0]
    print(player_info_df[['BIRTHDATE', 'SCHOOL', 'COUNTRY', 'POSITION', 'HEIGHT', 'WEIGHT', 'DRAFT_YEAR',
                          'DRAFT_NUMBER', 'TEAM_NAME', 'SEASON_EXP']])
    p = player_info_df.iloc[0]['BIRTHDATE']
    # print(p.split("T")[0])

    for index, row in player_info_df.iterrows():
        df = {'name': name, 'birthdate': player_info_df.iloc[0]['BIRTHDATE'].split("T")[0], 'school': row['SCHOOL'],
              'country': row['COUNTRY'], 'position': row['POSITION'], 'height': row['HEIGHT'], 'weight': row['WEIGHT'],
              'draft_year': row['DRAFT_YEAR'], 'draft_number': row['DRAFT_NUMBER'], 'team': row['TEAM_NAME'],
              'experience': row['SEASON_EXP']}
        return df

def player_seasons(name):
    player = [player for player in players.get_active_players() if player["full_name"] == name][0]

    player = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(player_id=player["id"])
    player_df = player.get_data_frames()[1]

    player_df["PPG"] = round(player_df["PTS"] / player_df["GP"], 1)
    player_df["APG"] = round(player_df["AST"] / player_df["GP"], 1)
    player_df["RPG"] = round(player_df["REB"] / player_df["GP"], 1)
    player_df["MPG"] = round(player_df["MIN"] / player_df["GP"], 1)
    player_df["SPG"] = round(player_df["STL"] / player_df["GP"], 1)
    player_df["BPG"] = round(player_df["BLK"] / player_df["GP"], 1)
    player_df["FGMPG"] = round(player_df["FGM"] / player_df["GP"], 1)
    player_df["FGAPG"] = round(player_df["FGA"] / player_df["GP"], 1)
    player_df["FG3MPG"] = round(player_df["FG3M"] / player_df["GP"], 1)
    player_df["FG3APG"] = round(player_df["FG3A"] / player_df["GP"], 1)
    player_df["FTMPG"] = round(player_df["FTM"] / player_df["GP"], 1)
    player_df["FTAPG"] = round(player_df["FTA"] / player_df["GP"], 1)
    player_df["ORPG"] = round(player_df["OREB"] / player_df["GP"], 1)
    player_df["DRPG"] = round(player_df["DREB"] / player_df["GP"], 1)
    player_df["TOVPG"] = round(player_df["TOV"] / player_df["GP"], 1)
    player_df["PFPG"] = round(player_df["PF"] / player_df["GP"], 1)
    player_df["PMPG"] = round(player_df["PLUS_MINUS"] / player_df["GP"], 1)

    result = []

    for index, row in player_df.iterrows():
        try:
            team = [team for team in teams.get_teams() if team["abbreviation"] == row['TEAM_ABBREVIATION']][0][
                "nickname"]
        except IndexError:
            team = "-"

        df = {'season': row['GROUP_VALUE'], 'team': team, 'GP': row['GP'], 'MPG': row['MPG'],
              'PPG': row['PPG'],
              'FGMPG': row['FGMPG'], 'FGAPG': row['FGAPG'], 'FG_PCT': row['FG_PCT'], 'FG3MPG': row['FG3MPG'],
              'FG3APG': row['FG3APG'], 'FG3_PCT': row['FG3_PCT'], 'FTMPG': row['FTMPG'], 'FTAPG': row['FTAPG'],
              'FT_PCT': row['FT_PCT'], 'ORPG': row['ORPG'], 'DRPG': row['DRPG'], 'RPG': row['RPG'], 'APG': row['APG'],
              'TOVPG': row['TOVPG'], 'SPG': row['SPG'], 'BPG': row['BPG'], 'PFPG': row['PFPG'], 'PMPG': row['PMPG']}
        result.append(df)

    return result


def get_id(name):
    player = [player for player in players.get_active_players() if player["full_name"] == name][0]

    return player["id"]


def get_id_all(name):
    player = [player for player in players.get_players() if player["full_name"] == name][0]
