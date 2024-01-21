import sqlite3
import os

# Set up db connection
db_name = "team_d.db"

# Remove db file, if exists
# db_file_path = os.path.join(os.getcwd(), db_name)
# if os.path.exists(db_file_path):
#os.remove(db_file_path)

# Connect to db
db_connection = sqlite3.connect(db_name)
db = db_connection.cursor()


# Decorator function that automatically closes db connection
def use_db(func):
    def open_and_close_db_connection(*args):
        result = func(*args)
        db_connection.commit()
        return result

    return open_and_close_db_connection


# Function to set up and populate database with data
@use_db
def setup():
    # Create user table
    db.execute(
        '''
            CREATE TABLE IF NOT EXISTS user (
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                is_logged_in INTEGER NOT NULL
            )
        '''
    )
    # Populate the users table with data
    users = [
        ["eotobo", "eotobo", 0],
        ["afarhad", "afarhad", 0],
        ["ihaque", "ihaque", 0],
        ["agraab", "agraab", 0],
        ["faraz", "faraz", 0]
    ]
    db.executemany('INSERT INTO user VALUES (?, ?, ?)', users)

    # Create review table
        # TODO: The category attribute would need to be filled out later
    db.execute(
        '''
            CREATE TABLE IF NOT EXISTS review (
                topic_id TEXT NOT NULL,
                creator_id INT NOT NULL,
                content TEXT NOT NULL,
                topic_answers TEXT,
                category TEXT,
                is_anonymous INTEGER,
                is_draft INTEGER,
                is_text_based INTEGER
            )
        '''
    )

    # Create topic table
    db.execute(
        '''
            CREATE TABLE IF NOT EXISTS topic (
                creator_id INT NOT NULL,
                title TEXT NOT NULL
            )
        '''
    )

    # Populate the topics table with data
    topics = [
        [1, "Topic 1"],
        [2, "Topic 2"],
        [3, "Topic 3"],
        [4, "Topic 4"],
        [5, "Topic 5"],
    ]
    db.executemany("INSERT INTO topic VALUES (?, ?)", topics)

    # Create topic questions
    db.execute(
        '''
            CREATE TABLE IF NOT EXISTS topic_question (
                question TEXT NOT NULL,
                topic_id INT NOT NULL
            )
        '''
    )
