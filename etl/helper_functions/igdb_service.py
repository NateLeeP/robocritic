from dotenv import load_dotenv
import os
import requests
from datetime import datetime
import logging

load_dotenv()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class IGDBService:
    def __init__(self):
        self.base_url = "https://api.igdb.com/v4"
        self.headers = {
            "Authorization": f"Bearer {os.environ['IGDB_BEARER_TOKEN']}",
            "Client-ID": os.environ["IGDB_CLIENT_ID"],
        }
        self.reviewable_platforms = set(['PlayStation 5', 'PlayStation 4', 'Xbox Series X|S', 'Xbox One', 'Nintendo Switch', 'PC (Microsoft Windows)'])

    def get_first_release_date_by_title(self, title):
        """
        Returns the IGDB release data id from the associated game title.
        Returns the last release date in array.
        Returning the first release date resulted in beta / demo release dates
        being returned.
        Returns datetime 'date' object.
        """
        try:
            # Replace apostrophes with standard apostrophe
            title = title.replace("\u2019", "'")
            request_data = (
                f'search "{title}"; fields name, platforms.name, first_release_date;'
            )
            response = requests.post(
                f"{self.base_url}/games",
                headers=self.headers,
                data=request_data,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(e)
            logger.error(f"IGDB API Request failed with data: {request_data}")
            raise requests.exceptions.HTTPError(f"IGDB API Request failed")
        games = response.json()
        games_with_release_date = [
            game for game in games if "first_release_date" in game
        ]
        if not games_with_release_date:
            raise ValueError(f"No game found for title '{title}'")
        sorted_games = sorted(
            games_with_release_date, key=lambda x: x["id"], reverse=True
        )
        game = sorted_games[0]
        release_date_unix = game.get("first_release_date")
        platforms = [platform.get('name') for platform in game.get('platforms', [])]
        platforms = [platform for platform in platforms if platform in self.reviewable_platforms]
        if not release_date_unix:
            raise ValueError(f"No first release date found for title '{title}'")
        if not platforms:
            raise ValueError(f"No reviewable platforms found for title '{title}'")
        release_date = datetime.fromtimestamp(release_date_unix).date()

        return release_date, platforms