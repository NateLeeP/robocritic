import os
import dotenv
import requests

dotenv.load_dotenv()

class YoutubeApi:
    def __init__(self):
        self.base_url = "https://www.googleapis.com/youtube/v3/search"
        self.api_key = os.getenv("YOUTUBE_API_KEY")
    def search_for_gameplay_videos(self, game_title):
        response = requests.get('https://youtube.googleapis.com/youtube/v3/search',
                                params={
                                    'key': self.api_key,
                                    'q': game_title + ' gameplay walkthrough no commentary',
                                    'part': 'snippet',
                                    'type': 'video',
                                    'maxResults': 1
                                })
        if response.status_code != 200:
            error_message = response.json()['error']['message']
            raise requests.exceptions.HTTPError(
                f'''Error getting youtube gameplay url for {game_title}: 
                {response.status_code}. Response: {error_message}'''
            )
        videos = response.json()['items']
        if not videos:
            return None
        # return the first video id. 
        return 'https://www.youtube.com/embed/' + videos[0]['id']['videoId']

