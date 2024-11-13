def test_read_product_route(self):
    response = self.client.get('/api/products/1/')
    self.assertEqual(response.status_code, 200)

def test_update_product_route(self):
    response = self.client.put('/api/products/1/', data={'name': 'Updated Product'})
    self.assertEqual(response.status_code, 200)

def test_delete_product_route(self):
    response = self.client.delete('/api/products/1/')
    self.assertEqual(response.status_code, 204)

def test_list_all_products_route(self):
    response = self.client.get('/api/products/')
    self.assertEqual(response.status_code, 200)

def test_list_by_name(self):
    response = self.client.get('/api/products/?name=Sample Product')
    self.assertEqual(response.status_code, 200)

def test_list_by_category(self):
    response = self.client.get('/api/products/?category=Electronics')
    self.assertEqual(response.status_code, 200)
  
def test_list_by_availability(self):
    response = self.client.get('/api/products/?available=True')
    self.assertEqual(response.status_code, 200)
