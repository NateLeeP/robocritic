from .db_connection import connection
import os
import mysql.connector.errors as mysql_errors
class RobocriticDBReader:
    def __init__(self):
        self.connection = connection
    
    def get_game(self, title):
        """
            Retrieves a game record from the database based on the given title.

            Parameters:
            title (str): The title of the game to retrieve.

            Returns:
            dict: A dictionary representing the game record if found, or None if not found.
            The dictionary will have the following keys: 'id', 'title', 'release_date', etc.
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM game WHERE tite = %s"
            cursor.execute(query, (title,))
            game = cursor.fetchone()
        except mysql_errors.ProgrammingError as e:
            print(f"(Programming Error) Error retrieving game: {e}")
            return None
        finally:
            cursor.close()
        return game