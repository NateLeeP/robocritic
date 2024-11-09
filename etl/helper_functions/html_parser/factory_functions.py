
from .pcgamer import PCGamerGameReviewParser
from .ign import IGNGameReviewParser
from .gamespot import GameSpotReviewParser
from .base import AbstractHTMLParser
import requests
from bs4 import BeautifulSoup
import re
# Import other parsers as needed    

header_mapping = {"User-Agent": "Mac Firefox"}

def fetch_html(url):
    response = requests.get(url, headers=header_mapping)
    return response.content

def get_pcgamer_review_urls(soup):
    """
    Expected HTML content from PC Gamer reviews page: 
        https://www.pcgamer.com/reviews/
        
        """

    # Find all the anchor tags with the class "article-link"
    review_links = soup.find_all('a', class_='article-link')

    # Filter out hardware reviews by checking if the "/games" path is present in the URL
    video_game_review_urls = [link['href'] for link in review_links if '/games' in link['href']]

    return video_game_review_urls

def get_ign_review_urls(soup):
    """
    Expected HTML content from IGN reviews page: 
        https://www.ign.com/reviews/games
    """
    latest_reviews_a_tag_list = soup.find(
        class_="main-content"
    ).find_all("a")

    filter_latest_reviews_a_tag = filter(
        lambda x: bool(x.get("aria-label")), latest_reviews_a_tag_list
    )

    filtered_a_tags = list(filter_latest_reviews_a_tag)

    review_urls = ['https://www.ign.com' + x.get("href") for x in filtered_a_tags]

    # filter out board games
    video_game_reviews = [x for x in review_urls if "board-game" not in x]

    return video_game_reviews

def get_gamespot_review_urls(soup):
    """Expected HTML content from Gamespot reviews page
        https://www.gamespot.com/games/reviews/
    """
    a_tags = soup.find_all('a')

    pattern = r'.*/reviews/[a-z0-9\-]+-review[a-z0-9\-]*/\d{4}-\d{7}/$'

    def filter_game_reviews(a):
        url = a.get('href')
        return re.match(pattern, url) if url else False

    mapped_tags = map(lambda x: "https://www.gamespot.com" + x.get('href') if x.get('href').startswith('/reviews/') else x.get('href'), filter(filter_game_reviews, a_tags))
    tags_list = list(mapped_tags)
    return tags_list

publisher_url_map = {
    'pcgamer': 'https://www.pcgamer.com/reviews/',
    "ign": "https://www.ign.com/reviews/games",
    "gamespot": "https://www.gamespot.com/games/reviews/"
}

publisher_parser_function_map = {
    'pcgamer': get_pcgamer_review_urls,
    'ign': get_ign_review_urls,
    "gamespot": get_gamespot_review_urls
}



def get_review_urls(publisher: str):
    """
    Get the review URLs for a given publisher.
    """

    if publisher in publisher_url_map:
        html_content = fetch_html(publisher_url_map[publisher])
        soup = BeautifulSoup(html_content, 'html.parser')
        return publisher_parser_function_map[publisher](soup)
    else:
        raise ValueError(f"Unsupported publisher: {publisher}")


def get_parser(source: str, html_content: str) -> AbstractHTMLParser:
    parser_map = {
        'pcgamer': PCGamerGameReviewParser,
        'ign': IGNGameReviewParser,
        'gamespot': GameSpotReviewParser
        # Add other sources and their corresponding parser classes here
    }

    if source in parser_map:
        return parser_map[source](html_content)

    raise ValueError(f"Parser for source '{source}' not found.")