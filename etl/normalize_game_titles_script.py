from helper_functions.db_reader import RobocriticDBReader
from helper_functions.robo_db_writer import RoboCriticDBWriter
from helper_functions.utils import normalize_game_title
import mysql.connector
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def update_normalized_titles(connection: mysql.connector.connection.MySQLConnection) -> None:
    reader = RobocriticDBReader(connection)
    writer = RoboCriticDBWriter(connection)
    
    # Get all games
    games = reader.get_all_games()
    logger.info(f"Found {len(games)} games to process")
    
    for game in games:
        # Calculate normalized title
        normalized_title = normalize_game_title(game['title'])
        
        # Update the game record
        success = writer.update_game(
            game_id=game['id'],
            normalized_title=normalized_title
        )
        
        if success:
            logger.info(f"Updated game '{game['title']}' with normalized title '{normalized_title}'")
        else:
            logger.error(f"Failed to update game '{game['title']}'")
    
    connection.commit()
    logger.info("Completed normalized title updates")

if __name__ == "__main__":
    # Setup database connection
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE')
    )
    
    try:
        update_normalized_titles(connection)
    finally:
        connection.close()