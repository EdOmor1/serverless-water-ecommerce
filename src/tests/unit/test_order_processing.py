import unittest
from lambda_functions.order_processing.app import process_order

class TestOrderProcessing(unittest.TestCase):

    def test_process_order_success(self):
        event = {'body': '{"user_id": 1, "product_id": 1, "quantity": 1}'}
        context = None
        response = process_order(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertIsNotNone(response['body']['orderId'])
        self.assertEqual(response['body']['message'], 'Order ORD123456789 processed successfully.')

    def test_process_order_failure(self):
        event = {'body': ''}
        context = None
        response = process_order(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertIsNone(response['body']['orderId'])
        self.assertEqual(response['body']['message'], 'Order processing failed. No order data provided.')

if __name__ == '__main__':
    unittest.main()
