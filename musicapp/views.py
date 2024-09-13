from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404, get_list_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):

    alltracks = Track.objects.all().order_by('-created_at')

    context = {

        'thetrack' : alltracks
    }

    return  render(request, 'index.html', context)

@login_required
def uploadtrack(request):

    if request.method == "POST":
        if request.user.is_authenticated:
            form = Addtrackform(request.POST, request.FILES)
            if form.is_valid():
                new_track = form.save(commit=False)
                new_track.author = request.user
                new_track.save()
                return redirect('track_detail', pk=new_track.pk)
    else:
        form = Addtrackform()
    
    return render(request, 'uploadtrack.html', {'forms' : form})
        

def trackdetail(request, pk):

    track = get_object_or_404(Track, pk=pk)
    if request.user.is_authenticated:
        playlist = get_object_or_404(Playlist, author=request.user)
        tracks_in_playlist = playlist.tracks_list.all()
    else:
        playlist = None
        tracks_in_playlist = []
        
    comments = track.comments.all().order_by('-created_at')
    if request.method == "POST":
        if request.user.is_authenticated:  
            form = Addcomment(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.track_object = track
                new_comment.author = request.user
                new_comment.save()
                return redirect('track_detail', pk=track.pk)
        else:
            return redirect('login')
    else:
        form = Addcomment()

    track_comments_amount = track.comments.count()
    context = {

        'track' : track,
        'form' : form,
        'comments' : comments,
        'comments_count' : track_comments_amount,
        'playlist' : playlist,
        'tracks_in_playlist' : tracks_in_playlist
    }

    return render(request, 'track_detail.html', context)

@login_required
def deletetrack(request, pk):

    item = get_object_or_404(Track, pk=pk)
    
    if request.method == "POST":
        if request.user == item.author:
             form = Deletetrack(request.POST, request.FILES)
             if form.is_valid():
                 item.delete()
                 return redirect("index")
        else:
            return redirect('index')
    else:
        form = Deletetrack()

    return render(request, 'deleteconfirm.html', {'form' : form if request.user == item.author else None})

@login_required
def trackupdate(request, pk):
    
    item = get_object_or_404(Track, pk=pk)
    form = Updatetrack(instance=item)

    if request.method == "POST":
        if request.user == item.author:
             form = Updatetrack(request.POST, request.FILES, instance=item)
             if form.is_valid():
                 item.save()
                 return redirect("track_detail", pk=item.pk)

    return render(request, 'updatetrack.html', {'form' : form if request.user == item.author else None})


def liketrack(request, pk):

    track_item = get_object_or_404(Track, pk=pk)
    ip_address = request.META.get('REMOTE_ADDR')

    if not Like.objects.filter(track = track_item, ip_address=ip_address).exists():
        Like.objects.create(track=track_item, ip_address=ip_address)

    
    return redirect('track_detail', pk=pk)

def search_result(request):

    if request.method == "POST":
        searched = request.POST['searched']
        searched_item = Track.objects.filter(title__contains=searched)
        return render(request, 'search_result.html', {'searched' : searched, 'item' : searched_item})
    else:
        return render(request, 'search_result.html', {})

@login_required
def dashboard(request):

    mytrack = Track.objects.filter(author=request.user)
    
    return render(request, 'dashboard.html', {'mytrack': mytrack})
@login_required

def add_to_playlist(request, pk):

    track = get_object_or_404(Track, pk=pk)
    playlist, created = Playlist.objects.get_or_create(author=request.user)
    playlist.tracks_list.add(track)
    return redirect('playlist')

@login_required
def playlist_view(request):

    playlist = get_object_or_404(Playlist, author=request.user)
    tracks = playlist.tracks_list.all()

    return render(request, 'playlist.html', {'playlist' : playlist, 'tracks' : tracks})

@login_required
def delete_track_playlist(request, pk):

    track = get_object_or_404(Track, pk=pk)
    playlist = get_object_or_404(Playlist, author=request.user)
    playlist.tracks_list.remove(track)
    return redirect('playlist')