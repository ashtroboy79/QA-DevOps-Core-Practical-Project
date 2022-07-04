from application import app
from random import randint
from flask import jsonify

@app.route('/monster_type', methods=['Get'])
def monster_type():
    type=randint(1, 6)
    quantity = randint(1,3)
    return jsonify(type=type, quantity=quantity)
