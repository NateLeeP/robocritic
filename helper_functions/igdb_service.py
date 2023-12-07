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
        release_date_epoch = requests.post(
            f"{self.base_url}/games",
            headers=self.headers,
            data='fields name, genres, platforms, release_dates; where name = "Avatar: Frontiers of Pandora";',
        )
        return release_date_epoch.json()[0]["release_dates"][0]
