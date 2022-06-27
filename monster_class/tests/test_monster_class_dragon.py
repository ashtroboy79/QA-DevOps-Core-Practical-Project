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
            json = {'monster':'Dragon', 'type':1, "minions":"Dire Wolves", "quantity":1}
        )
        self.assert200(response)
        self.assertIn(b'A Black Dragon has attacked the party, roll initiative!!!', response.data)
        self.assertIn(b'3 Dire Wolves accompany it', response.data)

    def test_monster_class_dragon2(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Dragon', 'type':2, "minions":"Dire Wolves", "quantity":2}
        )
        self.assert200(response)
        self.assertIn(b'A Red Dragon has attacked the party, roll initiative!!!', response.data)
        self.assertIn(b'5 Dire Wolves accompany it', response.data)

    def test_monster_class_dragon3(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Dragon', 'type':3, "minions":"Dire Wolves", "quantity":3}
        )
        self.assert200(response)
        self.assertIn(b'A Green Dragon has attacked the party, roll initiative!!!', response.data)
        self.assertIn(b'6 Dire Wolves accompany it', response.data)
  
    def test_monster_class_dragon4(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Dragon', 'type':4, "minions":"Orcs", "quantity":1}
        )
        self.assert200(response)
        self.assertIn(b'A Blue Dragon has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_dragon5(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Dragon', 'type':5, "minions":"Orcs", "quantity":1}
        )
        self.assert200(response)
        self.assertIn(b'A White Dragon has attacked the party, roll initiative!!!', response.data)

    def test_monster_class_dragon6(self):
        response = self.client.post(
            url_for('monster_class'),
            json = {'monster':'Dragon', 'type':6, "minions":"Orcs", "quantity":1}
        )
        self.assert200(response)
        self.assertIn(b'A Zombie Dragon has attacked the party, roll initiative!!!', response.data)

    