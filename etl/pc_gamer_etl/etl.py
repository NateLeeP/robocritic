import mysql.connector

try:
    cnx = mysql.connector.connect()
except Exception:
    print("Failed to connect")