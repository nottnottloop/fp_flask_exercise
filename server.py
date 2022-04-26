from flask import Flask
from flask import jsonify
from flask import request
import random

server = Flask(__name__)
breakfasts = [
    {'name': 'eggs', 'vegetable': False},
    {'name': 'bacon', 'vegetable': False},
    {'name': 'tomatoes', 'vegetable': True},
    {'name': 'mushrooms', 'vegetable': True},
]

@server.route('/') 
def home(): 
    return """<style>body {font-family: sans-serif; background-color: black; color: lime;}</style>
Welcome to the breakfast API<br>

Access all breakfasts at /breakfast<br>

Access a breakfast at /breakfast/id<br>

Make a POST request to /breakfast to create a breakfast<br>

Access a <em>random</em> breakfast at /breakfast/random 😮<br><br>
<img height="400px" src="https://media.istockphoto.com/photos/breakfast-with-bacon-eggs-pancakes-and-toast-picture-id533645537?k=20&m=533645537&s=612x612&w=0&h=KJXCpAo9XQvMI_djcnRMSsz_Y7OGS6z3-8VThxWyR0Q=">
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

@server.route('/breakfast/random') 
def return_random_breakfast(): 
    return breakfasts[random.randint(0, len(breakfasts) - 1)]

@server.route('/breakfast', methods=['POST']) 
def create_breakfast(): 
    new_breakfast = request.get_json()
    if ('name' in new_breakfast and 'vegetable' in new_breakfast):
        breakfasts.append(new_breakfast)
        return f'{new_breakfast["name"]} created. It is {new_breakfast["vegetable"]} that it is a vegetable. Access it at ID {len(breakfasts)}!'
    else:
        return 'Invalid breakfast!'

server.run(debug=True)