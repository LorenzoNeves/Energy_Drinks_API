from flask import Flask, jsonify, request

app = Flask(__name__)

drinks = [
    {
        'id': 1,
        'name': 'Monster',
        'price': '3.9$'
    },
    {
        'id': 2,
        'name': 'Redbull',
        'price': '2$'
    },
    {
        'id': 3,
        'name': 'Bally',
        'price': '5$'
    }
]

@app.route('/drinks', methods=['GET'])
def get_drinks():
    return jsonify(drinks)

@app.route('/drinks/<int:id>', methods=['GET'])
def get_drinks_by_id(id):

    for drink in drinks:
        if drink.get('id') == id:
            return jsonify(drink)

@app.route('/drinks/<int:id>', methods=['PUT'])
def edit_drink_by_id(id):

    drink_update = request.get_json()

    for index, drink in enumerate(drinks):
        if drink.get('id') == id:
            drinks[index].update(drink_update)
            return jsonify(drinks[index])

@app.route('/drinks', methods=['POST'])
def post_drink():

    new_drink = request.get_json()
    drinks.append(new_drink)
    return jsonify(drinks)

@app.route('/drinks/<int:id>', methods=['DELETE'])
def delete_drink(id):
    for index, drink in enumerate(drinks):
        if drink.get('id') == id:
            del drinks[index]

    return jsonify(drinks)

app.run(port=5000,host='localhost',debug=True)
