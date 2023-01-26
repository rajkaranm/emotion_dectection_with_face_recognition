from django.db import models

# Create your models here.
class Songs(models.Model):
    song_id = models.IntegerField()
    song_name = models.CharField(max_length=100)
    song_emotion = models.CharField(max_length=100)
    song_link = models.CharField(max_length=100)

    def __str__(self):
        return self.song_name