import requests
import mysql.connector
from helper_functions.db_reader import RobocriticDBReader
from helper_functions.igdb_service import IGDBService
from helper_functions.openai_service import OpenAIService
from helper_functions.db_connection import connection
from helper_functions.robo_db_writer import RoboCriticDBWriter
from helper_functions.giant_bomb_api import GiantBombAPI
from helper_functions.youtube_api import YoutubeApi
from helper_functions.html_parser.factory_functions import get_review_urls, get_parser
from helper_functions.utils import normalize_game_title
import json
import logging
from dotenv import load_dotenv
import os

load_dotenv()
publisher = os.getenv('PUBLISHER')

logger = logging.getLogger()
logger.setLevel(logging.INFO)
proxies = {
    "http": os.getenv('MARS_PROXY_CONNECTION'),
    "https": os.getenv('MARS_PROXY_CONNECTION')
}

def fetch_html(url):
    response = requests.get(url, headers={"User-Agent": "Mac Firefox"}, proxies=proxies)
    return response.content

def extract_review_details(html_content):
    parser = get_parser(publisher, html_content)
    return parser.get_review_text(), parser.get_game_title(), parser.get_critic_score()

def extract_reviewer_details(html_content):
    parser = get_parser(publisher, html_content)
    return parser.get_reviewer_name(), parser.get_reviewer_bio_url()

platform_id_map = {
    'PlayStation 5': 1,
    'PlayStation 4': 2,
    'Xbox Series X|S': 3,
    'Xbox One': 4,
    'Nintendo Switch': 5,
    'PC (Microsoft Windows)': 6
}

publisher_id_map = {
    "pcgamer": 1,
    "ign": 2,
    "gamespot": 3,
    "gamerant": 4
}

def main():
    review_urls = get_review_urls(publisher)
    publisher_id = publisher_id_map[publisher]

    if not connection:
        logger.error('Error connecting to database, exiting program')
        return
    
    db_reader = RobocriticDBReader(connection)
    db_writer = RoboCriticDBWriter(connection)
    igdb_service = IGDBService()
    openai_service = OpenAIService()
    
    for review_url in review_urls:
        review_html = fetch_html(review_url)
        review_text, game_title, critic_score = extract_review_details(review_html)
        reviewer_name, reviewer_bio_url = extract_reviewer_details(review_html)

        normalized_game_title = normalize_game_title(game_title)


        if not review_text or not game_title or not critic_score:
            logger.info(f"Skipping review {review_url} as it is missing required fields")
            continue
        
        game = db_reader.get_game_by_normalized_title(normalized_game_title)
        game_id = game.get('id')
        if not game:
            try:
                release_date, platforms = igdb_service.get_first_release_date_by_title(game_title)
            except (ValueError, requests.exceptions.HTTPError) as e:
                logger.error(f'Error getting game {game_title} from IGDB: {e}')
                continue
            try:
                art_url = GiantBombAPI().get_game_artwork(game_title) or 'placeholder_value'
            except Exception as e:
                logger.error(f'Error getting game artwork for {game_title} from Giant Bomb: {e}')
                logger.info(f'Using placeholder value for game artwork')
                art_url = 'placeholder_value'
            
            try:
                game_id = db_writer.write_game(game_title, release_date, art_url, normalized_game_title)
                for platform in platforms:
                    platform_id = platform_id_map[platform]
                    db_writer.write_platform_game(platform_id, game_id)
        
                connection.commit()
            except mysql.connector.Error as e:
                connection.rollback()
                logger.error(f'Error committing game {game_title} to database: {e}')
                logger.error(f'Error type: {type(e).__name__}')
                logger.info(f"Rolling back transaction, continuing with next review")
                continue
        try:
            youtube_gameplay_url = YoutubeApi().search_for_gameplay_videos(game_title)
        except requests.exceptions.HTTPError as e:
            logger.error(f'{e}')
            youtube_gameplay_url = None
        if game_id and youtube_gameplay_url:
            try:
                db_writer.update_game(game_id, youtube_gameplay_url=youtube_gameplay_url)
            except mysql.connector.Error as e:
                connection.rollback()
                logger.error(f'Error UPDATING game {game_title} in database: {e}')
                logger.error(f'Error type: {type(e).__name__}')
                logger.info(f"Rolling back transaction, continuing with next review")
                continue
        
        review = db_reader.get_review_by_publisher_id_and_game(publisher_id, game_id)

        if not review:
            reviewer = db_reader.get_reviewer_by_name_and_publisher(reviewer_name, publisher_id)
            reviewer_id = reviewer.get('id') if reviewer else None
            if not reviewer_id:
                reviewer_id = db_writer.write_reviewer(reviewer_name, publisher_id, reviewer_bio_url)
            
            robo_score = openai_service.assign_score_to_content(review_text)
            pros_cons = openai_service.extract_review_pros_and_cons(review_text)

            pros = json.dumps(pros_cons['pros'])
            cons = json.dumps(pros_cons['cons'])
            robo_score = robo_score.get('score')
            
            try:
                review_id = db_writer.write_review(review_url, robo_score, critic_score, reviewer_id, game_id, publisher_id)
                db_writer.write_review_pro(review_id, pros)
                db_writer.write_review_con(review_id, cons)
        
                connection.commit()
            except mysql.connector.Error as e:
                connection.rollback()
                logger.error(f'Error committing review {review_url} to database: {e}')
                logger.error(f'Error type: {type(e).__name__}')
                logger.info(f"Rolling back transaction, continuing with next review")
                continue

if __name__ == '__main__':
    main()