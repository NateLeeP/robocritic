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

    def get_first_release_date_by_title(self, title):
        """
        Returns the IGDB release data id from the associated game title.
        Returns the last release date in array.
        Returning the first release date resulted in beta / demo release dates
        being returned.
        Returns datetime 'date' object.
        """
        try:
            request_data = (
                f'search "{title}"; fields name, genres, platforms, first_release_date;'
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
        if not response.json():
            # Will raise an error for empty response
            raise ValueError(f"No game found from IGDB API with title '{title}'")

        games = sorted(response.json(), key=lambda x: x["id"], reverse=True)
        game = games[0]
        try:
            release_date_unix = game["first_release_date"]
            release_date = datetime.utcfromtimestamp(release_date_unix).date()
            return release_date
        except KeyError as e:
            logger.error(e)
            raise ValueError(f"No release date found with title '{title}'")
