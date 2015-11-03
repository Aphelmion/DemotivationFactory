from django.conf.urls import patterns, include, url

urlpatterns = [

     url(r'^', 'mainApp.views.home', name='home' ),

]