from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.new_entry, name="create"),
    path("<str:title>", views.entry, name="entry"),
]
