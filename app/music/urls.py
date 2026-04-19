from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.song_list_view, name='song_list'),
    path('song/<int:song_id>/', views.song_detail_view, name='song_detail'),
    path('song/create/', views.song_create_view, name='song_create'),
    path('song/<int:song_id>/update/', views.song_update_view, name='song_update'),
    path('song/<int:song_id>/delete/', views.song_delete_view, name='song_delete'),

    path('genres/', views.genre_list_view, name='genre_list'),
    path('genre/<int:genre_id>/', views.genre_detail_view, name='genre_detail'),
    path('genre/create/', views.genre_create_view, name='genre_create'),
    path('genre/<int:genre_id>/update/', views.genre_update_view, name='genre_update'),
    path('genre/<int:genre_id>/delete/', views.genre_delete_view, name='genre_delete'),
    path('genre/<int:genre_id>/songs/', views.genre_songs_view, name='genre_songs'),

    path('playlists/', views.playlist_list_view, name='playlist_list'),
    path('playlist/<int:playlist_id>/', views.playlist_detail_view, name='playlist_detail'),
    path('playlist/create/', views.playlist_create_view, name='playlist_create'),
    path('playlist/<int:playlist_id>/update/', views.playlist_update_view, name='playlist_update'),
    path('playlist/<int:playlist_id>/delete/', views.playlist_delete_view, name='playlist_delete'),
]