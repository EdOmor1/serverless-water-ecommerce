import unittest
from unittest.mock import patch
from lambda_functions.authentication.app import authenticate_user

class TestAuthentication(unittest.TestCase):

    def test_authentication_success(self):
        event = {'userId': 'test_user'}
        context = None
        response = authenticate_user(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertTrue(response['body']['authenticated'])
        self.assertEqual(response['body']['message'], 'User test_user authenticated successfully.')

    def test_authentication_failure(self):
        event = {}
        context = None
        response = authenticate_user(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertFalse(response['body']['authenticated'])
        self.assertEqual(response['body']['message'], 'Authentication failed. User ID not provided.')

if __name__ == '__main__':
    unittest.main()
