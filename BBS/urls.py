from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('reg/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('prof/', views.user_profile, name='profile'),
    path('profedit/', views.edit_profile, name='profile-edit'),
    path('post/detail/<int:post_id>/', views.post_detail, name='post-detail'),
    path('post/edit/<int:post_id>/', views.post_edit, name='post-edit'),
    path('posts/user/<str:username>', views.user_posts, name='user-posts'),
    path('post/tag/<str:tag_name>/', views.tag_posts, name='tag-posts'),
    path('tags/', views.tags_index, name='tags'),
    path('post/create/', views.post_create, name='post-create'),
    path('post/delete/<int:post_id>/', views.post_delete, name='post-delete'),
    path('ratings/', views.ratings_index, name='ratings'),
    path('rating/create/<str:player>/', views.rating_create, name='rating-create'),
    path('ratings/player/<str:player>/', views.ratings_by_player, name='ratings-by-player'),
    path('ratings/user/<str:username>/', views.ratings_by_user, name='ratings-by-user'),
    path('rating/delete/<int:rating_id>/', views.rating_delete, name='rating-delete'),
]