from django.urls import path
from .views import *


urlpatterns = [
    path('home/',MusicHomeView.as_view(),name='homepage'),
    path('addsongs/',AddSongsView.as_view(),name='addsongs'),
    path('privsongs/',PrivateSongView.as_view(),name='privsongs'),
    path('sharedsongs/',SharedSongView.as_view(),name='sharedsongs'),
]