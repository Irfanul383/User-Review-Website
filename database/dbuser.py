from database.db import use_db, db
from typing import List
from app_logic.user import User


@use_db
def create_user(username: str, password: str) -> User:
    """Creates a user in the database

    :param username:
    :param password:
    :return: User model
    """
    user_with_username = get_user_by_username(username)
    user_exists = user_with_username is not None
    if user_exists:
        raise Exception("User exists with username")

    params = (username, password, 0)
    new_user = db.execute("INSERT INTO user VALUES (?, ?, ?)", params)
    new_user_id = new_user.lastrowid

    return User(new_user_id, username, password, is_logged_in=0)


@use_db
def login_user(username: str) -> None:
    """
    :param username: Username of existing user that would be logged in
    """
    (
        db
        .execute("UPDATE user SET is_logged_in = ? WHERE is_logged_in = ?", (0, 1))
        .execute("UPDATE user SET is_logged_in = ? WHERE username = ?", (1, username))
    )

@use_db
def get_logged_in_user() -> User or None:
    user = db.execute("SELECT rowid, * FROM user WHERE is_logged_in = ?", (1, )).fetchone()
    if user is None:
        return None
    return User(user[0], user[1], user[2], user[3])

@use_db
def get_user_by_username(username: str):
    """Returns a user object from the database

    :param username:
    :return: User model
    """
    param = (username,)
    user_in_db = db.execute("SELECT rowid, * FROM user WHERE username=?", param).fetchone()
    if user_in_db is None:
        return None

    user = User(user_in_db[0], user_in_db[1], user_in_db[2], user_in_db[3])
    return user

@use_db
def get_users() -> List[User] or None:
    users = db.execute("SELECT rowid, * FROM user").fetchall()
    return users

@use_db
def logout_user():
    """Logs out the current user.

    """
    db.execute("UPDATE user SET is_logged_in = ? WHERE is_logged_in = ?", (0, 1))