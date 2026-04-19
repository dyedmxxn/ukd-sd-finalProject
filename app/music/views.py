from django.shortcuts import render, get_object_or_404, redirect
from .models import Song, Genre, Playlist
from .forms import SongForm, GenreForm, PlaylistForm

#========= Song =========

#Song: Read All
def song_list_view(request):
    songs = Song.objects.all()

    context = {
        'title': 'All songs',
        'songs': songs,
    }

    return render(request, 'music/song_list.html', context)

#Song: Read One
def song_detail_view(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    context = {
        'title': f'{song.title} by {song.artist}',
        'song': song,
    }

    return render(request, 'music/song_detailed.html', context)

#Song: Create
def song_create_view(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()

    context = {
        'title': 'Add new song',
        'form': form,
    }

    return render(request, 'music/song_form.html', context)

#Song: Update
def song_update_view(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_detail', song_id=song.id)
    else:
        form = SongForm(instance=song)

    context = {
        'title': f'Modify: {song.title}',
        'form': form,
    }

    return render(request, 'music/song_form.html', context)

#Song: Delete
def song_delete_view(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    if request.method == 'POST':
        song.delete()
        return redirect('song_list')

    context = {
        'title': f'Delete song {song.title}?',
        'song': song,
    }

    return render(request, 'music/song_confirm_delete.html', context)

#========= Genre =========

#Genre: Read All
def genre_list_view(request):
    genres = Genre.objects.all()

    context = {
        'title': 'All Genres',
        'genres': genres,
    }

    return render(request, 'music/genre_list.html', context)

#Genre: Read One
def genre_detail_view(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)

    context = {
        'title': f'{genre.name}',
        'genre': genre,
    }

    return render(request, 'music/genre_detailed.html', context)

#Genre: Create
def genre_create_view(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm()

    context = {
        'title': 'Add new genre',
        'form': form,
    }

    return render(request, 'music/genre_form.html', context)

#Genre: Update
def genre_update_view(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)

    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genre_detail', genre_id=genre.id)
    else:
        form = GenreForm(instance=genre)

    context = {
        'title': f'Modify: {genre.name}',
        'form': form,
    }

    return render(request, 'music/genre_form.html', context)

#Genre: Delete
def genre_delete_view(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)

    if request.method == 'POST':
        genre.delete()
        return redirect('genre_list')

    context = {
        'title': f'Delete genre {genre.name}?',
        'genre': genre,
    }

    return render(request, 'music/genre_confirm_delete.html', context)

#Genre: All songs in a specific genre
def genre_songs_view(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)

    songs = Song.objects.filter(genre=genre)

    context = {
        'title': f'All songs in {genre.name} genre:',
        'genre': genre,
        'songs': songs,
    }

    return render(request, 'music/genre_songs.html', context)

#========= Playlist =========

#Playlist: Read All
def playlist_list_view(request):
    playlists = Playlist.objects.all()

    context = {
        'title': 'All playlists',
        'playlists': playlists,
    }

    return render(request, 'music/playlist_list.html', context)

#Playlist: Read One
def playlist_detail_view(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)

    context = {
        'title': f'{playlist.title}',
        'playlist': playlist,
    }

    return render(request, 'music/playlist_detailed.html', context)

#Playlist: Create
def playlist_create_view(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('playlist_list')
    else:
        form = PlaylistForm()

    context = {
        'title': 'Add new playlist',
        'form': form,
    }

    return render(request, 'music/playlist_form.html', context)

#Playlist: Update
def playlist_update_view(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)

    if request.method == 'POST':
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            form.save()
            return redirect('playlist_detail', playlist_id=playlist.id)
    else:
        form = PlaylistForm(instance=playlist)

    context = {
        'title': f'Modify: {playlist.title}',
        'form': form,
    }

    return render(request, 'music/playlist_form.html', context)

#Playlist: Delete
def playlist_delete_view(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)

    if request.method == 'POST':
        playlist.delete()
        return redirect('playlist_list')

    context = {
        'title': f'Delete playlist "{playlist.title}"?',
        'playlist': playlist,
    }

    return render(request, 'music/playlist_confirm_delete.html', context)
