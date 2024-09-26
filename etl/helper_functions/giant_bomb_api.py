import os
import requests
from dotenv import load_dotenv
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class GiantBombAPI:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('GIANT_BOMB_API_KEY')
        self.base_url = 'https://www.giantbomb.com/api/games/'

    def get_game_artwork(self, game_title):
        params = {
            'api_key': self.api_key,
            'format': 'json',
            'filter': f'name:{game_title}',
            'field_list': 'name,image',
            'limit': 1,
            'sort': 'original_release_date:desc'
        }

        try:
            response = requests.get(self.base_url, params=params, headers={"User-Agent": "Mac Firefox"})
            response.raise_for_status()
            data = response.json()

            if data['error'] != 'OK':
                raise requests.exceptions.HTTPError(f"API Error: {data['error']}")

            most_recent_game = data['results'][0] 
            return most_recent_game['image']['original_url']

        except requests.exceptions.HTTPError  as e:
            logger.error(f"Giant Bomb API Request failed due to API error: {str(e)}")
        except (KeyError, TypeError) as e:
            logger.error(f"Giant Bomb API Error parsing API response: {str(e)}")