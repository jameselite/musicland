from django.contrib import admin
from .models import *

class Track_admin(admin.ModelAdmin):

    list_display = ('title', 'author', 'created_at')

class Comment_admin(admin.ModelAdmin):

    list_display = ('track_object', 'author', 'created_at', 'text')

class Playlist_admin(admin.ModelAdmin):

    list_display = ('author',)

admin.site.register(Track, Track_admin)
admin.site.register(Comment, Comment_admin)
admin.site.register(Playlist, Playlist_admin)