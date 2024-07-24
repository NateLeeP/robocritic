import os

def insert_game(title, release_date, art_url="https://shorturl.at/RKbAj"):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host='127.0.0.1',  # e.g., 'localhost'
            user='root',
            password=os.environ['MYSQL_ROOT_PASSWORD'],
            database=os.environ['MYSQL_DATABASE'],
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # SQL query to insert a new game
            sql_insert_query = """
            INSERT INTO game (title, release_date, art_url) 
            VALUES (%s, %s, %s)
            """
            # Tuple of values to be inserted
            values = (title, release_date, art_url)
            
            # Execute the SQL query
            cursor.execute(sql_insert_query, values)
            # Commit the transaction
            connection.commit()
            print("Game inserted successfully")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
