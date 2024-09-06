from .base import AbstractHTMLParser
import re
import logging
from abc import ABC, abstractmethod

logger = logging.getLogger()
logger.setLevel(logging.INFO)



class PCGamerGameReviewParser(AbstractHTMLParser):
    def get_review_text(self):
        try:    
            # Find all the paragraph tags
            paragraphs = self.soup.find('div', id='article-body').find_all('p', recursive=False)

            # Extract the text content from each paragraph
            text_content = [paragraph.get_text() for paragraph in paragraphs]

            # Combine the text content into one string
            combined_text = ' '.join(text_content)

            return combined_text if len(combined_text) > 0 else None
        except AttributeError as e:
            logger.error(f"AttributeError {e} in soup traversal for review text")
            return None
        except Exception as e:
            logger.error(f"Error getting review text: {e}")
            return None

    def get_game_title(self):
        """
        Expected HTML content from PC Gamer game review page: 
        https://www.pcgamer.com/games/rpg/dungeons-of-hinterberg-review/
        
        """
        try:
            # Find the 'h1' tag with class 'review-title-long'
            title_tag = self.soup.find('h1', class_=re.compile('^review-title'))

            # Extract the text content from the title tag
            game_title = title_tag.get_text()

            # Remove the word "review" from the end of the game title
            game_title = game_title.replace("review", "").strip()
            return game_title if len(game_title) > 0 else None
        except AttributeError as e:
            logger.error(f"AttributeError {e} in soup traversal for game title:")
            return None

    def get_reviewer_name(self):
        try:
            author_tag = self.soup.find('span', class_="author-byline__author-name")

            author_name = author_tag.get_text() if author_tag else None

            return author_name
        except AttributeError as e:
            logger.error(f"AttributeError {e} in soup traversal for reviewer name")
            return None
        except Exception as e:
            logger.error(f"Error getting reviewer name: {e}")
            return None
    
    def get_reviewer_bio_url(self):

        try:
            author_tag = self.soup.find('span', class_="author-byline__author-name")
            bio_tag = author_tag.find('a')
            bio_url = bio_tag['href']
            return bio_url if bio_url else None
        except AttributeError as e:
            logger.error(f"AttributeError {e} in soup traversal for reviewer bio URL")
            return None
        except Exception as e:
            logger.error(f"Error getting reviewer bio URL: {e}")
            return None
    
    def get_critic_score(self):
        try:
            critic_score_tag = self.soup.find('div', class_="score-area")
            critic_score = critic_score_tag.span.get_text() if critic_score_tag else None
            return int(critic_score) if critic_score else None
        except AttributeError as e:
            logger.error(f"AttributeError {e} in soup traversal for critic score")
            return None
        except Exception as e:
            logger.error(f"Error getting critic score: {e}")
            return None


