from nba_api.stats.endpoints import leaguestandings


def west_standings():
    standings = leaguestandings.LeagueStandings()
    standings_df = standings.get_data_frames()[0]
    result = []
    df_west = standings_df[standings_df["Conference"] == "West"]
    position = 1
    for index, row in df_west.iterrows():

        if int(row['CurrentStreak']) < 0:
            streak = "L" + str(abs(int(row['CurrentStreak'])))
        else:
            streak = "W" + str(row['CurrentStreak'])
        df = {'position': position, 'name': row['TeamName'], 'wins': row['WINS'], 'losses': row['LOSSES'],
              'winPCT': row['WinPCT'], 'conference': row['ConferenceRecord'], 'division': row['DivisionRecord'],
              'home': row['HOME'], 'road': row['ROAD'], 'L10': row['L10'], 'streak': streak}
        result.append(df)
        position += 1

    return result


def east_standings():
    standings = leaguestandings.LeagueStandings()
    standings_df = standings.get_data_frames()[0]
    result = []
    df_east = standings_df[standings_df["Conference"] == "East"]
    position = 1
    for index, row in df_east.iterrows():

        if int(row['CurrentStreak']) < 0:
            streak = "L" + str(abs(int(row['CurrentStreak'])))
        else:
            streak = "W" + str(row['CurrentStreak'])
        df = {'position': position, 'name': row['TeamName'], 'wins': row['WINS'], 'losses': row['LOSSES'],
              'winPCT': row['WinPCT'], 'conference': row['ConferenceRecord'], 'division': row['DivisionRecord'],
              'home': row['HOME'], 'road': row['ROAD'], 'L10': row['L10'], 'streak': streak}
        result.append(df)
        position += 1

    return result
