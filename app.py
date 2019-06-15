from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'citydb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/citydb'

mongo = PyMongo(app)

#client = pymongo.MongoClient("mongodb://localhost:27017/citydb")

#db = client['citydb']

#cities = db.cities

city1 = {
        'name': 'Boston',
        'state': 'MA'
        }

#result = cities.insert_one(city1)
#print('City: {0}'.format(result.inserted_id))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api', methods=['GET'])
def get_all_cities():
    city = mongo.db.cities
    output = []
    for s in city.find():
        output.append({'name' : s['name'], 'state' : s['state']})
    return jsonify({'result' : output}), 201

@app.route('/api/<name>', methods=['GET'])
def get_one_city(name):
    city = mongo.db.cities
    s = city.find_one({'name' : name})
    if s:
        output = {'name' : s['name'], 'state' : s['state']}
    else:
        output = "City not in database"
    return jsonify({'result' : output}), 201


if __name__ == '__main__':
    app.run()
