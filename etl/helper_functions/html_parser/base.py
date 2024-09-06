import logging
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class AbstractHTMLParser(ABC):
    def __init__(self, html_content):
        self.html_content = html_content
        self.soup = BeautifulSoup(self.html_content, 'html.parser')

    def _create_soup(self):
        # Implement the BeautifulSoup creation logic here
        pass

    @abstractmethod
    def get_review_text(self):
        pass

    @abstractmethod
    def get_game_title(self):
        pass

    @abstractmethod
    def get_critic_score(self):
        pass

    @abstractmethod
    def get_reviewer_name(self):
        pass

    @abstractmethod
    def get_reviewer_bio_url(self):
        pass


