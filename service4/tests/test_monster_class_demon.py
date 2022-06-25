from urllib import response
from application import app
from flask import url_for
from flask_testing import TestCase
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestMonsterClass(TestBase):
   
    def test_monster_class_demon1(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Demon', 'type':1}
        )
        self.assert200(response)
        self.assertIn(b'A Barlgura has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_demon2(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Demon', 'type':2}
        )
        self.assert200(response)
        self.assertIn(b'A Chasme has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_demon3(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Demon', 'type':3}
        )
        self.assert200(response)
        self.assertIn(b'A Glabrezu has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_demon4(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Demon', 'type':4}
        )
        self.assert200(response)
        self.assertIn(b'A Nalfeshnee has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_demon5(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Demon', 'type':5}
        )
        self.assert200(response)
        self.assertIn(b'A Vrock has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_demon6(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Demon', 'type':6}
        )
        self.assert200(response)
        self.assertIn(b'A Yochlol has attacked the party, roll initiative!!!', response.data)
