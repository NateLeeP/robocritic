import requests
import mysql.connector
from helper_functions.html_parser.pcgamer import PCGamerReviewsParser, PCGamerGameReviewParser
from helper_functions.db_reader import RobocriticDBReader
from helper_functions.igdb_service import IGDBService
from helper_functions.openai_service import OpenAIService
from helper_functions.db_connection import connection
from helper_functions.robo_db_writer import RoboCriticDBWriter
from helper_functions.giant_bomb_api import GiantBombAPI
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def fetch_html(url):
    response = requests.get(url)
    return response.content

def extract_review_urls(html_content):
    parser = PCGamerReviewsParser(html_content)
    return parser.get_video_game_review_urls()

def extract_review_details(html_content):
    parser = PCGamerGameReviewParser(html_content)
    return parser.get_review_text(), parser.get_game_title(), parser.get_critic_score()

def extract_reviewer_details(html_content):
    parser = PCGamerGameReviewParser(html_content)
    return parser.get_reviewer_name(), parser.get_reviewer_bio_url()

platform_id_map = {
    'PlayStation 5': 1,
    'PlayStation 4': 2,
    'Xbox Series X|S': 3,
    'Xbox One': 4,
    'Nintendo Switch': 5,
    'PC (Microsoft Windows)': 6
}

publisher_id = 1

def main():
    pc_gamer_url = 'https://www.pcgamer.com/reviews/'
    html_content = fetch_html(pc_gamer_url)
    review_urls = extract_review_urls(html_content)
    
    db_reader = RobocriticDBReader(connection)
    db_writer = RoboCriticDBWriter(connection)
    igdb_service = IGDBService()
    openai_service = OpenAIService()
    
    for review_url in review_urls:
        review_html = fetch_html(review_url)
        review_text, game_title, critic_score = extract_review_details(review_html)
        reviewer_name, reviewer_bio_url = extract_reviewer_details(review_html)
        
        game = db_reader.get_game_by_title(game_title)
        game_id = game.get('id')
        
        if not game:
            try:
                release_date, platforms = igdb_service.get_first_release_date_by_title(game_title)
            except (ValueError, requests.exceptions.HTTPError) as e:
                logger.error(f'Error getting game {game_title} from IGDB: {e}')
                continue
            try:
                art_url = GiantBombAPI().get_game_artwork(game_title) if not None else 'placeholder_value'
            except Exception as e:
                logger.error(f'Error getting game artwork for {game_title} from Giant Bomb: {e}')
                logger.info(f'Using placeholder value for game artwork')
                art_url = 'placeholder_value'
            
            
            game_id = db_writer.write_game(game_title, release_date, art_url)
            
            for platform in platforms:
                platform_id = platform_id_map[platform]
                db_writer.write_platform_game(platform_id, game_id)
        
        try:
            connection.commit()
        except mysql.connector.errors.IntegrityError:
            connection.rollback()
            print(f'Error committing game {game_title} to database')
            continue
        
        review = db_reader.get_review_by_publisher_id_and_game(publisher_id, game_id)

        if not review:
            reviewer_id = db_reader.get_reviewer_by_name_and_publisher(reviewer_name, publisher_id)
            if not reviewer_id:
                reviewer_id = db_writer.write_reviewer(reviewer_name, publisher_id, reviewer_bio_url)
            
            robo_score = openai_service.assign_score_to_content(review_text)
            robo_score = robo_score['score']
            review_id = db_writer.write_review(review_url, robo_score, critic_score, reviewer_id, game_id, publisher_id)
            
            pros_cons = openai_service.extract_review_pros_and_cons(review_text)

            pros = json.dumps(pros_cons['pros'])
            cons = json.dumps(pros_cons['cons'])

            db_writer.write_review_pro(review_id, pros)
            db_writer.write_review_con(review_id, cons)
        
        try:
            connection.commit()
        except mysql.connector.errors.IntegrityError:
            connection.rollback()
            print(f'Error committing review {review_url} to database')
            continue

if __name__ == '__main__':
    main()