import requests
from helper_functions.dynamodb_services import GameReleaseDate, Reviews
from helper_functions.igdb_service import IGDBService
from helper_functions.openai_service import OpenAIService
from helper_functions.scraping_utils import (
    get_latest_reviews_from_ign,
    get_game_review_content_from_ign,
    get_game_release_date_from_metacritic,
    get_game_art_from_ign,
)
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info(event)

    latest_reviews = get_latest_reviews_from_ign()
    logger.info(f"Latest reviews: {latest_reviews}")

    # OpenAI Health check
    logger.info(f"OpenAI health check: {OpenAIService().health_check()}")

    for review in latest_reviews:
        game_title = review["title"]
        logger.info(game_title)
        game_release_date = None
        try:
            game_release_date = (
                IGDBService()
                .get_first_release_date_by_title(game_title)
                .strftime("%Y-%m-%d")
            )
        except requests.exceptions.HTTPError as e:
            logger.error(e)
        except ValueError as e:
            logger.error(e)

        if not game_release_date:
            # Try pulling release date with refactored game title
            # Drop 'Early Access' text from game title - IGN includes it.
            formatted_game_title = game_title.split("Early Access")[0].rstrip()
            try:
                logger.info(
                    "Querying IGDB for game release date with formatted game title"
                )
                game_release_date = (
                    IGDBService()
                    .get_first_release_date_by_title(formatted_game_title)
                    .strftime("%Y-%m-%d")
                )
            except requests.exceptions.HTTPError as e:
                logger.error(e)
            except ValueError as e:
                logger.error(e)

        if not game_release_date:
            # if pulling release_date from igdb service failed, try metacritic
            try:
                logger.info("Querying metacritic for game release date")
                game_release_date = get_game_release_date_from_metacritic(
                    formatted_game_title
                )
                game_release_date = game_release_date.strftime("%Y-%m-%d")
            except requests.exceptions.HTTPError as e:
                logger.error(e)
            except ValueError as e:
                logger.error(e)

        if not game_release_date:
            # If fail to pull release date from meta critic and API, mark as no release date
            game_release_date = "NoRelease"

        logger.info(game_release_date)
        logger.info(game_release_date + "_" + game_title)

        # Get game art
        try:
            game_art_url = get_game_art_from_ign(game_title)
        except requests.exceptions.HTTPError as e:
            logger.error(e)
        except ValueError as e:
            logger.error(e)

        release_date_game_title = game_release_date + "_" + game_title
        # Write game to DB.
        GameReleaseDate().write_item(release_date_game_title, game_art_url)

        logger.info(f"Writing review to db for {review['title']}")
        # Scrape review from site.
        # Check if review exists for review.
        review_in_db = Reviews().get_review_by_game_title_and_reviewer_name(
            game_title=game_title, review_publisher_name="IGN"
        )
        if review_in_db:
            # if review does not exist, continue to next in loop.
            logger.info(f"Review found for game {game_title} published by IGN")
            continue

        review_url = "https://www.ign.com" + review["href"]
        logger.info(f"Scrape review from {review_url}")
        game_review_content = None
        try:
            game_review_content = get_game_review_content_from_ign(review_url)
        except requests.exceptions.HTTPError as e:
            logger.error(e)

        if game_review_content:
            # Get roboscore from open ai
            score_json = OpenAIService().assign_score_to_content(game_review_content)
            score = score_json["score"]

            # Send content to OpenAI API.
            pros_cons_json = OpenAIService().extract_review_pros_and_cons(
                game_review_content
            )

            # Parse pros cons list
            # Create a list of tuples with review_id, text
            pros = pros_cons_json["pros"]
            cons = pros_cons_json["cons"]

            reviews_response = Reviews().write_item(
                game_title=game_title,
                review_publisher_name="IGN",
                game_release_date=game_release_date,
                list_of_pros=pros,
                list_of_cons=cons,
                roboscore=score,
            )
            logger.info(reviews_response)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": "Success",
    }
