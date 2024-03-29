import requests
from bs4 import BeautifulSoup
from datetime import datetime
import logging

ign_latest_reviews_url = "https://www.ign.com/reviews/games"
header_mapping = {"User-Agent": "Mac Firefox"}

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_latest_reviews_from_ign():
    """
    Returns list of latest game review from IGN.
    "Latest" determined by games at reviews/games url,
    that are NOT board games.
    List will be an array of dictionary objects with a 'title' and 'href' key.

    """
    ign_latest_reviews_html = requests.get(
        ign_latest_reviews_url, headers=header_mapping
    )
    ign_latest_reivews_soup = BeautifulSoup(
        ign_latest_reviews_html.content, "html.parser"
    )
    latest_reviews_a_tag_list = ign_latest_reivews_soup.find(
        class_="main-content"
    ).find_all("a")

    filter_latest_reviews_a_tag = filter(
        lambda x: bool(x.get("aria-label")), latest_reviews_a_tag_list
    )

    filtered_a_tags = list(filter_latest_reviews_a_tag)

    mapped_latest_reviews = list(
        map(
            lambda x: {
                "title": x.get("aria-label")
                .split("Early Access")[0]
                .split("Final")[0]
                .split("Review")[0]
                .rstrip(),
                "href": x.get("href"),
            },
            filtered_a_tags,
        )
    )

    # filter out board games
    video_game_reviews = list(
        filter(lambda x: "board-game" not in x["href"], mapped_latest_reviews)
    )

    return video_game_reviews


def get_game_review_soup_from_ign(url):
    """
    Accepts a game review url and returns a string
    with the game review content.
    Catches error if request fails and returns None.

    Returns:
        A soup object with the game review content.
    """
    try:
        response = requests.get(url, headers=header_mapping)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logger.error(e)
        raise requests.exceptions.HTTPError(f"HTTP Request failed with url: {url}")
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


def parse_review_content_from_ign_article(soup):
    """
    Accepts a BeautifulSoup object scraped from an IGN game review article
    and returns a string with the game review content.

    """
    try:
        articles = soup.find_all("p")
        content = "".join(list(map(lambda x: x.get_text(), articles)))
        return content
    except Exception as e:
        logger.error(e)
        raise ValueError(
            f"Failed to parse html review content from IGN for soup: {soup}"
        )


def get_game_release_date_from_metacritic(game_title):
    """
    Accepts a game title and returns a datetime 'date' object. If error is thrown, return none.

    Returns:
        "date" of type 'datetime.date'.
    """
    try:
        game_title = (
            game_title.lower().replace(":", "").replace("'", "").replace(" ", "-")
        )
        response = requests.get(
            f"https://www.metacritic.com/game/{game_title}", headers=header_mapping
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logger.error(e)
        raise requests.exceptions.HTTPError(
            f"HTTP Request failed with url: https://www.metacritic.com/browse/games/{game_title}"
        )
    soup = BeautifulSoup(response.content, "html.parser")
    try:
        release_date = soup.find(
            lambda tag: tag.name == "span"
            and tag.has_attr("class")
            and tag["class"] == ["u-text-uppercase"]
        ).text
        release_date = datetime.strptime(release_date, "%b %d, %Y").date()
        return release_date
    except Exception as e:
        logger.error(e)
        raise ValueError(
            f"Failed to parse html content from metacritic for game title: {game_title}"
        )


def get_game_art_from_ign(game_title, game_page_url):
    """
    Accepts a Beautiful Soup object generated from the html of an IGN review page
    and returns a string with the game art.
    The soup object will have

    Returns:
        URL to image.
    """
    try:
        response = requests.get(
            f"https://www.ign.com{game_page_url}", headers=header_mapping
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logger.error(e)
        raise requests.exceptions.HTTPError(
            f"HTTP Request failed with url: https://www.ign.com{game_page_url}"
        )
    soup = BeautifulSoup(response.content, "html.parser")
    try:
        artwork_url = soup.find(class_="progressive-image").get("src")
        return artwork_url
    except Exception as e:
        logger.error(e)
        raise ValueError(
            f"Failed to parse artwork from ign for game title: {game_title}"
        )
