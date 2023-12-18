from dotenv import load_dotenv
import os
import requests

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
        print(type(release_date_id))
        release_date_epoch = requests.post(
            f"{self.base_url}/release_dates",
            headers=self.headers,
            data=f"fields date; where id = {release_date_id};",
        )

        return release_date_epoch.json()[0]["date"]

    def __get_release_date_id_by_title(self, title):
        """
        Returns the IGDB release data id from the associated game title.

        """
        release_date_id = requests.post(
            f"{self.base_url}/games",
            headers=self.headers,
            data=f'fields name, genres, platforms, release_dates; where name = "{title}";',
        )
        return release_date_id.json()[0]["release_dates"][0]
