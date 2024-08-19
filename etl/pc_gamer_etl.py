import os
from dotenv import load_dotenv
load_dotenv()
import requests
from requests.exceptions import RequestException

from helper_functions.openai_service import OpenAIService
from helper_functions import pc_gamer_etl_func
from helper_functions import igdb_service
from helper_functions.html_parser.pcgamer import PCGamerReviewsParser, PCGamerGameReviewParser
def main():
    reviews_url = 'https://www.pcgamer.com/reviews/'
    try:
        # Get the HTML content from the PC Gamer reviews page
        response = requests.get(reviews_url)
        response.raise_for_status()
        html_content = response.content
    except RequestException as e:
        print("Failed to get the HTML content from the PC Gamer reviews page", e)
        return
    # Parse the HTML content to extract the video game review URLs
    parser = PCGamerReviewsParser(html_content)
    video_game_review_urls = parser.get_video_game_review_urls()
    # Print the extracted URLs
    igdb_service_instance = igdb_service.IGDBService()
    for url in video_game_review_urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            html_content = response.content
        except RequestException as e:
            print(f"Failed to get the HTML content from the game review page, url: {url}", e)
            continue
        html_parser = PCGamerGameReviewParser(html_content)
        article_body = html_parser.get_review_text()
        game_title = html_parser.get_game_title()
        if article_body is None or game_title is None:
            print(f'No article body and / or game title found for url: {url}')
            print(f'article body: {article_body}')
            print(f'game title: {game_title}')
            continue
        release_date = igdb_service_instance.get_first_release_date_by_title(game_title)
        print(release_date)
        pc_gamer_etl_func.insert_game(game_title, release_date)
        openai_pros_cons = OpenAIService().extract_review_pros_and_cons(article_body)
        openai_scores = OpenAIService().assign_score_to_content(article_body)
        print(openai_pros_cons)
        print(openai_scores)
    return 

if __name__ == "__main__":
    main()