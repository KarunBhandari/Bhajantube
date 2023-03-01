from django.shortcuts import render,HttpResponse
from musicplayer.models import Songs

# Create your views here.
def index(request):
    song= Songs.objects.all()
    return render(request,'index.html',{'song':song})