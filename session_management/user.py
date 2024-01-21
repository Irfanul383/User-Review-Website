from typing import List
from app_logic.user import User
import database.dbuser as dbuser


def create_user(username: str, password: str) -> User:
    return dbuser.create_user(username, password)


def login_user(username: str) -> None:
    dbuser.login_user(username)


def get_user_by_username(username: str) -> User or None:
    return dbuser.get_user_by_username(username)


def get_logged_in_user() -> User or None:
    return dbuser.get_logged_in_user()


def get_users() -> List[User] or None:
    return dbuser.get_users()

def logout_user():
    """Logs out the current user.

    """
    dbuser.logout_user()


def is_logged_in(username):
    return (get_user_by_username(username).is_logged_in)
def check_username_exists(username):
    return (get_user_by_username(username) != None)
def match_password(username, password):
    return (get_user_by_username(username).password == password)
