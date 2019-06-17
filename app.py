from flask import Flask
from flask import jsonify, render_template, request, make_response, url_for, redirect
from flask_pymongo import PyMongo

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from trie import TrieNode, Trie

tree = Trie()
def build_search():
    city = mongo.db.capitals
    for c in city.find():
        tree.insert(c['name'])
        print(c['name'].lower())

app = Flask(__name__)
limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=["500 per day", "50 per hour"]
)

app.config['MONGO_DBNAME'] = 'capitalsdb'
app.config['MONGO_URI'] = 'mongodb://heroku_nkr5hncm:l769nnp0qu5rdv3oenun1iva5c@ds137827.mlab.com:37827/heroku_nkr5hncm' or 'mongodb://localhost:27017/capitalsdb'

mongo = PyMongo(app)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found. Make sure the URL typed is a correct endpoint.'}), 404)

@app.route('/')
def home():
    build_search()
    return render_template('home.html')

@app.route('/api', methods=['GET'])
def get_state_capitals():
    city = mongo.db.capitals
    output = []
    for c in city.find():
        output.append({'capital' : c['capital'], 'state' : c['name']})
    return jsonify({'result' : output}), 201

@app.route('/api/<name>', methods=['GET'])
def get_one_capital(name):
    name = name.lower()
    city = mongo.db.capitals
    state = tree.search(name)
    print(state)
    res = city.find_one({'name': state})
    if res:
        output = {'capital': res['capital'], 'state': res['name']}
    else:
        output = "City not in database"
    return jsonify({'result' : output}), 201

@app.route('/accept', methods=['POST'])
def accept():
    state = request.form['state']
    print(state)
    return redirect(url_for('get_one_capital', name=state)), 201


if __name__ == '__main__':
    app.run()
