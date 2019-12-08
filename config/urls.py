"""
ioi URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from ioi.game.views import home, login_view, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("social-auth/", include("social_django.urls", namespace="social")),
    url(r"^$", home, name="home"),
]
