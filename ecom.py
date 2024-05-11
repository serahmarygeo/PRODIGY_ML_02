from flask import Flask, jsonify, request

app =Flask(__name__)

# Sample data for products
products = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 20.99},
    {"id": 3, "name": "Product 3", "price": 15.99}
]

# GET all products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

# GET a specific product by id
@app.route('/api/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((product for product in products if product['id'] == id), None)
    return jsonify(product) if product else jsonify({'error': 'Product not found'}), 404

# POST a new product
@app.route('/api/products', methods=['POST'])
def add_product():
    new_product = request.json
    products.append(new_product)
    return jsonify(new_product), 201

# PUT update a product by id
@app.route('/api/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = next((product for product in products if product['id'] == id), None)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    product.update(request.json)
    return jsonify(product)

# DELETE a product by id
@app.route('/api/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    global products
    products = [product for product in products if product['id'] != id]
    return jsonify({'message': 'Product deleted'})

if _name_ == '_main_':
    app.run(debug=True)