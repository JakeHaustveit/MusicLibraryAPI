from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.from django.db import models

# Create your views here.
class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_date = models.DateField()
    likes= models.IntegerField(+1)
