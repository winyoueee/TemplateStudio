```python
import os
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('music_library.db')
    return conn

def close_db_connection(conn):
    conn.close()

def execute_query(query):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    close_db_connection(conn)

def fetch_query_results(query):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    close_db_connection(conn)
    return results

def get_song_path(song_id):
    query = f"SELECT path FROM songs WHERE id = {song_id}"
    results = fetch_query_results(query)
    if results:
        return results[0][0]
    else:
        return None

def get_playlist_songs(playlist_id):
    query = f"SELECT song_id FROM playlists WHERE id = {playlist_id}"
    results = fetch_query_results(query)
    if results:
        return [result[0] for result in results]
    else:
        return []

def get_user_playlists(user_id):
    query = f"SELECT id FROM playlists WHERE user_id = {user_id}"
    results = fetch_query_results(query)
    if results:
        return [result[0] for result in results]
    else:
        return []

def get_user_settings(user_id):
    query = f"SELECT * FROM settings WHERE user_id = {user_id}"
    results = fetch_query_results(query)
    if results:
        return results[0]
    else:
        return None

def update_user_settings(user_id, settings):
    query = f"UPDATE settings SET volume = {settings['volume']}, theme = '{settings['theme']}' WHERE user_id = {user_id}"
    execute_query(query)
```