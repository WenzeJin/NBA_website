"""
views.py
Description: Views related to BBS
Author: Wenze Jin
Date: 2024/05/14
"""

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.db import models


# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            create_user_info(user)
            return HttpResponse('Registration successful')
        else:
            return HttpResponse('Form was invalid')
    else:
        form = UserCreationForm()
    return render(request, 'BBS/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            create_user_info_condition(user)
            messages.success(request, 'You are now logged in.')
            return redirect('BBS:index')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect("BBS:login")
    else:
        form = UserLoginForm()
        return render(request, 'BBS/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'You are now logged out!')
    return redirect("BBS:index")


def fill_post_info(post):
    post.user_info = get_object_or_404(UserInfo, user=post.user)
    post.my_tags = post.tags.all()
    return post


def fill_rate_info(rate):
    rate.user_info = get_object_or_404(UserInfo, user=rate.user)
    return rate


def fill_posts_info(posts):
    return [fill_post_info(post) for post in posts]


def fill_rates_info(rates):
    return [fill_rate_info(rate) for rate in rates]


def index(request):
    posts = Post.objects.all()
    posts = posts.order_by('-post_time')
    posts = fill_posts_info(posts)
    logged_in = request.user.is_authenticated
    user_info = None
    if logged_in:
        logged_in = True
        create_user_info_condition(request.user)
        user_info = UserInfo.objects.filter(user=request.user)
        user_info = user_info[0]
    else:
        logged_in = False
    return render(request, 'BBS/index.html', {'nickname': user_info.nickname if logged_in else "", "posts": posts})


def user_profile(request):
    logged_in = request.user.is_authenticated
    user_info = None
    if logged_in:
        logged_in = True
        create_user_info_condition(request.user)
        user_info = UserInfo.objects.filter(user=request.user)
        user_info = user_info[0]
    else:
        logged_in = False
    return render(request, 'BBS/profile.html', {'logged_in': logged_in, 'user_info': user_info})


def edit_profile(request):
    logged_in = request.user.is_authenticated
    user_info = None
    if logged_in:
        logged_in = True
        create_user_info_condition(request.user)
        user_info = UserInfo.objects.filter(user=request.user)
        user_info = user_info[0]
        form = UserInfoForm(instance=user_info)
    else:
        logged_in = False
        form = UserInfoForm()
    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile saved successfully.')
            return redirect('BBS:profile')
        else:
            messages.error(request, 'Form was invalid')
            return redirect('BBS:profile-edit')
    else:
        return render(request, 'BBS/profile_edit.html', {'logged_in': logged_in, 'user_info': user_info, 'form': form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_owner = post.user
    user: User = request.user
    user_own = False

    if post is None:
        messages.error(request, f'Post with id: {post_id} not found!')
        return redirect('BBS:index')

    if user.is_authenticated and user == post_owner:
        # user authentication failed
        user_own = True

    post = fill_post_info(post)
    return render(request, 'BBS/post_detail.html', {'post': post, 'user_own': user_own})


def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_owner = post.user
    user: User = request.user

    if post is None:
        messages.error(request, f'Post with id: {post_id} not found!')
        return redirect('BBS:index')

    if not user.is_authenticated or user != post_owner:
        # user authentication failed
        messages.error(request, 'You are not allowed to edit this post.')
        return redirect('BBS:index')

    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully.')
            return redirect('BBS:post-detail', post_id)
        else:
            messages.error(request, 'Form was invalid, please check.')
            return redirect('BBS:post-edit', post_id)
    else:
        form = PostEditForm(instance=post)
        return render(request, 'BBS/post_edit.html', {'form': form, 'post': post})


def post_create(request):
    user: User = request.user
    if not user.is_authenticated:
        messages.error(request, 'You should log in first.')
        return redirect('BBS:login')

    if request.method == 'POST':
        post = Post.objects.create(user=user)
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post created successfully.')
            return redirect('BBS:user-posts', user.username)
        else:
            messages.error(request, 'Form was invalid, please check.')
            return redirect('BBS:post-create')
    else:
        form = PostEditForm()
        return render(request, 'BBS/post_create.html', {'form': form})


def post_delete(request, post_id):
    post: Post = get_object_or_404(Post, pk=post_id)
    post_owner = post.user
    user: User = request.user

    if not user.is_authenticated or post_owner != user:
        messages.error(request, 'You are not allowed to delete this post.')
        return redirect('BBS:index') if user.is_authenticated else redirect('BBS:login')

    post.delete()
    messages.success(request, f'Post {post_id} deleted successfully.')
    return redirect('BBS:user-posts', user.username)


def user_posts(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserInfo, user=user)
    posts = Post.objects.filter(user=user)
    posts = posts.order_by('-post_time')
    posts = fill_posts_info(posts)

    return render(request,
                  'BBS/user_posts.html', {'profile': profile, 'posts': posts, 'owner': user, })


def tag_posts(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.all()
    posts.order_by('-post_time')
    posts = fill_posts_info(posts)

    filtered = []
    for post in posts:
        if tag in post.my_tags:
            filtered.append(post)

    return render(request,
                  'BBS/tag_posts.html', {'tag': tag, 'posts': filtered})


def ratings_index(request):
    rates = Rate.objects.all()
    rates = rates.order_by('-rate_time')
    rates = fill_rates_info(rates)
    return render(request, 'BBS/ratings.html', {"rates": rates})


def rating_create(request, player):
    user: User = request.user
    if not user.is_authenticated:
        messages.error(request, 'You should log in first.')
        return redirect('BBS:login')

    if request.method == 'POST':
        rate = Rate.objects.create(user=user, player=player)
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rating created successfully.')
            return redirect('BBS:ratings')
        else:
            messages.error(request, 'Rating value was invalid (0-5), please check.')
            return redirect('BBS:rating-create')
    else:
        form = RateForm()
        return render(request, 'BBS/rating_create.html', {'form': form, 'player': player})


def ratings_by_player(request, player):
    rates = Rate.objects.filter(player=player)
    rates = rates.order_by('-rate_time')
    rates = fill_rates_info(rates)

    empty = len(rates) == 0

    return render(request, 'BBS/player_ratings.html', {"rates": rates, "empty": empty, "player": player})


def ratings_by_user(request, username):
    user = get_object_or_404(User, username=username)
    rates = Rate.objects.filter(user=user)
    rates = rates.order_by('-rate_time')

    empty = len(rates) == 0

    user_prof = get_object_or_404(UserInfo, user=user)
    return render(request, 'BBS/user_ratings.html', {'rates': rates, 'empty': empty, 'user_prof': user_prof})


def rating_delete(request, rating_id):
    rate: Rate = get_object_or_404(Rate, pk=rating_id)
    rate_owner = rate.user
    user: User = request.user

    if not user.is_authenticated or rate_owner != user:
        messages.error(request, 'You are not allowed to delete this post.')
        return redirect('BBS:index') if user.is_authenticated else redirect('BBS:login')

    rate.delete()
    messages.success(request, f'Post {rating_id} deleted successfully.')
    return redirect('BBS:ratings-by-user', user.username)


def tags_index(request):
    tags = Tag.objects.all()
    tags = tags.order_by('name')
    return render(request, 'BBS/tags_index.html', {'tags': tags})
