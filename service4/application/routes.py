from application import app
from random import choice
from flask import request


@app.route('/monster_class', methods=['POST'])
def monster_class():
    data_sent = request.get_json()
    monster = {
        "Dragon":['Black', 'Red', 'Green', 'Blue', 'White', 'Zombie'],
        "Giant":['Fire', 'Hill', 'Cloud', 'Frost', 'Stone', 'Storm'],
        "Troll":['Dire', 'Ice', 'Rot', 'Venom', 'Spirit', 'Ancient'],
        "Beholder":["Death tyrant", "Spectator", "Death Kiss", "Gauth", "Gazer", "Mindwitness"],
        "Demon":["Barlgura", "Chasme", "Glabrezu", "Nalfeshnee", "Vrock", "Yochlol" ],
        "Liche":["Archlich", "Mindflayer", "Demilich", "Dracolich", "Baelnorn", "Banelich" ],
        "Vampire":["Corpse", "Eastern", "Spirit", "lord", "muse", "spawn"]

    }
    monster_class = monster[data_sent['monster']][data_sent['type']-1]
    print(monster_class)
    if monster_class == "Archlich":
        return f"An {monster_class} has attacked the party"
    elif (data_sent['monster'] in ("Beholder" , "Demon")):
        return f"A {monster_class} has attacked the party roll initiative"
    elif monster_class in ("Demilich", "Dracolich", "Banelich", "lord", "muse", "spawn"):
        return f"A {monster_class} has attacked your party, roll initiative"
    return f"A {monster_class} {data_sent['monster']} has attacked the party, roll initiative!!!"
