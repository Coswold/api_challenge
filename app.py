from flask import Flask
from flask import jsonify, render_template, request, make_response
from flask_pymongo import PyMongo

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=["500 per day", "50 per hour"]
)

app.config['MONGO_DBNAME'] = 'citydb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/citydb'

mongo = PyMongo(app)

city1 = {
        'name': 'Boston',
        'state': 'MA'
        }

#result = cities.insert_one(city1)
#print('City: {0}'.format(result.inserted_id))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api', methods=['GET'])
def get_state_capitals():
    city = mongo.db.cities
    output = []
    for s in city.find():
        output.append({'name' : s['name'], 'state' : s['state']})
    return jsonify({'result' : output}), 201

@app.route('/api/<name>', methods=['GET'])
def get_one_capital(name):
    city = mongo.db.cities
    s = city.find_one({'name' : name})
    if s:
        output = {'name' : s['name'], 'state' : s['state']}
    else:
        output = "City not in database"
    return jsonify({'result' : output}), 201


if __name__ == '__main__':
    app.run()
