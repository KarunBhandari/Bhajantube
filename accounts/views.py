from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.
from django.urls import reverse
from fyp.utilityfunctions import *
from accounts.forms import EditProfileForm
from accounts.models import Playlist
from music.models import Songs
from django.contrib.auth.forms import UserChangeForm
from .Recommendation import genre_recommendations


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('login')

    
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if username is None:
            messages.info(request, 'Username should be 1-10')
            return render(request, 'register.html')

        else:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')

            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                password=password, email=email)
                user.save()
                messages.info(request, 'registration successful')

                return redirect('login')
    else:
        return render(request, 'register.html')


def homepage(request):
    song = Songs.objects.all().order_by('?')[:20]
    return render(request, 'homepage.html', {'song': song})


@login_required(login_url='login')
def profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)


@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        User_form = EditProfileForm(request.POST, instance=request.user)
        if User_form.is_valid():
            user = User_form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
        else:
            return redirect(reverse('edit_profile'))
            messages.info(request, 'invalid credential')

    else:
        User_form = EditProfileForm(instance=request.user)
        arg = {'form': User_form}
        return render(request, 'edit_profile.html', arg)


def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required(login_url='login')
def Search(request):
    searched_songs = set()
    searchKey = request.POST.get('searchkey').lower()
    print(searchKey)
    for song in Songs.objects.all():
        if (song.song_name and searchKey in song.song_name.lower()):
            searched_songs.add(song)
    return render(request, 'Search.html', {'searched_songs': searched_songs})


@login_required(login_url='login')
def changePasswordForm(request):
    return render(request,'changePassword.html')


@login_required(login_url='login')
def changePassword(request):
    if request.method == 'POST':
        # user = User.objects.get(username=request.user.username)
        user = authenticate(request, username=request.POST['username'], password=request.POST['old-password'])

        if user is not None:
            user.set_password(request.POST['new-password'])
            user.save()
            update_session_auth_hash(request, user)
            # messages.success(request, 'Password successfully updated!')
            return redirect('/',username=user.username)
        messages.error(request,'User authenticatio failed')
        return render(request,'changePassword.html')
    return render(request,'login.html')

@login_required(login_url='login')
def playlist(request):
    if request.method == 'POST':
        song_id = request.POST.get('song_id', None)
        song = get_object_or_404(Songs, id=song_id)
        if Playlist.objects.filter(user=request.user, song=song).exists():
            messages.info(request, 'song already exist in playlist')
            song = Songs.objects.all().order_by('?')[:6]
            return render(request, 'homepage.html', {'song': song})
        Playlist.objects.create(user=request.user, song=song)
        lists = Playlist.objects.filter(user=request.user)
        args = {'lists': lists}

        return render(request, 'playlist.html', args)
    else:
        lists = Playlist.objects.filter(user=request.user)
        args = {'lists': lists}
        return render(request, 'playlist.html', args)


@login_required(login_url='login')
def remove(request):
    fav_id = request.POST.get('fav_id', None)
    fav = Playlist.objects.get(id=fav_id)
    if request.method == 'POST':
        fav.delete()
        lists = Playlist.objects.filter(user=request.user)
        args = {'lists': lists}
        return render(request, 'playlist.html', args)

    else:
        lists = Playlist.objects.filter(user=request.user)
        args = {'lists': lists}
        return render(request, 'playlist.html', args)


def recommendation(request):
    if request.method == 'POST':
        Recm = request.POST['rec']
        if Recm:
            try:
                recom = genre_recommendations(Recm).head()
                if recom is not None:
                    return render(request, 'recommendation.html', {'re': recom, 'songName': Recm})
                else:
                    messages.error(request, 'no recommendation found')
                    return render(request, 'recommendation.html', {'re': [], 'songName': Recm})
            except Exception:
                messages.error(request, 'no recommendation found')
                return render(request, 'recommendation.html', {'re': [], 'songName': Recm})
        else:
            messages.error(request, 'no recommendation found')
            return render(request, 'recommendation.html', {'re': [], 'songName': Recm})
    else:
        messages.error(request, 'no recommendation found')
        return render(request, 'recommendation.html', {'re': [], 'songName': Recm})
