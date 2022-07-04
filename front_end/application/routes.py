from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    minions = {
        'Orcs' : 'orc',
        'Skeletons' : 'skeleton',
        'Goblins': 'goblin',
        'Gnolls': 'gnoll',
        'Dire Wolves' : 'dire-wolf'
    }
    monster_species = requests.get('http://service2:5000/monster_species').json()
    monster_type = requests.get('http://service3:5000/monster_type').json()
    encounter = requests.post('http://service4:5000/monster_class', json={"monster":monster_species['monster'], "type":monster_type['type'], "minions":monster_species['minions'], "quantity":monster_type['quantity']})
    minion = minions[monster_species['minions']]
    minion_details = requests.get(f'https://www.dnd5eapi.co/api/monsters/{minion}/').json()
    print(minion_details)
    return render_template('index.html', encounter_text=encounter.text, minion_details=minion_details, minion=minion)
