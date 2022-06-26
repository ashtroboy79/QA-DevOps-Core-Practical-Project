from application import app
from random import choice

@app.route('/monster_species', methods=['Get'])
def monster_species():
    return choice(['Dragon','Giant','Troll','Beholder','Demon','Liche','Vampire'])
