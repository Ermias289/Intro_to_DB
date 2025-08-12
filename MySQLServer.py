import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update user and password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # Change to your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: Could not connect to MySQL server - {e}")

    finally:
        # Close the connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            # print("MySQL connection closed.")  # Optional

if __name__ == "__main__":
    create_database()
