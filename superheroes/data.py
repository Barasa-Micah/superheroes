from flask import Flask, jsonify, request
from .models import hero, Power, HeroPower,db

# The blueprint I create here will be used in defining the API routes 
app=Flask( __name__)


@app.route('/')
def home():
    return jsonify({'error':'Creating Superheroes'})

# Implementing the GET route (heroes)
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = hero.query.all()
    return jsonify([hero.serialize() for hero in heroes])


# Implementing the GET route again but now the id route

@app.route('/herores/<int:id>', methods=['GET'])
def get_hero(id):
    hero= hero.query.get(id)
    if hero is None:
        return jsonify({'error': 'Hero not found'}), 404
    return jsonify(hero.serialize())


# Implementing PATCH with the id route
@app.route('/heroes/<int:id>', methods=['PATCH'])
def update_power(id):
    power= power.query.get(id)
    if power is None:
        return jsonify({'error':'Power not found'}), 404
    

    data = request.get_json()
    if 'description' in data:
        power.description = data['description']
        db.session.commit()

    return jsonify(power.serialize())


# Implementing POST for the hero_powers route

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data=request.get_json()
    hero_id=data.get('hero_id')
    power_id=data.get('power_id')
    strength = data.get('strength')


    hero = hero.query.get(hero_id)
    power= power.query.get(power_id)


    if hero is None or power is None:
        return jsonify({'error':'Hero or Power not found'}), 404
    
    hero_power=HeroPower(hero=hero, power=power, strength=strength)
    db.session.add(hero_power)
    db.session.commit()


    return jsonify(hero_power.serialize()), 201