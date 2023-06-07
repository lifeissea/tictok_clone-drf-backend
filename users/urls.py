from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("@<str:username>", views.PublicUser.as_view()),
    path("<str:username>/likes", views.Likes.as_view()),
    path("<str:username>/follow", views.Follow.as_view()),
    path("<str:username>/unfollow", views.Unfollow.as_view()),
    path("<str:username>/following", views.Following.as_view()),
    path("<str:username>/followers", views.Followers.as_view()),
]
