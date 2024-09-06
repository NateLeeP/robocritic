
from .pcgamer import PCGamerGameReviewParser
from .ign import IGNGameReviewParser
import requests
from bs4 import BeautifulSoup
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

publisher_url_map = {
    'pcgamer': 'https://www.pcgamer.com/reviews/',
    "ign": "https://www.ign.com/reviews/games"
}

publisher_parser_function_map = {
    'pcgamer': get_pcgamer_review_urls,
    'ign': get_ign_review_urls
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


def get_parser(source, html_content):
    parser_map = {
        'pcgamer': PCGamerGameReviewParser,
        'ign': IGNGameReviewParser
        # Add other sources and their corresponding parser classes here
    }

    if source in parser_map:
        return parser_map[source](html_content)

    raise ValueError(f"Parser for source '{source}' not found.")