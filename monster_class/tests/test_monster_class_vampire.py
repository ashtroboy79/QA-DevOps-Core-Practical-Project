from urllib import response
from application import app
from flask import url_for
from flask_testing import TestCase
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestMonsterClass(TestBase):
   
    def test_monster_class_vampire1(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Vampire', 'type':1}
        )
        self.assert200(response)
        self.assertIn(b'A Corpse Vampire has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_vampire2(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Vampire', 'type':2}
        )
        self.assert200(response)
        self.assertIn(b'An Eastern Vampire has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_vampire3(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Vampire', 'type':3}
        )
        self.assert200(response)
        self.assertIn(b'A Spirit Vampire has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_vampire4(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Vampire', 'type':4}
        )
        self.assert200(response)
        self.assertIn(b'A Vampire lord has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_vampire5(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Vampire', 'type':5}
        )
        self.assert200(response)
        self.assertIn(b'A Vampire muse has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_vampire6(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Vampire', 'type':6}
        )
        self.assert200(response)
        self.assertIn(b'A Vampire spawn has attacked the party, roll initiative!!!', response.data)
