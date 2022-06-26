from application import app
from random import choice
from flask import jsonify

@app.route('/monster_species', methods=['Get'])
def monster_species():
    monster =  choice(['Dragon','Giant','Troll','Beholder','Demon','Liche','Vampire'])
    minions = choice(["Orc", "Skeleton", "Goblin", "Gnoll", "Dire Wolf"])
    return jsonify(monster=monster, minions=minions)
