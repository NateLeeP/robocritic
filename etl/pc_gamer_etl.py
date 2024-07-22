import os
from dotenv import load_dotenv
load_dotenv()


from helper_functions.openai_service import OpenAIService
from helper_functions import pc_gamer_etl_func
from helper_functions import igdb_service
def main():
    url = 'https://www.pcgamer.com/reviews/'
    video_game_review_urls = pc_gamer_etl_func.extract_video_game_review_urls(url)
    igdb_service_instance = igdb_service.IGDBService()
    # Print the extracted URLs
    for url in video_game_review_urls:
        article_body = pc_gamer_etl_func.scrape_review_text(url)
        game_title = pc_gamer_etl_func.extract_game_title(url)
        release_date = igdb_service_instance.get_first_release_date_by_title(game_title)
        pc_gamer_etl_func.insert_game(game_title, release_date)
        # openai_pros_cons = OpenAIService().extract_review_pros_and_cons(article_body)
        # openai_scores = OpenAIService().assign_score_to_content(article_body)
        # print(openai_pros_cons)
        # print(openai_scores)
    return 

if __name__ == "__main__":
    main()