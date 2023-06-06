from django.urls import path, include
from . import views



urlpatterns = [
    path("",views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("@<str:username>", views.PublicUser.as_view()),
    path("<str:username>/likes", views.Likes.as_view()),
]