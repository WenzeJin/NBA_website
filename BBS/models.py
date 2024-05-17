from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True)
    slogan = models.TextField(blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return "User: " + self.user.username + " Nickname: " + self.nickname

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return "Tag: " + self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, default="No Title")
    abstract = models.TextField(max_length=200, blank=True)
    content = RichTextField()
    post_time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self) -> str:
        return "Post: " + self.title + " User: " + self.user.username


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

