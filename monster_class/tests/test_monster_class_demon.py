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
            json = {'monster':'Demon', 'type':1, "minions":"Goblins", "quantity":1}
        )
        self.assert200(response)
        self.assertIn(b'A Barlgura has attacked the party, roll initiative!!!', response.data)
        self.assertIn(b'3 Goblins accompany it', response.data)

    def test_monster_class_demon2(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Demon', 'type':2, "minions":"Goblins", "quantity":2}
        )
        self.assert200(response)
        self.assertIn(b'A Chasme has attacked the party, roll initiative!!!', response.data)
        self.assertIn(b'5 Goblins accompany it', response.data)

    def test_monster_class_demon3(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Demon', 'type':3, "minions":"Goblins", "quantity":3}
        )
        self.assert200(response)
        self.assertIn(b'A Glabrezu has attacked the party, roll initiative!!!', response.data)
        self.assertIn(b'8 Goblins accompany it', response.data)

    def test_monster_class_demon4(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Demon', 'type':4, "minions":"Gnolls", "quantity":1}
        )
        self.assert200(response)
        self.assertIn(b'A Nalfeshnee has attacked the party, roll initiative!!!', response.data)
        self.assertIn(b'2 Gnolls accompany it', response.data)

    def test_monster_class_demon5(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Demon', 'type':5, "minions":"Gnolls", "quantity":2}
        )
        self.assert200(response)
        self.assertIn(b'A Vrock has attacked the party, roll initiative!!!', response.data)
        self.assertIn(b'3 Gnolls accompany it', response.data)

    def test_monster_class_demon6(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Demon', 'type':6, "minions":"Gnolls", "quantity":3}
        )
        self.assert200(response)
        self.assertIn(b'A Yochlol has attacked the party, roll initiative!!!', response.data)
        self.assertIn(b'4 Gnolls accompany it', response.data)
