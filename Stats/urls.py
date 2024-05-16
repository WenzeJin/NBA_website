from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('standings/', views.standings_view, name='standings'),
    path('schedule/', views.schedule_view, name='schedule'),
    path('teams/', views.teams_view, name='teams'),
    path('west/', views.west_view, name='west'),
    path('east/', views.east_view, name='east'),
    path('team/', views.team_view, name='team'),
    path('roster/', views.roster_view, name='roster'),
    path('played/', views.games_played_view, name='played'),
    path('player/', views.player_view, name='player'),
    path('matches/', views.matches_view, name='matches'),
    path('leagueleaders/', views.league_leaders_view, name='league_leaders'),
    path('playerseasons/', views.player_seasons_view, name='player_seasons'),
]
