from django.shortcuts import render
from django.http import HttpResponse
import json
import random

from .models import Songs 

# Create your views here.
def index(request, song_id):
    songs = Songs.objects.all()
    song = songs.filter(song_id=song_id)
    random_num = random.randint(0, len(song))
    song = {"song_name": song[random_num].song_name,"emotion": song[random_num].song_emotion, "url": song[random_num].song_link}
    return HttpResponse(json.dumps(song), content_type="application/json")

