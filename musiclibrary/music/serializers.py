from re import S
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [ 'id', 'title', 'artist', 'album', 'release-date' ]