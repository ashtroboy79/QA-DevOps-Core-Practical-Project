from email.mime import application
from urllib import response
from application import app, routes
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestMonsterType(TestBase):
    @patch('application.routes.randint', return_value=1)
    def test_monster_type(self,pathced):
        response = self.client.get(url_for('monster_type'))
        self.assert200(response)
        self.assertIn(b'1', response.data)

    @patch('application.routes.randint', return_value=5)
    def test_monster_type(self,pathced):
        response = self.client.get(url_for('monster_type'))
        self.assert200(response)
        self.assertIn(b'5', response.data)
