from django.db import models
from django.contrib.auth.models import User
from music.models import Songs


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    song = models.ForeignKey(Songs, on_delete=models.CASCADE, )


    def __str__(playlist):
        return playlist.user

# Create your models here.