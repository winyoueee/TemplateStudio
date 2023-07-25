import pygame
from src import player, library, playlist, settings

current_user = None
current_song = None
current_playlist = None

def update_ui():
    print(f"Current User: {current_user}")
    print(f"Current Song: {current_song}")
    print(f"Current Playlist: {current_playlist}")

def handle_song_changed(song):
    global current_song
    current_song = song
    update_ui()

def handle_playlist_changed(pl):
    global current_playlist
    current_playlist = pl
    update_ui()

def handle_user_changed(user):
    global current_user
    current_user = user
    update_ui()

def main():
    pygame.init()
    player.SONG_CHANGED.connect(handle_song_changed)
    playlist.PLAYLIST_CHANGED.connect(handle_playlist_changed)
    settings.USER_CHANGED.connect(handle_user_changed)

    while True:
        command = input("Enter command: ")
        if command == "quit":
            break
        elif command.startswith("play "):
            song_name = command.split(" ", 1)[1]
            player.play_song(song_name)
        elif command.startswith("load "):
            playlist_name = command.split(" ", 1)[1]
            playlist.load_playlist(playlist_name)
        elif command.startswith("user "):
            user_name = command.split(" ", 1)[1]
            settings.load_settings(user_name)

if __name__ == "__main__":
    main()