from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    # add item only if it is not already present
    if item in items:
        return jsonify({'error': 'Item already exists'}), 400
    else:
        items.append(item)
    return jsonify(item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id >= len(items) or item_id < 0:
        return jsonify({'error': 'Todo not found'}), 404
    item = request.json
    items[item_id] = item
    return jsonify(item), 200

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id >= len(items) or item_id < 0:
        return jsonify({'error': 'Todo not found'}), 404
    item = items.pop(item_id)
    return jsonify(item), 200

if __name__ == '__main__':
    app.run(debug=True)