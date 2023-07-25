```python
import sqlite3
from src.song import SongSchema

class PlaylistSchema:
    def __init__(self):
        self.connection = sqlite3.connect('src/database.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS playlists (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        self.connection.commit()

    def add_playlist(self, name, user_id):
        self.cursor.execute("""
            INSERT INTO playlists (name, user_id) VALUES (?, ?)
        """, (name, user_id))
        self.connection.commit()

    def get_playlists(self, user_id):
        self.cursor.execute("""
            SELECT * FROM playlists WHERE user_id = ?
        """, (user_id,))
        return self.cursor.fetchall()

    def delete_playlist(self, id):
        self.cursor.execute("""
            DELETE FROM playlists WHERE id = ?
        """, (id,))
        self.connection.commit()

class Playlist:
    def __init__(self, id, name, user_id):
        self.id = id
        self.name = name
        self.user_id = user_id
        self.songs = []
        self.song_schema = SongSchema()

    def add_song(self, song_id):
        song = self.song_schema.get_song(song_id)
        if song:
            self.songs.append(song)

    def remove_song(self, song_id):
        self.songs = [song for song in self.songs if song.id != song_id]

    def get_songs(self):
        return self.songs

    def clear_songs(self):
        self.songs = []
```
