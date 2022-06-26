from application import app
from random import randint
from flask import jsonify

@app.route('/monster_type', methods=['Get'])
def monster_type():
    return jsonify(type=randint(1, 6))
