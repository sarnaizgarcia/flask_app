from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:} --- Creates new store with a given name
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name> --- Get a store for a given name
@app.route('/store/<string:name>')  # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    pass

# GET /store --- Returns list of all stores
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})  # converts store variable into JSON

# POST /store/<string:name>/item {name:, price:} --- Creates an item inside a specific store of a given name
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item --- Gets all the items in a specific store
# 'http://127.0.0.1:5000/store/some_name'
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass


app.run(port=5000)
