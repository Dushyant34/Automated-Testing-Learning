from flask import Flask, jsonify, request
from .models import Product

@app.route('/api/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict())

@app.route('/api/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    product.name = request.json.get('name', product.name)
    product.save()
    return jsonify(product.to_dict())

@app.route('/api/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    product.delete()
    return '', 204

@app.route('/api/products', methods=['GET'])
def list_all_products():
    try:
        products = Product.query.all()  # Fetch all products from the database
        return jsonify([product.to_dict() for product in products]), 200  # Return as JSON list
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@app.route('/api/products/search/name', methods=['GET'])
def list_by_name():
    name = request.args.get('name')  # Get 'name' from query parameters
    products = Product.query.filter(Product.name.ilike(f'%{name}%')).all()  # Search for products with a name similar to 'name'
    return jsonify([product.to_dict() for product in products]), 200
@app.route('/api/products/search/category', methods=['GET'])

def list_by_category():
    category = request.args.get('category')  # Get 'category' from query parameters
    products = Product.query.filter_by(category=category).all()  # Filter products by category
    return jsonify([product.to_dict() for product in products]), 200

@app.route('/api/products/search/availability', methods=['GET'])
def list_by_availability():
    is_available = request.args.get('is_available', type=bool)  # Get availability from query params
    products = Product.query.filter_by(is_available=is_available).all()  # Filter by availability
    return jsonify([product.to_dict() for product in products]), 200
