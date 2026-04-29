from django.db import models
from django.db.models import Sum, Count
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, default='Unknown artist')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    duration_seconds = models.PositiveIntegerField(help_text='Duration in seconds')
    is_available = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    @property
    def formatted_duration(self):
        minutes = self.duration_seconds // 60
        seconds = self.duration_seconds % 60
        return f"{minutes}:{seconds:02d}"

    def __str__(self):
        return f"{self.title} by {self.artist}"

class Playlist(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='playlist', null=True)
    songs = models.ManyToManyField(Song, related_name='playlists', blank=True)

    def __str__(self):
        return self.title

    @property
    def total_duration_formatted(self):
        total_seconds = self.songs.aggregate(total=Sum('duration_seconds'))['total'] or 0
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        minutes_copy = minutes
        hours = minutes_copy // 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    @property
    def top_genre(self):
        valid_songs = self.songs.exclude(genre__isnull=True)
        grouped = valid_songs.values('genre__id', 'genre__name')
        counted = grouped.annotate(count=Count('genre'))
        ordered = counted.order_by('-count')
        top_two = list(ordered[:2])

        if not top_two:
            return None
        if len(top_two) == 1:
            return top_two[0]
        if top_two[0]['count'] == top_two[1]['count']:
            return None

        return top_two[0]
