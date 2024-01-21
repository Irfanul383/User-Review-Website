import sqlite3
import os


# Set up db connection
db_name = "team_d.db"

# Remove db file, if exists
# db_file_path = os.path.join(os.getcwd(), db_name)
# if os.path.exists(db_file_path):
#     os.remove(db_file_path)

# Connect to db
db_connection = sqlite3.connect(db_name)
db = db_connection.cursor()


# Decorator function that automatically closes db connection
def use_db(func):
    def open_and_close_db_connection(*args):
        func(*args)
        db_connection.commit()

    return open_and_close_db_connection


# Function to set up and populate database with data
@use_db
def setup():
    # Create user table
    db.execute(
        '''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                is_logged_in INTEGER NOT NULL
            )
        '''
    )
    # Populate the users table with data
    users = [
        ("eotobo", "eotobo", 0),
        ("afarhad", "afarhad", 0),
        ("ihaque", "ihaque", 0),
        ("agraab", "agraab", 0),
        ("faraz", "faraz", 0)
    ]
    db.executemany('INSERT INTO users VALUES (?, ?, ?)', users)

    # Create review table
    db.execute(
        '''
            CREATE TABLE IF NOT EXISTS reviews (
                topic TEXT NOT NULL,
                content TEXT NOT NULL,
                category TEXT NOT NULL,
                is_anonymous INTEGER NOT NULL,
                is_draft INTEGER NOT NULL,
                username TEXT
            )
        '''
    )
