from urllib import response
from application import app
from flask import url_for
from flask_testing import TestCase
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestMonsterClass(TestBase):
   
    def test_monster_class_troll1(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Troll', 'type':1}
        )
        self.assert200(response)
        self.assertIn(b'A Dire Troll has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_troll2(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Troll', 'type':2}
        )
        self.assert200(response)
        self.assertIn(b'An Ice Troll has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_troll3(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Troll', 'type':3}
        )
        self.assert200(response)
        self.assertIn(b'A Rot Troll has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_troll4(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Troll', 'type':4}
        )
        self.assert200(response)
        self.assertIn(b'A Venom Troll has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_troll5(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Troll', 'type':5}
        )
        self.assert200(response)
        self.assertIn(b'A Spirit Troll has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_troll6(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Troll', 'type':6}
        )
        self.assert200(response)
        self.assertIn(b'An Ancient Troll has attacked the party, roll initiative!!!', response.data)
