from urllib import response
from application import app, routes
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestMonsterSpecies(TestBase):
    @patch('application.routes.choice', side_effect=['Dragon', 'Orcs'])
    def test_monster_species(self, patched):
        response = self.client.get(url_for('monster_species'))
        self.assert200(response)
        self.assertIn(b'"monster":"Dragon"', response.data)
        self.assertIn(b'"minions":"Orcs"', response.data)
    
    @patch('application.routes.choice', side_effect=['Giant', 'Skeletons'])
    def test_monster_species2(self, patched):
        response = self.client.get(url_for('monster_species'))
        self.assert200(response)
        self.assertIn(b'"monster":"Giant"', response.data)
        self.assertIn(b'"minions":"Skeletons"',response.data)
