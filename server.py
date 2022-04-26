from flask import Flask
from flask import jsonify
from flask import request

server = Flask(__name__)
breakfasts = [
    {'name': 'eggs', 'vegetable': False},
    {'name': 'bacon', 'vegetable': False},
    {'name': 'tomatoes', 'vegetable': True},
    {'name': 'mushrooms', 'vegetable': True},
]

@server.route('/') 
def home(): 
    return """
Welcome to the breakfast API<br>

Access all breakfasts at /breakfast<br>

Access a breakfast at /breakfast/id<br>

Make a POST request to /breakfast to create a breakfast
"""

@server.route('/breakfast') 
def return_all_breakfast(): 
    return jsonify(breakfasts)

@server.route('/breakfast/<int:breakfast_id>') 
def return_breakfast(breakfast_id): 
    breakfast_id -= 1
    if (breakfast_id != -1 and breakfast_id < len(breakfasts)):
        return breakfasts[breakfast_id]
    else:
        return 'Breakfast not found!'

@server.route('/breakfast', methods=['POST']) 
def create_breakfast(): 
    new_breakfast = request.get_json()
    if ('name' in new_breakfast and 'vegetable' in new_breakfast):
        breakfasts.append(new_breakfast)
        return f'{new_breakfast["name"]} created. It is {new_breakfast["vegetable"]} that it is a vegetable. Access it at ID {len(breakfasts)}!'
    else:
        return 'Invalid breakfast!'

server.run(debug=True)