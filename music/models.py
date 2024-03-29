from django.db import models
from django.utils import timezone

def upload_to(instance,filename):
    return f'images/{filename}'.format(filename)

class Songs(models.Model):
    song_name = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255)
    song_genre = models.CharField(max_length=255)
    release_date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to=upload_to, null = True)
    music = models.FileField(upload_to=upload_to, null = True)
    