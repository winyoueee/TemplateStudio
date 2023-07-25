import sqlite3
import os

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'database.db')

def load_settings():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM settings WHERE user_id=?", (current_user['id'],))
    settings = cursor.fetchone()
    conn.close()
    return settings

def update_settings(new_settings):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE settings
        SET theme=?, language=?, volume=?
        WHERE user_id=?
    """, (new_settings['theme'], new_settings['language'], new_settings['volume'], current_user['id']))
    conn.commit()
    conn.close()