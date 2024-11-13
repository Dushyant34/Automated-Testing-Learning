def test_read_product(self):
    product = Product.objects.create(name="Sample Product", category="Electronics")
    fetched_product = Product.objects.get(name="Sample Product")
    self.assertEqual(fetched_product.name, "Sample Product")

def test_update_product(self):
    product = Product.objects.create(name="Old Product", category="Electronics")
    product.name = "Updated Product"
    product.save()
    updated_product = Product.objects.get(id=product.id)
    self.assertEqual(updated_product.name, "Updated Product")

def test_delete_product(self):
    product = Product.objects.create(name="Sample Product")
    product.delete()
    self.assertRaises(Product.DoesNotExist, Product.objects.get, name="Sample Product")

def test_list_all_products(self):
    product1 = Product.objects.create(name="Product 1")
    product2 = Product.objects.create(name="Product 2")
    products = Product.objects.all()
    self.assertEqual(len(products), 2)

def test_find_by_name(self):
    product = Product.objects.create(name="Sample Product")
    found_product = Product.objects.get(name="Sample Product")
    self.assertEqual(found_product.name, "Sample Product")

def test_find_by_category(self):
    category = "Electronics"
    product = Product.objects.create(name="Product 1", category=category)
    products = Product.objects.filter(category=category)
    self.assertGreater(len(products), 0)

def test_find_by_availability(self):
    product = Product.objects.create(name="Product 1", is_available=True)
    available_products = Product.objects.filter(is_available=True)
    self.assertGreater(len(available_products), 0)
