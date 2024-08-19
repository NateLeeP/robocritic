from .base import HTMLParser
import re

class PCGamerReviewsParser(HTMLParser):
    def __init__(self, html_content):
        """
        Initializes the PCGamerParser class with the provided HTML content.
 
        Args:
            html_content (str): The HTML content to be parsed.
        
        """
        super().__init__(html_content)
    
    def get_video_game_review_urls(self):
        """
        Expected HTML content from PC Gamer reviews page: 
        https://www.pcgamer.com/reviews/
        
        """

        # Find all the anchor tags with the class "article-link"
        review_links = self.soup.find_all('a', class_='article-link')

        # Filter out hardware reviews by checking if the "/games" path is present in the URL
        video_game_review_urls = [link['href'] for link in review_links if '/games' in link['href']]

        return video_game_review_urls

class PCGamerGameReviewParser(HTMLParser):
    def __init__(self, html_content):
        """
        Initializes the PCGamerGameReviewParser class with the provided HTML content.
        Expected HTML content from PC Gamer game review page: 
        https://www.pcgamer.com/games/rpg/dungeons-of-hinterberg-review/

        Args:
            html_content (str): The HTML content to be parsed.
        
        """
        super().__init__(html_content)
    def get_review_text(self):

        # Find all the paragraph tags
        paragraphs = self.soup.find('div', id='article-body').find_all('p', recursive=False)

        # Extract the text content from each paragraph
        text_content = [paragraph.get_text() for paragraph in paragraphs]

        # Combine the text content into one string
        combined_text = ' '.join(text_content)

        return combined_text if len(combined_text) > 0 else None

    def get_game_title(self):
        """
        Expected HTML content from PC Gamer game review page: 
        https://www.pcgamer.com/games/rpg/dungeons-of-hinterberg-review/
        
        """
        # Find the 'h1' tag with class 'review-title-long'
        title_tag = self.soup.find('h1', class_=re.compile('^review-title'))

        # Extract the text content from the title tag
        game_title = title_tag.get_text()

        # Remove the word "review" from the end of the game title
        game_title = game_title.replace("review", "").strip()

        return game_title if len(game_title) > 0 else None

    def get_reviewer_name(self):
        author_tag = self.soup.find('span', class_="author-byline__author-name")

        author_name = author_tag.get_text() if author_tag else None

        return author_name
    
    def get_reviewer_bio_url(self):

        try:
            author_tag = self.soup.find('span', class_="author-byline__author-name")
            bio_tag = author_tag.find('a')
            bio_url = bio_tag['href']
            return bio_url
        except Exception as e:
            return None


