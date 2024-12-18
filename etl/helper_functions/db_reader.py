import mysql.connector
from mysql.connector import Error
from typing import List, Dict, Any
import logging
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class RobocriticDBReader:
    def __init__(self, connection: mysql.connector.connection.MySQLConnection):
        self.connection = None
        try:
            self.connection = connection
            print("Successfully connected to the database")
        except Error as e:
            print(f"Error connecting to the database: {e}")


    def _execute_query(self, query: str, params: tuple = None) -> List[Dict[str, Any]]:
        """
        Executes a SQL query against the database.

        Args:
            query (str): The SQL query to be executed.
            params (tuple, optional): A tuple of parameters to be used with the query. 
                                      Defaults to None.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries representing the rows returned 
                                   by the query. Each dictionary corresponds to a row, 
                                   with column names as keys. Returns an empty list if 
                                   an error occurs or no results are found.
        """
        try:
            cursor = self.connection.cursor(dictionary=True)
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except mysql.connector.Error as e:
            logger.error(f"Error executing query: {query} for error {e} in db_reader.py")
            logger.error(f"Error type: {type(e).__name__}")
    def get_game(self, game_id: int) -> Dict[str, Any]:
        query = "SELECT * FROM game WHERE id = %s"
        result = self._execute_query(query, (game_id,))
        return result[0] if result else {}

    def get_review(self, review_id: int) -> Dict[str, Any]:
        query = "SELECT * FROM review WHERE id = %s"
        result = self._execute_query(query, (review_id,))
        return result[0] if result else {}

    def get_reviewer(self, reviewer_id: int) -> Dict[str, Any]:
        query = "SELECT * FROM reviewer WHERE id = %s"
        result = self._execute_query(query, (reviewer_id,))
        return result[0] if result else {}

    def get_all_games(self) -> List[Dict[str, Any]]:
        query = "SELECT * FROM game"
        return self._execute_query(query)
    
    def get_games_after_release_date(self, release_date: datetime.date) -> List[Dict[str, Any]]:
        query = "SELECT * FROM game WHERE release_date >= %s"
        return self._execute_query(query, (release_date,))

    def get_all_reviews(self) -> List[Dict[str, Any]]:
        query = "SELECT * FROM review"
        return self._execute_query(query)

    def get_all_reviewers(self) -> List[Dict[str, Any]]:
        query = "SELECT * FROM reviewer"
        return self._execute_query(query)

    def get_reviews_by_game(self, game_id: int) -> List[Dict[str, Any]]:
        query = "SELECT * FROM review WHERE game_id = %s"
        return self._execute_query(query, (game_id,))

    def get_reviews_by_reviewer(self, reviewer_id: int) -> List[Dict[str, Any]]:
        query = "SELECT * FROM review WHERE reviewer_id = %s"
        return self._execute_query(query, (reviewer_id,))
    
    def get_game_by_title(self, game_name: str) -> Dict[str, Any]:
        query = "SELECT * FROM game WHERE title = %s"
        result = self._execute_query(query, (game_name,))
        return result[0] if result else {}

    def get_review_by_publisher_id_and_game(self, publisher_id: int, game_id: int) -> Dict[str, Any]:
        query = "SELECT * FROM review WHERE publisher_id = %s AND game_id = %s"
        result = self._execute_query(query, (publisher_id, game_id))
        return result[0] if result else {}

    def get_reviewer_by_name_and_publisher(self, reviewer_full_name: str, publisher_id: int) -> Dict[str, Any]:
        query = "SELECT * FROM reviewer WHERE reviewer_full_name = %s AND publisher_id = %s"
        result = self._execute_query(query, (reviewer_full_name, publisher_id))
        return result[0] if result else {}
    def get_publisher_by_id(self, publisher_id: int) -> Dict[str, Any]:
        query = "SELECT * FROM publisher WHERE id = %s"
        result = self._execute_query(query, (publisher_id,))
        return result[0] if result else {}
    
    def get_game_by_normalized_title(self, normalized_title: str) -> Dict[str, Any]:
        query = "SELECT * FROM game WHERE normalized_title = %s"
        result = self._execute_query(query, (normalized_title,))
        return result[0] if result else {}