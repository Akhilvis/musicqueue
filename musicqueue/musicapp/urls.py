from django.contrib import admin
from django.urls import path, include
from musicapp import urls as appurls
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('add', add_youtube_music, name="add_youtube_music"),

]