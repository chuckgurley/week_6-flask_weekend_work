from flask import Blueprint, request, jsonify
from bar_inventory.helpers import token_required, random_joke_generator
from bar_inventory.models import db, Bar, bar_schema, bars_schema

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/getdata')
@token_required
def getdata(our_user0):
    return {'some': 'value'}

@api.route('/bars', methods = ["POST"])
@token_required
def create_bar(our_user):
    
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    chocolate_quality = request.json['chocolate_quality']
    melt_temp = request.json['melt_temp']
    freeze_time = request.json['freeze_time']
    dimensions = request.json['dimensions']
    weight = request.json['weight']
    cost_of_production = request.json['cost_of_production']
    series = request.json['series']
    random_joke = random_joke_generator()
    user_token = our_user.token

    print(f"User Token: {our_user.token}")

    bar = Bar(name, description, price, chocolate_quality, melt_temp, freeze_time, dimensions, weight, cost_of_production, series, random_joke, user_token = user_token )

    db.session.add(bar)
    db.session.commit()

    response = bar_schema.dump(bar)

    return jsonify(response)

#  retrieve (read)all bars
@api.route('/bars', methods = ['GET'])
@token_required
def get_bars(our_user):
    owner = our_user.token
    bars = Bar.query.filter_by(user_token = owner).all()
    response = bars_schema.dump(bars)

    return jsonify(response)

#retrieve one sigular individual lonely bar
#bar
@api.route('/bars/<id>', methods = ['GET'])
@token_required
def get_barbar(our_user, id):    
    if id:
        bar = Bar.query.get(id)
        response = bar_schema.dump(bar)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid Id required'}), 401
    
#update bar by id
@api.route('/bars/<id>', methods = ["PUT"])
@token_required
def update_bar(our_user, id): 
    bar = Bar.query.get(id)   
    bar.name = request.json['name']
    bar.description = request.json['description']
    bar.price = request.json['price']
    bar.tire_quality = request.json['tire_quality']
    bar.drive_time = request.json['drive_time']
    bar.max_speed = request.json['max_speed']
    bar.height = request.json['height']
    bar.weight = request.json['weight']
    bar.cost_of_production = request.json['cost_of_production']
    bar.series = request.json['series']
    bar.random_joke = random_joke_generator()
    bar.user_token = our_user.token  

    db.session.commit()

    response = bar_schema.dump(bar)

    return jsonify(response)

#DELETE bar by id
@api.route('/bars/<id>', methods = ['DELETE'])
@token_required
def delete_bars(current_user, id):
    bar = Bar.query.get(id)
    db.session.delete(bar)
    db.session.commit()

    response = bar_schema.dump(bar)
    return jsonify(response)