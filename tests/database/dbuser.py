from unittest import TestCase
from database.dbuser import create_user, get_logged_in_user, logout_user, login_user
from app_logic.user import User


class DBUser(TestCase):
    user_creation_params = ("user_1", "user_1")
    def handle_create_user(self):
        created_user: User = create_user(*self.user_creation_params)

        # Assert that the username is correct
        self.assertEquals(created_user.username, self.user_creation_params[0])

    def check_logged_in_user(self):
        # Test that the user is logged in
        logged_in_user: User = get_logged_in_user()
        self.assertEquals(logged_in_user.username, self.user_creation_params[0])

    def handle_logout_user(self):
        logout_user()
        result = get_logged_in_user()
        self.assertEquals(result, None)

    def login_user(self):
        login_user(self.user_creation_params[0])
        result: User = get_logged_in_user()
        self.assertEquals(result.username, self.user_creation_params[0])
        self.assertEquals(result.is_logged_in, 1) # 1 maps to Boolean True
