import datetime

from django.db import models


class Teams(models.Model):
    nba_id = models.CharField(max_length=11)
    full_name = models.CharField(max_length=25)
    espn_name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.full_name


class DatePicker(models.Model):
    date = models.DateField(default=datetime.datetime.now)


def from_espn_to_nickname(espn):
    teams = Teams.objects.filter(espn_name=espn)
    for team in teams:
        return team.nickname
