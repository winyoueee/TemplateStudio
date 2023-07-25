import os
import sqlite3
from player import Player
from library import Library
from user_interface import UserInterface
from settings import Settings
from database import Database

def main():
    # Initialize database
    db = Database(sqlite3.connect('music_library.db'))

    # Initialize settings
    settings = Settings(db)

    # Load settings
    settings.load_settings()

    # Initialize library
    library = Library(db)

    # Load library
    library.load_library()

    # Initialize player
    player = Player(pygame.mixer)

    # Initialize user interface
    ui = UserInterface(player, library, settings)

    # Start user interface
    ui.start()

if __name__ == "__main__":
    main()