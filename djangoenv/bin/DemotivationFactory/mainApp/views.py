from django.shortcuts import render_to_response
from django.contrib import auth
# Create your views here.

def main_view(request):
    print "at m_v"
    return render_to_response('main.html', {'username': auth.get_user(request).username})
