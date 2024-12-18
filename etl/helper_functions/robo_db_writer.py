from typing import Dict, Any, Tuple, List
import mysql.connector
from datetime import date

class RoboCriticDBWriter:
    def __init__(self, connection: mysql.connector.connection.MySQLConnection) -> None:
        self.connection = connection

    def write_game(self, title: str, release_date: date, art_url: str, normalized_title: str) -> None:
        cursor = self.connection.cursor()
        query = """
        INSERT INTO game (title, release_date, art_url, normalized_title)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (title, release_date, art_url, normalized_title))
        game_id = cursor.lastrowid
        cursor.close()
        return game_id

    def write_reviewer(self, reviewer_full_name: str, publisher_id: int, reviewer_bio_url: str) -> None:
        cursor = self.connection.cursor()
        query = """
        INSERT INTO reviewer (reviewer_full_name, publisher_id, reviewer_bio_url)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (reviewer_full_name, publisher_id, reviewer_bio_url))
        reviewer_id = cursor.lastrowid
        cursor.close()
        return reviewer_id

    def write_review(self, review_url: str, robo_score: int, critic_score: int, reviewer_id: int, game_id: int, publisher_id: int) -> None:
        cursor = self.connection.cursor()
        query = """
        INSERT INTO review (review_url, robo_score, critic_score, reviewer_id, game_id, publisher_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (review_url, robo_score, critic_score, reviewer_id, game_id, publisher_id))
        review_id = cursor.lastrowid
        cursor.close()
        return review_id

    def write_platform_game(self, platform_id: int, game_id: int) -> None:
        cursor = self.connection.cursor()
        query = """
        INSERT INTO platform_game (platform_id, game_id)
        VALUES (%s, %s)
        """
        cursor.execute(query, (platform_id, game_id))
        platform_game_id = cursor.lastrowid
        cursor.close()
        return platform_game_id

    def write_review_pro(self, review_id: int, pros: str) -> None:
        cursor = self.connection.cursor()
        query = """
        INSERT INTO review_pro (review_id, pros)
        VALUES (%s, %s)
        """
        cursor.execute(query, (review_id, pros))
        review_pro_id = cursor.lastrowid
        cursor.close()
        return review_pro_id

    def write_review_con(self, review_id: int, cons: str) -> None:
        cursor = self.connection.cursor()
        query = """
        INSERT INTO review_con (review_id, cons)
        VALUES (%s, %s)
        """
        cursor.execute(query, (review_id, cons))
        review_con_id = cursor.lastrowid
        cursor.close()
        return review_con_id
    def update_game(self, game_id: int, **fields_to_update) -> bool:
        """
        Update one or more fields for a game in the database.
        
        Args:
        game_id (int): The ID of the game to update
        **fields_to_update:  Possible fields: title, release_date, art_url, youtube_gameplay_url, average_critic_score
    
        Returns:
            bool: True if update was successful, False otherwise
        """
        if not fields_to_update:
            return False    
        
        cursor = self.connection.cursor()
    
        # Build the UPDATE query dynamically based on provided fields
        set_clause = ", ".join([f"{field} = %s" for field in fields_to_update.keys()])
        query = f"""
        UPDATE game 
        SET {set_clause}
        WHERE id = %s
        """
    
        # Create tuple of values for the query
        values = tuple(fields_to_update.values()) + (game_id,)
        
        cursor.execute(query, values)
        self.connection.commit()
        success = cursor.rowcount > 0
        cursor.close()
        return success