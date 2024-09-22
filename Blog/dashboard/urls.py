from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("blog/", views.blog, name="blog"),
    path("comment/", views.comment, name="comment"),
    


]
