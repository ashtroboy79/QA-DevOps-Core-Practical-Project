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
            mock.get('http://service2:5000/monster_species', text = 'Dragon')
            mock.get('http://service3:5000/monster_type', json = { "type": 1 } )
            mock.post('http://service4:5000/monster_class', text = "A Black Dragon has attacked the party, roll initiative!!!")
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'A Black Dragon has attacked the party, roll initiative!!!', response.data)
