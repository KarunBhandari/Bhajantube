from django.shortcuts import render, HttpResponse
from musicplayer.models import Songs
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.


def index(request):
    song = Songs.objects.all()
    return render(request, 'index.html', {'song': song})


def songs(request):
    song = Songs.objects.all()
    return render(request, 'songs.html', {'song': song})


def songpost(request, id):
    song = Songs.objects.filter(song_id=id).first()
    return render(request, 'songpost.html', {'song': song})


def login(request):
    if request.method == "POST":
      username=request.POST['username']
      password=request.POST['pass']
     
      user= authenticate(Username=username, Password=password)
      login(request,user)
      redirect("/")
    return render(request,'login.html')

def signup(request):
     if request.method=="POST":
      username=request.POST['username']
      pass1=request.POST['pass1']
      pass2=request.POST['pass2']

      myuser=User.objects.create_user(username,pass1)
      myuser.save()
      user= authenticate(Username=username, Password=pass1)
      login(request,user)

      return redirect('/')
     return render(request,'signup.html')