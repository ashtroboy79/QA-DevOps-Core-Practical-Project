from urllib import response
from application import app, routes
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestMonsterType(TestBase):
    @patch('application.routes.randint', side_effect=[1,3])
    def test_monster_type1(self,pathced):
        response = self.client.get(url_for('monster_type'))
        self.assert200(response)
        self.assertIn(b'"type":1', response.data)
        self.assertIn(b'"quantity":3', response.data)

    @patch('application.routes.randint', side_effect=[5,6])
    def test_monster_type2(self,pathced):
        response = self.client.get(url_for('monster_type'))
        self.assert200(response)
        self.assertIn(b'"type":5', response.data)
        self.assertIn(b'"quantity":6', response.data)
