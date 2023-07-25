import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a database in RAM
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        email text NOT NULL UNIQUE
                                    ); """

    sql_create_songs_table = """CREATE TABLE IF NOT EXISTS songs (
                                    id integer PRIMARY KEY,
                                    title text NOT NULL,
                                    artist text NOT NULL,
                                    album text,
                                    genre text,
                                    length text NOT NULL,
                                    user_id integer NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES users (id)
                                );"""

    sql_create_playlists_table = """CREATE TABLE IF NOT EXISTS playlists (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        user_id integer NOT NULL,
                                        FOREIGN KEY (user_id) REFERENCES users (id)
                                    );"""

    sql_create_settings_table = """CREATE TABLE IF NOT EXISTS settings (
                                        id integer PRIMARY KEY,
                                        user_id integer NOT NULL,
                                        theme text NOT NULL,
                                        volume integer NOT NULL,
                                        FOREIGN KEY (user_id) REFERENCES users (id)
                                    );"""

    conn = create_connection()

    if conn is not None:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_songs_table)
        create_table(conn, sql_create_playlists_table)
        create_table(conn, sql_create_settings_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()