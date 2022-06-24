from application import app
from random import randint

@app.route('/monster_type', methods=['Get'])
def monster_type():
    return str(randint(1, 6))
