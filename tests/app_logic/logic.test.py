from unittest import TestCase
from app_logic.logic import handle_login, handle_register


class LogicTest(TestCase):
    def handle_login_test(self):
        user_with_nonexistent_username = ("mikky", "mikky")
        result = handle_login(*user_with_nonexistent_username)
        self.assertEqual(result[1], "Username does not exist")

        user_with_invalid_password = ('eotobo', '123456')
        result = handle_login(*user_with_invalid_password)
        self.assertEqual(result[1], "Incorrect password")

        existing_user = ("eotobo", "eotobo")
        result = handle_login(*existing_user)
        # No errors in index 1 of the result list
        self.assertEqual(result[1], None)

    def handle_register_test(self):
        user_with_existing_username = ("eotobo", "eotobo")
        result = handle_register(*user_with_existing_username)
        self.assertEqual(result[1], "Username already exists")

        valid_user_registration_credentials = ('mikky', 'mikky')
        result = handle_register(*valid_user_registration_credentials)
        self.assertEqual(result[1], "register successful")