from .base import AbstractHTMLParser
import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class IGNGameReviewParser(AbstractHTMLParser):
    def get_review_text(self):
        try:
            articles = self.soup.find_all("p")
            content = "".join(list(map(lambda x: x.get_text(), articles)))
            return content if len(content) > 0 else None
        except Exception as e:
            logger.error(f"Error getting review text: {e}")
            return None

    def get_game_title(self):
        try:
            title = self.soup.find("h1").get_text()
            # Remove "Review" and other unnecessary text from the title
            title = title.split("Early Access")[0].split("Final")[0].split("Review")[0].strip()
            return title if len(title) > 0 else None
        except AttributeError as e:
            logger.error(f"AttributeError {e} in soup traversal for game title")
            return None

    def get_reviewer_name(self):
        try:
            author_tag = self.soup.find('a', class_=['article-author'])
            author_name = author_tag.get_text() if author_tag else None
            return author_name
        except AttributeError as e:
            logger.error(f"AttributeError {e} in IGN soup traversal for reviewer name")
            return None
        except Exception as e:
            logger.error(f"Error getting IGN reviewer name: {e}")
            return None

    def get_reviewer_bio_url(self):
        try:
            author_tag = self.soup.find('a', class_=['article-author'])            
            bio_url = "https://www.ign.com" + author_tag['href'] if author_tag else None
            return bio_url
        except AttributeError as e:
            logger.error(f"AttributeError {e} in IGN soup traversal for reviewer bio URL")
            return None
        except Exception as e:
            logger.error(f"Error getting IGN reviewer bio URL: {e}")
            return None

    def get_critic_score(self):
        try:
            score_tag = self.soup.find('span', "hexagon-content-wrapper")
            score = score_tag.get_text()if score_tag else None
            return int(float(score)) if score else None
        except AttributeError as e:
            logger.error(f"AttributeError {e} in soup traversal for IGN critic score")
            return None
        except Exception as e:
            logger.error(f"Error getting IGN critic score: {e}")
            return None

    def get_game_artwork_url(self):
        try:
            artwork_tag = self.soup.find(class_="progressive-image")
            artwork_url = artwork_tag.get("src") if artwork_tag else None
            return artwork_url
        except AttributeError as e:
            logger.error(f"AttributeError {e} in soup traversal for game artwork URL")
            return None
        except Exception as e:
            logger.error(f"Error getting game artwork URL: {e}")
            return None