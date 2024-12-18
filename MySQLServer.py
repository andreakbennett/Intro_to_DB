import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish the connection to MySQL Server
        connection = mysql.connector.connect(
            host="localhost",        # Replace with your host if different
            user="root",    # Replace with your MySQL username
            password="123456" # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Try to create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        
    except mysql.connectorError as e:
        print(f"Error connecting to MySQL: {e}")

   
        
    
    finally:
        # Ensure resources are released
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

# Run the function
if __name__ == "__main__":
    create_database()





