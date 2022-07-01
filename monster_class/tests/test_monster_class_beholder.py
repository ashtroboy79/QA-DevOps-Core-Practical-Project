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
            json = {'monster':'Beholder', 'type':1}
        )
        self.assert200(response)
        self.assertIn(b'A Death tyrant has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_beholder2(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Beholder', 'type':2}
        )
        self.assert200(response)
        self.assertIn(b'A Spectator has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_beholder3(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Beholder', 'type':3}
        )
        self.assert200(response)
        self.assertIn(b'A Death Kiss has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_beholder4(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Beholder', 'type':4}
        )
        self.assert200(response)
        self.assertIn(b'A Gauth has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_beholder5(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Beholder', 'type':5}
        )
        self.assert200(response)
        self.assertIn(b'A Gazer has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_beholder6(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Beholder', 'type':6}
        )
        self.assert200(response)
        self.assertIn(b'A Mindwitness has attacked the party, roll initiative!!!', response.data)
