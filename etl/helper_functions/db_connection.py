import mysql.connector
from dotenv import load_dotenv
import os
from mysql.connector import Error

load_dotenv()


def create_connection(host_name, user_name, user_password, database_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=database_name,
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    return connection


connection = create_connection(
    "localhost", os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), "robocritic"
)
