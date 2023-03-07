from django.shortcuts import render,HttpResponse
from musicplayer.models import Songs

# Create your views here.
def index(request):
    song= Songs.objects.all()
    return render(request,'index.html',{'song':song})

def songs(request):
    song= Songs.objects.all()
    return render(request,'songs.html',{'song':song})


def songpost(request,id):
    song= Songs.objects.filter(song_id=id).first()
    return render(request,'songpost.html',{'song':song})

