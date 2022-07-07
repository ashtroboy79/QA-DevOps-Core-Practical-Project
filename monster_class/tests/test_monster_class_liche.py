from urllib import response
from application import app
from flask import url_for
from flask_testing import TestCase
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestMonsterClass(TestBase):
   
    def test_monster_class_liche1(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Liche', 'type':1, "minions":"Orcs", "quantity":1}
        )
        self.assert200(response)
        self.assertIn(b'An Archlich has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_liche2(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Liche', 'type':2, "minions":"Orcs", "quantity":1}
        )
        self.assert200(response)
        self.assertIn(b'A Mindflayer Liche has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_liche3(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Liche', 'type':3, "minions":"Orcs", "quantity":1}
        )
        self.assert200(response)
        self.assertIn(b'A Demilich has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_liche4(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Liche', 'type':4, "minions":"Orcs", "quantity":1}
        )
        self.assert200(response)
        self.assertIn(b'A Dracolich has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_liche5(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Liche', 'type':5, "minions":"Orcs", "quantity":1}
        )
        self.assert200(response)
        self.assertIn(b'A Baelnorn Liche has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_liche6(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Liche', 'type':6, "minions":"Orcs", "quantity":1}
        )
        self.assert200(response)
        self.assertIn(b'A Banelich has attacked the party, roll initiative!!!', response.data)
