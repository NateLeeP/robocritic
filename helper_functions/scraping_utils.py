import requests
from bs4 import BeautifulSoup
from datetime import datetime

ign_latest_reviews_url = "https://www.ign.com/reviews/games"
header_mapping = {"User-Agent": "Mac Firefox"}


def get_latest_reviews_from_ign():
    """
    Returns list of latest game review from IGN.
    Returns the 10 latest reviews.
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
                "title": x.get("aria-label").rstrip("Review").rstrip(),
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


def get_game_review_content_from_ign(url):
    """
    Accepts a game review url and returns a string
    with the game review content.
    Catches error if request fails and returns None.

    Returns:
        "content" of type 'str'.
    """
    try:
        response = requests.get(url, headers=header_mapping)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        print(f"Request failed with url: {url}")
        return None
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("p")
    content = "".join(list(map(lambda x: x.get_text(), articles)))
    return content


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
        print(e)
        raise requests.exceptions.HTTPError(
            f"Request failed with url: https://www.metacritic.com/browse/games/{game_title}"
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
        print(e)
        raise ValueError(
            f"Failed to parse html content from metacritic for game title: {game_title}"
        )
