from django.urls import path
from . import views

urlpatterns = [
    path('songs/<song_id>', views.index, name="index"),
]
