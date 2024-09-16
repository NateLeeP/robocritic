from .base import AbstractHTMLParser
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class GameSpotReviewParser(AbstractHTMLParser):
    def get_review_text(self):
        try:
            section_tag = self.soup.find('section', class_='article-body')
            p_tags = section_tag.find_all('p') if section_tag else []
            text_list = []
        
            for tag in p_tags:
                text_list.append(tag.get_text(strip=True))
        
            combined_text = ' '.join(text_list)
            return combined_text if combined_text else None
        except Exception as e:
            logger.error(f"Error getting review text for Gamespot review: {e}")
            return None

    def get_game_title(self):
        try:
            review_title = self.soup.find('h1', class_='kubrick-info__title').get_text(strip=True)
            index = review_title.find('Review')
            if index != -1:
                return review_title[:index].strip()
            return review_title if review_title else None
        except AttributeError as e:
            logger.error(f"AttributeError {e} in soup traversal for Gamespot game title")
            return None
        except Exception as e:
            logger.error(f"Error getting Gamespot game title: {e}")
            return None

    def get_reviewer_name(self):
        try:
            author_tag = self.soup.find('a', class_='byline-author__name')
            reviewer_name = author_tag.get_text(strip=True) if author_tag else None
            return reviewer_name
        except AttributeError as e:
            logger.error(f"AttributeError {e} in soup traversal for Gamespot reviewer name")
            return None
        except Exception as e:
            logger.error(f"Error getting Gamespot reviewer name: {e}")
            return None

    def get_reviewer_bio_url(self):
        try:
            author_tag = self.soup.find('a', class_='byline-author__name')
            reviewer_url = "https://www.gamespot.com" + author_tag.get('href') if author_tag else None
            return reviewer_url
        except AttributeError as e:
            logger.error(f"AttributeError {e} in soup traversal for Gamespot reviewer bio URL")
            return None
        except Exception as e:
            logger.error(f"Error getting Gamespot reviewer bio URL: {e}")
            return None

    def get_critic_score(self):
        try:
            critic_score_tag = self.soup.find('div', class_='review-ring-score__ring')
            score = critic_score_tag.get_text() if critic_score_tag else None
            return int(score) if score else None
        except AttributeError as e:
            logger.error(f"AttributeError {e} in soup traversal Gamespot for critic score")
            return None
        except Exception as e:
            logger.error(f"Error getting Gamespot critic score: {e}")
            return None

