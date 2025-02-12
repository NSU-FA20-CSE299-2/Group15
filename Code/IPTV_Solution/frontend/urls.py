from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path("iptv/", views.iptv, name="iptv"),
    path("register/", views.registerPage, name='register'),
    path("login/", views.loginPage, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    path("movies/", views.vod, name='vod'),
]