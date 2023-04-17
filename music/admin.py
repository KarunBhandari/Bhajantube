from django.contrib import admin


# Register your models here.
from music.models import Songs

admin.site.register(Songs)