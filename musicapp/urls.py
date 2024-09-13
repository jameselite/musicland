from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name='index'),
    path('upload/', views.uploadtrack, name='uploadtrack'),
    path('tracks/<int:pk>', views.trackdetail, name='track_detail'),
    path('tracks/<int:pk>/delete', views.deletetrack, name='deletetrack'),
    path('tracks/<int:pk>/update', views.trackupdate, name='trackupdate'),
    path('tracks/<int:pk>/like', views.liketrack, name='liketrack'),
    path('search_result', views.search_result, name='search_result'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add-to-playlist/<int:pk>/', views.add_to_playlist, name='add_to_playlist'),
    path('remove-from-playlist/<int:pk>/', views.delete_track_playlist, name='remove_from_playlist'),
    path('playlist', views.playlist_view, name='playlist'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)