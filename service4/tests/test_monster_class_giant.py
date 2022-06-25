from urllib import response
from application import app
from flask import url_for
from flask_testing import TestCase
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestMonsterClass(TestBase):
   
    def test_monster_class_giant1(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Giant', 'type':1}
        )
        self.assert200(response)
        self.assertIn(b'A Fire Giant has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_giant2(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Giant', 'type':2}
        )
        self.assert200(response)
        self.assertIn(b'A Hill Giant has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_giant3(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Giant', 'type':3}
        )
        self.assert200(response)
        self.assertIn(b'A Cloud Giant has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_giant4(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Giant', 'type':4}
        )
        self.assert200(response)
        self.assertIn(b'A Frost Giant has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_giant5(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Giant', 'type':5}
        )
        self.assert200(response)
        self.assertIn(b'A Stone Giant has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_giant6(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Giant', 'type':6}
        )
        self.assert200(response)
        self.assertIn(b'A Storm Giant has attacked the party, roll initiative!!!', response.data)


        
