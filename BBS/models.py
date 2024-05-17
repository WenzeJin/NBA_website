from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True)
    slogan = models.TextField(blank=True)
    birthday = models.DateField(null=True, blank=True)


def create_user_info(user: User):
    entries = UserInfo.objects.filter(user=user)
    if len(entries) == 1:
        for entry in entries:
            entry.delete()
    entry = UserInfo.objects.create(user=user, nickname=user.username)
    entry.save()


def create_user_info_condition(user: User):
    entries = UserInfo.objects.filter(user=user)
    print(entries)
    if len(entries) == 0:
        entry = UserInfo.objects.create(user=user, nickname=user.username)
        entry.save()