from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Songs(models.Model):
 name= models.CharField(max_length=2000)
 song_id= models.AutoField(primary_key=True)
 name= models.CharField(max_length=2000)
 singer= models.CharField(max_length=2000)
 tags= models.CharField(max_length=100)
 image= models.ImageField(upload_to='documents')
 song= models.FileField(upload_to='documents')



 def __str__(self):
    return self.name 