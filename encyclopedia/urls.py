from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random", views.random_entry, name="random"),
    path("create", views.new_entry, name="create"),
    path("<str:title>", views.entry, name="entry"),
]
