from urllib import response
from application import app
from flask import url_for
from flask_testing import TestCase
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestMonsterClass(TestBase):
   
    def test_monster_class1(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Dragon', 'type':1}
        )
        self.assert200(response)
        self.assertIn(b'A Black Dragon has attacked the party', response.data)

    def test_monster_class2(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Troll', 'type':2}
        )
        self.assert200(response)
        self.assertIn(b'Ice Troll', response.data)

    def test_monster_class3(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Beholder', 'type':4}
        )
        self.assert200(response)
        self.assertIn(b'Gauth has attacked the party', response.data)

    def test_monster_class4(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Liche', 'type':3}
        )
        self.assert200(response)
        self.assertIn(b'A Demilich has attacked the party roll initiative', response.data)

    def test_monster_class5(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Liche', 'type':1}
        )
        self.assert200(response)
        self.assertIn(b'An Archlich has attacked the party', response.data)

    def test_monster_class6(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Vampire', 'type':4}
        )
        self.assert200(response)
        self.assertIn(b'A Vampire lord has', response.data)
