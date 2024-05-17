from django.shortcuts import render
from .scripts import standings, team, teams, player, schelude, leagueLeaders
from .forms import DatePickerForm
from BBS.models import *

def index(request):
    logged_in = request.user.is_authenticated
    user_info = None
    if logged_in:
        logged_in = True
        create_user_info_condition(request.user)
        user_info = UserInfo.objects.filter(user=request.user)
        user_info = user_info[0]
    else:
        logged_in = False

    return render(
        request,
        'index.html',
        {
            'title': 'Home page',
            'nickname': user_info.nickname if logged_in else '',
        }
    )


def standings_view(request):
    return render(
        request,
        'standings.html',
        {
            'title': 'Standings',
        }
    )


def schedule_view(request):
    date = ""

    if request.method == 'POST':
        form = DatePickerForm(request.POST)
        if form.is_valid():
            date = schelude.address(form.cleaned_data['date'])
            feature = schelude.feature(date)
            print(feature)

            if feature:
                print("FEATURE!!!!!!!!!!!!!!!")
                return render(
                    request,
                    'matches.html',
                    {
                        'title': 'Matches',
                        'day': str(form.cleaned_data['date']),
                        'date': date,
                        'matches': schelude.get_data(form.cleaned_data['date']),
                    }
                )
            else:
                print("PAST!!!!!!!!!!!!!!!")
                return render(
                    request,
                    'past.html',
                    {
                        'title': 'Matches',
                        'day': str(form.cleaned_data['date']),
                        'date': date,
                        'matches': schelude.get_past_data(form.cleaned_data['date']),
                    }
                )
        else:
            print("BibleThump")

    form = DatePickerForm

    return render(
        request,
        'schedule.html',
        {
            'title': 'Schedule',
            'form': form,
            'date': date,
        }
    )


def teams_view(request):
    return render(
        request,
        'teams.html',
        {
            'title': 'Teams',
            'teams': teams.all_teams(),
        }
    )


def west_view(request):
    return render(
        request,
        'west.html',
        {
            'title': 'West',
            'standings': standings.west_standings(),
        }
    )


def east_view(request):
    return render(
        request,
        'east.html',
        {
            'title': 'East',
            'standings': standings.east_standings(),
        }
    )


def team_view(request):
    team_name = request.GET.get('team')
    url = "https://cdn.nba.com/logos/nba/"
    team_id = team.get_id(team_name)
    url += str(team_id)
    url += "/global/L/logo.svg"

    return render(
        request,
        'team.html',
        {
            'team': team_name,
            'details': team.details(team_name),
            'photo': url,
        }
    )


def roster_view(request):
    team_name = request.GET.get('team')

    return render(
        request,
        'roster.html',
        {
            'team': team_name,
            'roster': team.get_roster(team_name),
        }
    )


def games_played_view(request):
    team_name = request.GET.get('team')

    return render(
        request,
        'games_played.html',
        {
            'team': team_name,
            'games': team.games_played(team_name),
        }
    )


def player_view(request):
    player_name = request.GET.get('player')
    url = "https://cdn.nba.com/headshots/nba/latest/1040x760/"
    player_id = player.get_id(player_name)
    url += str(player_id)
    url += ".png"

    return render(
        request,
        'player.html',
        {
            'player': player.player_info(player_name),
            'photo': url,
        }
    )


def matches_view(request):
    date = request.GET.get('date')

    return render(
        request,
        'matches.html',
        {
            'date': date
        }
    )


def league_leaders_view(request):
    print('league_leaders_view')
    leaders = leagueLeaders.league_leaders()
    print(f'leaders: {leaders}')
    return render(
        request,
        'league_leaders.html',
        {
            'leaders': leaders,
        }
    )


def player_seasons_view(request):
    player_name = request.GET.get('player')

    return render(
        request,
        'player_seasons.html',
        {
            'player': player_name,
            'seasons': player.player_seasons(player_name),
        }
    )
