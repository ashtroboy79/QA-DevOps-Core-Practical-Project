from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    var1 = requests.get('http://service2/monster_species').text
