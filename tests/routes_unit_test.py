import unittest
from unittest.mock import MagicMock
import sys
import os
from bottle import run, route, TEMPLATE_PATH, redirect, request, template

from database import db
from app_logic import logic

class TestRoutes(unittest.TestCase):
    def setUp(self):
        # Set up a test Bottle app for each test case
        self.app = app

    def redirect_to_login_page_test(self):
        response = self.app.request("/")

        # Ensure that the response is a redirect to /login
        self.assertEqual(response.status, 302)
        self.assertEqual(response.header['Location'], '/login')

    def show_login_page_test(self):
        response = self.app.request("/login")

        # Ensure that the response contains the login template
        self.assertIn('login', response.body.decode())

    def handle_login_successful_test(self):
        # Mock logic.handle_login to return a successful result
        logic.handle_login = MagicMock(return_value=(True, None, None))

        # Simulate a POST request to /login
        response = self.app.post("/login", data={'username': 'valid_user', 'password': 'valid_password'})

        # Ensure that the response is a redirect to /topic_list
        self.assertEqual(response.status, 302)
        self.assertEqual(response.header['Location'], '/topic_list')

    def handle_login_unsuccessful_test(self):
        # Mock logic.handle_login to return an unsuccessful result
        logic.handle_login = MagicMock(return_value=(False, 'Error message', True))

        # Simulate a POST request to /login
        response = self.app.post("/login", data={'username': 'invalid_user', 'password': 'invalid_password'})

        # Ensure that the response contains the login template with an error message
        self.assertIn('login', response.body.decode())
        self.assertIn('Error message', response.body.decode())

    def show_post_review_test(self):
        response = self.app.request("/post_review")
        # Ensure that the response contains the post_review template
        self.assertIn('post_review', response.body.decode())

    def show_post_topic_test(self):
        response = self.app.request("/post_topic")
        # Ensure that the response contains the post_topic template
        self.assertIn('post_topic', response.body.decode())

    def show_register_test(self):
        response = self.app.request("/register")
        # Ensure that the response contains the register template
        self.assertIn('register', response.body.decode())

    def handle_register_successful_test(self):
        # Mock logic.handle_register to return a successful result
        logic.handle_register = MagicMock(return_value=(True, None, None))

        # Simulate a POST request to /register
        response = self.app.post("/register", data={'username': 'valid_user', 'password': 'valid_password'})

        # Ensure that the response is a redirect to /login
        self.assertEqual(response.status, 302)
        self.assertEqual(response.header['Location'], '/login')

    def handle_register_unsuccessful_test(self):
        # Mock logic.handle_register to return an unsuccessful result
        logic.handle_register = MagicMock(return_value=(False, 'Error message', True))

        # Simulate a POST request to /register
        response = self.app.post("/register", data={'username': 'invalid_user', 'password': 'invalid_password'})

        # Ensure that the response contains the register template with an error message
        self.assertIn('register', response.body.decode())
        self.assertIn('Error message', response.body.decode())

    def show_review_list_test(self):
        response = self.app.request("/review_list")
        # Ensure that the response contains the review_list template
        self.assertIn('review_list', response.body.decode())

    def show_topic_list_test(self):
        response = self.app.request("/topic_list")
        # Ensure that the response contains the topic_list template
        self.assertIn('topic_list', response.body.decode())

    def show_write_review_test(self):
        response = self.app.request("/write_review")
        # Ensure that the response contains the write_review template
        self.assertIn('write_review', response.body.decode())

    def show_write_topic_test(self):
        response = self.app.request("/write_topic")
        # Ensure that the response contains the write_topic template
        self.assertIn('write_topic', response.body.decode())

if __name__ == '__main__':
    unittest.main()
