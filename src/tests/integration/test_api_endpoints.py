import unittest
import requests

class TestAPIEndpoints(unittest.TestCase):

    def test_authentication_endpoint(self):
        response = requests.get('http://localhost:3000/authentication')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('authenticated' in response.json())
        self.assertTrue('message' in response.json())

    def test_product_management_endpoint(self):
        response = requests.get('http://localhost:3000/product-management')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))
        self.assertTrue(len(response.json()) > 0)

    def test_order_processing_endpoint(self):
        response = requests.post('http://localhost:3000/order-processing', json={'user_id': 1, 'product_id': 1, 'quantity': 1})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('orderId' in response.json())
        self.assertTrue('message' in response.json())

if __name__ == '__main__':
    unittest.main()
