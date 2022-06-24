from application import app, routes
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestMonsterSpecies(TestBase):
    @patch('application.routes.choice', return_value= 'Dragon')
    def test_monster_species(self, patched):
        response = self.client.get(url_for('monster_species'))
        self.assert200(response)
        self.assertIn(b'Dragon', response.data)

    @patch('application.routes.choice', return_value= 'Giant')
    def test_monster_species(self, patched):
        response = self.client.get(url_for('monster_species'))
        self.assert200(response)
        self.assertIn(b'Giant', response.data)
