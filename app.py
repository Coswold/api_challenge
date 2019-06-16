from flask import Flask
from flask import jsonify, render_template, request, make_response, url_for, redirect
from flask_pymongo import PyMongo

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from search import Search

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
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api', methods=['GET'])
def get_state_capitals():
    city = mongo.db.capitals
    output = []
    for c in city.find():
        output.append({'capital' : c['capital'], 'state' : c['state']})
    return jsonify({'result' : output}), 201

@app.route('/api/<name>', methods=['GET'])
def get_one_capital(name):
    name = name.lower()
    city = mongo.db.capitals
    output = []
    # c = city.find_one({'name' : name})
    for c in city.find():
        output.append({'capital': c['capital'], 'state': c['state']})
    # res = [i for i in output if name in i['state'].lower()]
    search = Search(output, name)
    res = search.find()
    if res:
        output = res
    else:
        output = "City not in database"
    return jsonify({'result' : output}), 201

@app.route('/accept', methods=['POST'])
def accept():
    state = request.form['state']
    print(state)
    return redirect(url_for('get_one_capital', name=state))


if __name__ == '__main__':
    app.run()
