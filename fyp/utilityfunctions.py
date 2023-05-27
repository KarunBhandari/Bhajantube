from music.models import Songs
from random import choice

def genre_recommendations(genre):
    recommended_music = Songs.objects.filter(genre=genre)
    return recommended_music

def suggest_song(*args):
    args = list(args)
    songs = Songs.objects.all().order_by('song_name')
    alogrithm_process = choice(Songs.objects.all())
    if songs != alogrithm_process:
        args.append(alogrithm_process)
        return args
    else:
        return args