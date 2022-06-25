from urllib import response
from application import app
from flask import url_for
from flask_testing import TestCase
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestMonsterClass(TestBase):
   
    def test_monster_class_dragon1(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Dragon', 'type':1}
        )
        self.assert200(response)
        self.assertIn(b'A Black Dragon has attacked the party', response.data)

    def test_monster_class_dragon2(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Dragon', 'type':2}
        )
        self.assert200(response)
        self.assertIn(b'Red Dragon', response.data)

    def test_monster_class_dragon3(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Dragon', 'type':3}
        )
        self.assert200(response)
        self.assertIn(b'Green Dragon', response.data)

    def test_monster_class_dragon4(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Dragon', 'type':4}
        )
        self.assert200(response)
        self.assertIn(b'Blue Dragon', response.data)

    def test_monster_class_dragon5(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Dragon', 'type':5}
        )
        self.assert200(response)
        self.assertIn(b'White Dragon', response.data)

    def test_monster_class_dragon6(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Dragon', 'type':6}
        )
        self.assert200(response)
        self.assertIn(b'Zombie Dragon', response.data)

    