from nba_api.stats.endpoints import leagueleaders


def league_leaders():
    leaders = leagueleaders.LeagueLeaders()
    leaders_df = leaders.get_data_frames()[0]

    leaders_df["PPG"] = round(leaders_df["PTS"] / leaders_df["GP"], 1)
    leaders_df["APG"] = round(leaders_df["AST"] / leaders_df["GP"], 1)
    leaders_df["RPG"] = round(leaders_df["REB"] / leaders_df["GP"], 1)
    leaders_df["MPG"] = round(leaders_df["MIN"] / leaders_df["GP"], 1)
    leaders_df["FGMPG"] = round(leaders_df["FGM"] / leaders_df["GP"], 1)
    leaders_df["FGAPG"] = round(leaders_df["FGA"] / leaders_df["GP"], 1)
    leaders_df["FG3MPG"] = round(leaders_df["FG3M"] / leaders_df["GP"], 1)
    leaders_df["FG3APG"] = round(leaders_df["FG3A"] / leaders_df["GP"], 1)
    leaders_df["FTMPG"] = round(leaders_df["FTM"] / leaders_df["GP"], 1)
    leaders_df["FTAPG"] = round(leaders_df["FTA"] / leaders_df["GP"], 1)
    leaders_df["ORPG"] = round(leaders_df["OREB"] / leaders_df["GP"], 1)
    leaders_df["DRPG"] = round(leaders_df["DREB"] / leaders_df["GP"], 1)
    leaders_df["TOVPG"] = round(leaders_df["TOV"] / leaders_df["GP"], 1)
    leaders_df["PFPG"] = round(leaders_df["PF"] / leaders_df["GP"], 1)
    leaders_df["SPG"] = round(leaders_df["STL"] / leaders_df["GP"], 1)
    leaders_df["BPG"] = round(leaders_df["BLK"] / leaders_df["GP"], 1)

    result = []
    for index, row in leaders_df.iterrows():
        df = {'name': row['PLAYER'], 'PPG': row['PPG'], 'RPG': row['RPG'], 'APG': row['APG'], 'FG_PCT': row['FG_PCT'],
              'FG3_PCT': row['FG3_PCT'], 'FGMPG': row['FGMPG'], 'FGAPG': row['FGAPG'], 'FG3MPG': row['FG3MPG'],
              'FT_PCT': row['FT_PCT'], 'MPG': row['MPG'], 'FTMPG': row['FTMPG'], 'FTAPG': row['FTAPG'],
              'ORPG': row['ORPG'], 'DRPG': row['DRPG'], 'TOVPG': row['TOVPG'], 'PFPG': row['PFPG'], 'PER': row['RANK'],
              'SPG': row['SPG'], 'BPG': row['BPG']}
        result.append(df)

    return result
