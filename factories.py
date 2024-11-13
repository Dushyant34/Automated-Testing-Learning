# tests/factories.py
import factory
from myapp.models import Product

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker('name')
    category = factory.Faker('word')
    price = factory.Faker('random_number', digits=2)
    is_available = factory.Faker('boolean')
