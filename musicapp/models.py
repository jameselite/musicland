from django.db import models
from django.conf import settings


class Track(models.Model):

    title = models.CharField(max_length=220)
    description = models.TextField(max_length=600)
    track = models.FileField(upload_to='tracks/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True, default='image/default.jpg')

    def __str__(self):

        return self.title
    
class Like(models.Model):

    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.track
    
class Comment(models.Model):

    track_object = models.ForeignKey(Track, related_name='comments', on_delete=models.CASCADE, verbose_name='track')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=400)

    def __str__(self):

        return f"{self.author} in {self.track_object.title}"
    
    
class Playlist(models.Model):

    tracks_list = models.ManyToManyField(Track, related_name='playlists')
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)