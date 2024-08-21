import pytest
from unittest.mock import patch, Mock
from datetime import datetime
import requests

# Import the IGDBService class
from helper_functions.igdb_service import IGDBService


# Fixtures to set up the IGDBService instance
@pytest.fixture
def igdb_service():
    return IGDBService()


def test_get_first_release_date_by_title_no_games_found(igdb_service):
    # Mock the requests.post to return an empty list
    with patch("requests.post") as mock_post:
        mock_post.return_value = Mock(status_code=200, json=lambda: [])

        with pytest.raises(ValueError) as exc_info:
            igdb_service.get_first_release_date_by_title("Non-existent Game")

        assert (
            str(exc_info.value)
            == "No game with release date found for title 'Non-existent Game'"
        )


def test_get_first_release_date_by_title_no_release_date(igdb_service):
    # Mock the requests.post to return a game with no first_release_date
    with patch("requests.post") as mock_post:
        mock_post.return_value = Mock(
            status_code=200,
            json=lambda: [{"id": 1, "name": "Game without release date"}],
        )

        with pytest.raises(ValueError) as exc_info:
            igdb_service.get_first_release_date_by_title("Game without release date")

        assert (
            str(exc_info.value)
            == "No game with release date found for title 'Game without release date'"
        )


def test_get_first_release_date_by_title_http_error(igdb_service):
    # Mock the requests.post to raise an HTTPError
    with patch("requests.post") as mock_post:
        mock_post.side_effect = requests.exceptions.HTTPError("API Request failed")

        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            igdb_service.get_first_release_date_by_title("Some Game")

        assert str(exc_info.value) == "IGDB API Request failed"


def test_get_first_release_date_by_title_valid_case(igdb_service):
    # Mock the requests.post to return a valid game with a release date
    with patch("requests.post") as mock_post:
        mock_post.return_value = Mock(
            status_code=200,
            json=lambda: [
                {"id": 1, "name": "Valid Game", "first_release_date": 1609459200}
            ],
        )

        release_date = igdb_service.get_first_release_date_by_title("Valid Game")
        assert release_date == datetime.utcfromtimestamp(1609459200).date()
