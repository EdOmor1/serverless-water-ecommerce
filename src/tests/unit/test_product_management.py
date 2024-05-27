import unittest
from lambda_functions.product_management.app import get_products

class TestProductManagement(unittest.TestCase):

    def test_get_products(self):
        event = {}
        context = None
        response = get_products(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertTrue(isinstance(response['body'], list))
        self.assertTrue(len(response['body']) > 0)

if __name__ == '__main__':
    unittest.main()
