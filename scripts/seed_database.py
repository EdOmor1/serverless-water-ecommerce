import psycopg2
from psycopg2 import sql

# Database connection parameters
DB_HOST = 'your-db-hostname'
DB_PORT = '5432'
DB_NAME = 'your-db-name'
DB_USER = 'your-db-username'
DB_PASSWORD = 'your-db-password'

# Sample data for seeding
USERS = [
    ('john_doe', 'john@example.com', 'hashed_password_1'),
    ('jane_doe', 'jane@example.com', 'hashed_password_2')
]

PRODUCTS = [
    ('Premium Water Bottle', 19.99, 100),
    ('Eco-Friendly Water Bottle', 14.99, 200)
]

ORDERS = [
    (1, 1, 2),
    (2, 2, 1)
]

def seed_data():
    try:
        # Connect to the database
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

        # Insert data into users table
        for user in USERS:
            cursor.execute(
                sql.SQL("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)")
                .format(sql.Identifier('users')),
                user
            )

        # Insert data into products table
        for product in PRODUCTS:
            cursor.execute(
                sql.SQL("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)")
                .format(sql.Identifier('products')),
                product
            )

        # Insert data into orders table
        for order in ORDERS:
            cursor.execute(
                sql.SQL("INSERT INTO orders (user_id, product_id, quantity) VALUES (%s, %s, %s)")
                .format(sql.Identifier('orders')),
                order
            )

        # Commit the transaction
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        print("Database seeded successfully.")

    except Exception as e:
        print(f"An error occurred while seeding the database: {e}")

if __name__ == "__main__":
    seed_data()
