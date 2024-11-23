import argparse
import datetime
from helper_functions.db_reader import RobocriticDBReader
from helper_functions.db_connection import connection
from helper_functions.robo_db_writer import RoboCriticDBWriter
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

date_one_month_ago = datetime.datetime.now() - datetime.timedelta(days=30)

parser = argparse.ArgumentParser(description="Calculate game average critic score")
parser.add_argument("--earliest_game_release_date", 
                    type=str, 
                    help="The earliest game release date to include in the calculation", 
                    default=date_one_month_ago.date().strftime("%Y-%m-%d"))

args = parser.parse_args()

writer = RoboCriticDBWriter(connection)
reader = RobocriticDBReader(connection)
def normalize_score(score, original_scale):
    """
    Normalize a review score to a scale of 0 to 100.
    
    Args:
        score (float): The original score.
        original_scale (int or float): The maximum value of the original scale.
    
    Returns:
        int: The normalized score on a scale of 0 to 100.
    """
    if original_scale <= 0:
        raise ValueError("Original scale must be greater than 0.")
    return int((score / original_scale) * 100)

def calculate_game_average(game_id: int) -> float:
    reviews = reader.get_reviews_by_game(game_id)
    score_total = 0
    for review in reviews:
        score_scale = reader.get_publisher_by_id(review['publisher_id'])['rating_scale']
        normalized_score = normalize_score(review['critic_score'], score_scale)
        score_total += normalized_score
    return score_total / len(reviews) if reviews else 0



def main():
    # Get all games released after the earliest game release date

    print(args.earliest_game_release_date)

    games = reader.get_games_after_release_date(args.earliest_game_release_date)

    for game in games:
        average_score = calculate_game_average(game['id'])
        writer.update_game(game['id'], critic_score_average=average_score)
        logger.info(f"Updated game {game['id']} / {game['title']} with average critic score {average_score}")


if __name__ == "__main__":
    main()