from nba_api.stats.static import teams


def all_teams():
    result = []
    for row in teams.get_teams():
        df = {'full_name': row['full_name'], 'nickname': row['nickname'], 'city': row['city'],
              'state': row['state'], 'year_founded': row['year_founded']}
        result.append(df)

    return result

