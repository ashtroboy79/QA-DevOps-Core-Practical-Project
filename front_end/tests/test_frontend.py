from urllib import response
from application import app
from flask_testing import TestCase
from flask import url_for
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

class TestFront(TestBase):
    def test_front_end(self):
        with requests_mock.Mocker() as mock:
            
            mock.get('http://service2:5000/monster_species', json = {"monster" : 'Dragon', "minions": "Dire Wolves" } )
            mock.get('http://service3:5000/monster_type', json = { "type": 1 , 'quantity': 3} )
            mock.get('https://www.dnd5eapi.co/api/monsters/dire-wolf/', json = { "hit_points": 37 })
            mock.post('http://service4:5000/monster_class', text = "A Black Dragon has attacked the party, roll initiative!!!\n 6 Dire Wolves accompany it")
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'A Black Dragon has attacked the party, roll initiative!!!', response.data)
            self.assertIn(b'6 Dire Wolves accompany it',response.data)
            self.assertIn(b'dire-wolf', response.data)
            self.assertIn(b'37', response.data)
