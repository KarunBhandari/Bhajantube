from django.urls import path
from musicplayer import views



urlpatterns = [
    path('songs', views.songs, name='songs'),
    path('songs/<int:id>', views.songpost, name='songpost')

]