import unittest
import psycopg2

class TestDatabaseIntegration(unittest.TestCase):

    def test_database_connection(self):
        conn = psycopg2.connect(
            host='localhost',
            port='5432',
            dbname='test_db',
            user='test_user',
            password='test_password'
        )
        self.assertIsNotNone(conn)
        conn.close()

if __name__ == '__main__':
    unittest.main()
