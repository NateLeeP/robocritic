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
        release_date_id = self.__get_release_date_id_by_title(title)
        release_date_epoch = requests.post(
            f"{self.base_url}/release_dates",
            headers=self.headers,
            data=f"fields date; where id = {release_date_id};",
        )

        unix_time = release_date_epoch.json()[0]["date"]
        release_date = datetime.utcfromtimestamp(unix_time)
        return release_date.date()

    def __get_release_date_id_by_title(self, title):
        """
        Returns the IGDB release data id from the associated game title.
        Returns the last release date in array.
        Returning the first release date resulted in beta / demo release dates
        being returned.
        """
        release_date_id = requests.post(
            f"{self.base_url}/games",
            headers=self.headers,
            data=f'fields name, genres, platforms, release_dates; where name = "{title}";',
        )
        return release_date_id.json()[0]["release_dates"][-1]
