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
            json = {'monster':'Giant', 'type':1}
        )
        self.assert200(response)
        self.assertIn(b'Fire Giant', response.data)

    def test_monster_class2(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Giant', 'type':2}
        )
        self.assert200(response)
        self.assertIn(b'Hill Giant', response.data)

    def test_monster_class3(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Giant', 'type':3}
        )
        self.assert200(response)
        self.assertIn(b'Cloud Giant', response.data)

    def test_monster_class4(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Giant', 'type':4}
        )
        self.assert200(response)
        self.assertIn(b'Frost Giant', response.data)

    def test_monster_class5(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Giant', 'type':5}
        )
        self.assert200(response)
        self.assertIn(b'Stone Giant', response.data)

    def test_monster_class6(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Giant', 'type':6}
        )
        self.assert200(response)
        self.assertIn(b'Storm Giant', response.data)


        
