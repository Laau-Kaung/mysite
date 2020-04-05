from django.urls import path
from . import views
from .models import Album

app_name = "music"

urlpatterns = [
        #music/
        path('',views.index,name="music"),
        # music/album
        path('album/',views.albums,name="album"),
        #music/album/1
        path('album/<int:album_id>',views.album,name="album_detail"),
        #music/song
        path('song/',views.songs,name="song"),
        #music/song/1
        path('song/<int:song_id>',views.song,name="song_detail"),
        #artist/
        path('artist/',views.artists,name="artist"),
        #artist/1
        path('artist/<str:artist_name>',views.artist,name="artist_detail"),
]
