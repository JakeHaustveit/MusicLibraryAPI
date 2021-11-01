from django.urls import path
from django.urls.conf import include, include
from . import views

urlpaptterns = [
    path('music/', views.SongList.as_view()),
    path('', include('music.urls')),
]