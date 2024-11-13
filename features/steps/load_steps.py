from behave import given
from .models import Product

# Step to load products into the database for testing purposes
@given('the following products exist in the system')
def step_impl(context):
    """Load predefined products into the database for testing."""
    # List of sample products to load
    sample_products = [
        {"name": "Laptop", "category": "Electronics", "price": 999.99, "is_available": True},
        {"name": "Smartphone", "category": "Electronics", "price": 699.99, "is_available": True},
        {"name": "Coffee Maker", "category": "Appliances", "price": 99.99, "is_available": True},
        {"name": "Desk Chair", "category": "Furniture", "price": 149.99, "is_available": False},
    ]

    # Add each product to the database
    for product_data in sample_products:
        product = Product(
            name=product_data['name'],
            category=product_data['category'],
            price=product_data['price'],
            is_available=product_data['is_available']
        )
        product.save()  # Assuming you have a method `save()` to store the product in the database
