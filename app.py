from flask import Flask, jsonify, request, render_template

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


@app.route('/')
def home():
    # flask lo busca directamente en el directorio 'templates'
    return render_template('index.html')

# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:} --- Creates new store with a given name
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()  # convierte el json en diccionario
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name> --- Get a store for a given name
@app.route('/store/<string:name>')  # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        return jsonify({'message': 'store not found'})

    # GET /store --- Returns list of all stores


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})  # converts store variable into JSON

# POST /store/<string:name>/item {name:, price:} --- Creates an item inside a specific store of a given name
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return new_item
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item --- Gets all the items in a specific store
# 'http://127.0.0.1:5000/store/some_name'
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5000)
