1. Shared Variables:
   - `current_user`: Stores the current user's information.
   - `current_song`: Stores the current song being played.
   - `current_playlist`: Stores the current playlist being played.

2. Data Schemas:
   - `UserSchema`: Defines the structure for user data.
   - `SongSchema`: Defines the structure for song data.
   - `PlaylistSchema`: Defines the structure for playlist data.

3. ID Names of DOM Elements:
   - `player`: The main audio player element.
   - `playlist`: The playlist display element.
   - `library`: The music library display element.
   - `settings`: The settings display element.

4. Message Names:
   - `SONG_CHANGED`: Triggered when the current song changes.
   - `PLAYLIST_CHANGED`: Triggered when the current playlist changes.
   - `USER_CHANGED`: Triggered when the current user changes.

5. Function Names:
   - `play_song()`: Plays a specific song.
   - `stop_song()`: Stops the current song.
   - `load_playlist()`: Loads a specific playlist.
   - `save_playlist()`: Saves the current playlist.
   - `load_library()`: Loads the user's music library.
   - `save_library()`: Saves the user's music library.
   - `update_settings()`: Updates the user's settings.
   - `load_settings()`: Loads the user's settings.

6. Shared Modules:
   - `os`: For interacting with the operating system.
   - `sqlite3`: For interacting with the SQLite database.
   - `pytest`: For running tests.
   - `pygame`: For playing audio files.

7. Shared Database Tables:
   - `users`: Stores user data.
   - `songs`: Stores song data.
   - `playlists`: Stores playlist data.
   - `settings`: Stores user settings data.