from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
from django.contrib import auth
from DemotivationFactory import settings

from picasagallery.utils import get_albums, get_photos

def gallery(request):
    albums = get_albums()
    return render(request, 'picasagallery/gallery.html', {'albums': albums})

def album_list(request, album_id):
    for album in get_albums():
        if album.gphoto_id.text == album_id:
            photos = get_photos(album)
            return render(request, 'picasagallery/album.html', {'photos': photos, 'album': album})
    raise Http404()


def album(request):
    print('tut static url' + settings.STATIC_URL )
    album = get_albums()[0]
    if (album):
        photos = get_photos(album)
        return render_to_response('picasagallery/home.html',
                                  {'username': auth.get_user(request).username,'photos': photos, 'album': album})
    raise Http404()