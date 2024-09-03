import os
import requests
from dotenv import load_dotenv

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
            'field_list': 'name,image'
        }

        try:
            response = requests.get(self.base_url, params=params, headers={"User-Agent": "Mac Firefox"})
            response.raise_for_status()
            data = response.json()

            if data['error'] != 'OK':
                raise requests.exceptions.HTTPError(f"API Error: {data['error']}")

            for game in data['results']:
                if game['name'].lower() == game_title.lower():
                    return game['image']['original_url']

            return None

        except requests.exceptions.HTTPError  as e:
            raise Exception(f"Request failed due to API error: {str(e)}")
        except (KeyError, ValueError) as e:
            raise Exception(f"Error parsing API response: {str(e)}")