import requests
from bs4 import BeautifulSoup

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

    return mapped_latest_reviews


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
