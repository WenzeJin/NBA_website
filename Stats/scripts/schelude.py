import requests
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.static import teams

from ..models import from_espn_to_nickname
from datetime import date


def address(data):
    str_date = str(data)
    url = str_date.split("-")[0] + str_date.split("-")[1] + str_date.split("-")[2]

    return url


def get_body(url):
    response = requests.get(url)
    response_text = response.text
    body = response_text[response.text.find('<tbody'): response.text.find('/tbody>')]
    return body


def get_data(data):
    data = str(data)

    url = 'https://www.espn.com/nba/schedule/_/date/'
    url += data.split("-")[0] + data.split("-")[1] + data.split("-")[2]

    body = get_body(url)

    find = body.find('<span>')
    helper = 0
    matches = []
    match = []

    while find != -1:
        if helper % 2 == 0 and helper > 0:
            matches.append(match)
            match = []

        team = body[body.find('<span>') + len('<span>'):body.find('</span>')]
        match.append(team)
        body = body[body.find('</span>')+len('</span>'):]
        find = body.find('<span>')

        helper += 1

    matches.append(match)
    result = []

    for match in matches:

        df = {'away': from_espn_to_nickname(match[0]), 'home': from_espn_to_nickname(match[1])}
        result.append(df)

    return result


def feature(data):
    d1 = date.today().strftime("%d/%m/%Y")
    d1 = d1.split("/")[2] + d1.split("/")[1] + d1.split("/")[0]
    print(data)
    print(d1)
    if data >= d1:
        return True
    else:
        return False


def switch_demo(var):
    switcher = {
        "JAN": "01",
        "FEB": "02",
        "MAR": "03",
        "APR": "04",
        "MAY": "05",
        "JUN": "06",
        "JUL": "07",
        "AUG": "08",
        "SEP": "09",
        "OCT": "10",
        "NOV": "11",
        "DEC": "12"
    }
    return switcher.get(var, "Invalid Month")


def get_points(data, nickname):
    team = [team for team in teams.get_teams() if team["nickname"] == nickname][0]

    calendar = teamgamelog.TeamGameLog(team_id=team["id"])
    calendar_df = calendar.get_data_frames()[0]

    for index, row in calendar_df.iterrows():
        day = row['GAME_DATE']
        date_index = day.split(" ")[2] + switch_demo(day.split(" ")[0]) + day.split(" ")[1].split(",")[0]

        if date_index == data:
            return row['PTS']


def get_past_data(data):
    data = str(data)

    url = 'https://www.espn.com/nba/schedule/_/date/'
    data = data.split("-")[0] + data.split("-")[1] + data.split("-")[2]

    url += data

    body = get_body(url)

    find = body.find('<span>')
    helper = 0
    matches = []
    match = []

    while find != -1:
        if helper % 2 == 0 and helper > 0:
            matches.append(match)
            match = []

        team = body[body.find('<span>') + len('<span>'):body.find('</span>')]
        match.append(team)
        body = body[body.find('</span>')+len('</span>'):]
        find = body.find('<span>')

        helper += 1

    matches.append(match)
    result = []
    print(matches)
    for match in matches:
        print(match[0])
        away = from_espn_to_nickname(match[0])
        print(away)
        away_points = get_points(data, away)

        print(match[1])
        home = from_espn_to_nickname(match[1])
        print(home)
        home_points = get_points(data, home)

        if home_points is None or away_points is None:
            home_points = "PPD"
            away_points = "PPD"

        print(str(away_points) + " away home " + str(home_points))

        df = {'away': away, 'home': home, 'points_a': str(away_points), 'points_h': str(home_points)}
        result.append(df)

    return result
