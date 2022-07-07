from urllib import response
from application import app
from flask import url_for
from flask_testing import TestCase
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestMonsterClass(TestBase):
   
    def test_monster_class_beholder1(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Beholder', 'type':1, "minions":"Orcs", "quantity":1}
        )
        self.assert200(response)
        self.assertIn(b'A Death tyrant has attacked the party, roll initiative!!!', response.data)
        self.assertIn(b'3 Orcs accompany it', response.data)

    def test_monster_class_beholder2(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Beholder', 'type':2, "minions":"Orcs", "quantity":2}
        )
        self.assert200(response)
        self.assertIn(b'A Spectator has attacked the party, roll initiative!!!', response.data)
        self.assertIn(b'4 Orcs accompany it', response.data)

    def test_monster_class_beholder3(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Beholder', 'type':3, "minions":"Orcs", "quantity":3}
        )
        self.assert200(response)
        self.assertIn(b'A Death Kiss has attacked the party, roll initiative!!!', response.data)
        self.assertIn(b'6 Orcs accompany it', response.data)

    def test_monster_class_beholder4(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Beholder', 'type':4, "minions":"Skeletons", "quantity":1}
        )
        self.assert200(response)
        self.assertIn(b'A Gauth has attacked the party, roll initiative!!!', response.data)
        self.assertIn(b'2 Skeletons accompany it', response.data)

    def test_monster_class_beholder5(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Beholder', 'type':5, "minions":"Skeletons", "quantity":2}
        )
        self.assert200(response)
        self.assertIn(b'A Gazer has attacked the party, roll initiative!!!', response.data)
        self.assertIn(b'4 Skeletons accompany it', response.data)

    def test_monster_class_beholder6(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Beholder', 'type':6, "minions":"Skeletons", "quantity":3}
        )
        self.assert200(response)
        self.assertIn(b'A Mindwitness has attacked the party, roll initiative!!!', response.data)
        self.assertIn(b'7 Skeletons accompany it', response.data)
