from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()


class IGDBService:
    def __init__(self, connection):
        self.connection = connection
        self.base_url = "https://api.igdb.com/v4"
        self.headers = {
            "Authorization": f"Bearer {os.getenv('IGDB_BEARER_TOKEN')}",
            "Client-ID": os.getenv("IGDB_CLIENT_ID"),
        }

    def get_game_release_date_by_title(self, title):
        """
        Returns the release date as a datetime date object
        from the associated game title.
        """
        try:
            release_date_id = self.get_release_date_id_by_title(title)
        except ValueError as e:
            print(e)
            return None
        try:
            request_data = f"fields date; where id = {release_date_id};"
            response = requests.post(
                f"{self.base_url}/release_dates",
                headers=self.headers,
                data=request_data,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(e)
            print(f"Request failed with data: {request_data}")
            return None

        if not response.json():
            raise ValueError(f"No release date found with title '{title}'")
        unix_time = response.json()[0]["date"]
        release_date = datetime.utcfromtimestamp(unix_time)
        return release_date.date()

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
            print(e)
            print(f"IGDB API Request failed with data: {request_data}")
            raise requests.exceptions.HTTPError(f"IGDB API Request failed")
        if not response.json():
            # Will raise an error for empty response
            raise ValueError(f"No game found with title '{title}'")
        game = response.json()[0]
        try:
            release_date_unix = game["first_release_date"]
            release_date = datetime.utcfromtimestamp(release_date_unix).date()
            return release_date
        except KeyError as e:
            print(e)
            raise ValueError(f"No release date found with title '{title}'")
