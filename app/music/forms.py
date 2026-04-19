from django import forms
from .models import Song, Genre, Playlist


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'genre', 'duration_seconds', 'is_available']

        labels = {
            'title': 'Song Title',
            'artist': 'Artist',
            'genre': 'Genre',
            'duration_seconds': 'Song duration(in seconds)',
            'is_available': 'Availability'
        }

        help_texts = {
            'duration_seconds': '',
        }

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'description']

        labels = {
            'name': 'Genre Name',
            'description': 'Description'
        }

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['title', 'description', 'is_public', 'songs']

        labels = {
            'title': 'Playlist Title',
            'description': 'Description',
            'is_public': 'Make this playlist public?',
            'songs': 'Select songs that will be in the playlist(hold Ctrl / Cmd to select multiple)'
        }