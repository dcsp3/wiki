from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random", views.random_entry, name="random"),
    path("search", views.search, name="search"),
    path("create", views.new_entry, name="create"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),
]
