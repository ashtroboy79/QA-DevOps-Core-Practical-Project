from urllib import response
from application import app, routes
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestMonsterSpecies(TestBase):
    # @patch('application.routes.choice', return_value= 'Dragon')
    # def test_monster_species1(self, patched):
    #     response = self.client.get(url_for('monster_species'))
    #     self.assert200(response)
    #     self.assertIn(b'Dragon', response.data)

    # @patch('application.routes.choice', return_value= 'Giant')
    # def test_monster_species2(self, patched):
    #     response = self.client.get(url_for('monster_species'))
    #     self.assert200(response)
    #     self.assertIn(b'Giant', response.data)
    @patch('application.routes.choice', side_effect=['Dragon', 'Orc'])
    def test_monster_species(self, patched):
        response = self.client.get(url_for('monster_species'))
        self.assert200(response)
        # print(response.data)
        self.assertIn(b'"monster":"Dragon"', response.data)
        self.assertIn(b'"minions":"Orc"', response.data)
    
    @patch('application.routes.choice', side_effect=['Giant', 'Skeleton'])
    def test_monster_species2(self, patched):
        response = self.client.get(url_for('monster_species'))
        self.assert200(response)
        self.assertIn(b'"monster":"Giant"', response.data)
        self.assertIn(b'"minions":"Skeleton"',response.data)
