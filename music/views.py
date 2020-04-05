from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Song


# def error(request,lol):
#     context = {
#         "error":lol,
#     }
#     return render(request,"music/error.html",context)


def index(request):
    page_title = "Music"
    context = {
        "page_title": page_title,
    }
    return render(request, "music/index.html", context)


def albums(request):
    all_albums = Album.objects.all()
    page_title = "Albums"
    context = {
        'all_albums': all_albums,
        'page_title': page_title,
    }
    return render(request, "music/all_albums.html", context)


def album(request, album_id):
    try:
        a = Album.objects.get(id=album_id)
        songs = a.song_set.all()
        page_title = a.album_title
        context = {
            "page_title": page_title,
            "album": a,
            "songs": songs,
            'a':request,
        }
        return render(request, "music/album_details.html", context)
    except (Album.DoesNotExist):
        page_title = "Error In Album"
        error = "No such Album"
        context = {
            "error":error,
            "page_title":page_title,
        }
        return render(request,"music/error.html",context)


def songs(request):
    a = False
    a = Song.objects.order_by("album__artist").all()
    page_title = "Songs"
    context = {
        "page_title": page_title,
        "songs": a,
    }
    return render(request, "music/songs.html", context)


def song(request, song_id):
    try:
        a = Song.objects.get(id=song_id)
        page_title = a.song_title
        context = {
            "page_title": page_title,
            "song_details": a,
        }
        return render(request,"music/song_details.html",context)
    except (Song.DoesNotExist):
        error = "No Such song"
        context = {
            "page_title": "Error No Song",
            "error":error,
        }
        return render(request,"music/error.html",context)

def artists(request):
    a = Album.objects.order_by('artist').all()
    singers=[]
    for b in a:
        container =  b.artist
        if container in singers:
            continue
        singers.append(container)

    page_title = "Artists"
    context = {
        "page_title":page_title,
        "artists": singers,
    }
    return render(request,"music/artists.html" , context)

def artist(request,artist_name):
    try:
        b = Album.objects.filter(artist=artist_name).first()
        a = Album.objects.filter(artist= artist_name)
        page_title  = b.artist
        context = {
            "page_title":page_title,
            "albums":a,
        }
        return render (request,'music/artist_detail.html',context)
    except (Album.DoesNotExist,AttributeError):
        page_title="Error Artist"
        context = {
            "page_title":page_title,
            "error":"No such artist or does not exist in database!"
        }
        return render(request,"music/error.html",context)

    return False