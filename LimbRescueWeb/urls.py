from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("about/", views.about, name="about"),
    path("index/", views.index),
    path("login/", views.login),
    path("register/", views.register),
    path("logout/", views.logout),
    path("about/", views.about),
    path(
        "uploadppg/", TemplateView.as_view(template_name="../templates/ppg.html"), name="uploadppg"
    ),
    path("saved/", views.SavePPG, name="savedppg"),
    path("admin/", admin.site.urls),
]
