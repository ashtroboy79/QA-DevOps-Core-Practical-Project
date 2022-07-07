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
    monster_species = monster[data_sent['monster']]
    # print(monster_species)
    monster_type = [data_sent['type']-1][0]
    # print(monster_type)
    # monster_class = monster[data_sent['monster']][data_sent['type']-1]
    monster_class = monster_species[monster_type]
    if monster_class == "Archlich":
        encounter =  f"An {monster_class}"
    elif monster_class in ("Ice", "Eastern", "Ancient"):
        encounter = f"An {monster_class} {data_sent['monster']}"
    elif data_sent['monster'] in ("Beholder" , "Demon"):
        encounter =  f"A {monster_class}"
    elif monster_class in ("Demilich", "Dracolich", "Banelich"):
        encounter =  f"A {monster_class}"
    elif monster_class in ("lord", "muse", "spawn"):
        encounter =  f"A {data_sent['monster']} {monster_class}"
    else:
        encounter = f"A {monster_class} {data_sent['monster']}"


    minions = {
        "Orcs":["3","4","6" ],
        "Skeletons":["2","4","7"],
        "Goblins":["3","5","8"],
        "Gnolls":["2","3","4"],
        "Dire Wolves":["3","5","6"]
    }
    minion_quantity = minions[data_sent['minions']][data_sent['quantity']-1]

    minion_encounter = f"{minion_quantity} {data_sent['minions']} accompany it"
    return f"{encounter} has attacked the party, roll initiative!!! {minion_encounter}"
