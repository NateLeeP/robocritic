from bs4 import BeautifulSoup
from .base import AbstractHTMLParser

class EurogamerGameReviewParser(AbstractHTMLParser):
    def __init__(self, html_content):
        super().__init__(html_content)
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def get_review_text(self):
        article_body = self.soup.find('div', class_='article_body_content')
        if not article_body:
            return None
        
        paragraphs = article_body.find_all('p')
        return ' '.join(p.get_text().strip() for p in paragraphs)

    def get_game_title(self):
        title_element = self.soup.find('h1', class_='title')
        if title_element:
            # Remove "Review" from the end of the title if present
            title = title_element.get_text().strip()
            if " review - " in title.lower():
                title = title.split(" review - ")[0]
            return title.replace(" Review", "").strip()
        return None

    def get_critic_score(self):
        rating_div = self.soup.find('div', class_='review_rating')
        if rating_div and 'data-value' in rating_div.attrs:
            try:
                return float(rating_div['data-value'])
            except (ValueError, TypeError):
                return None
        return None

    def get_reviewer_name(self):
        byline = self.soup.find('span', class_='author')
        if byline:
            return byline.get_text().strip()
        return None

    def get_reviewer_bio_url(self):
        byline_link = self.soup.find('span', class_='author')
        if byline_link:
            anchor_tag = byline_link.find('a')
            if anchor_tag and 'href' in anchor_tag.attrs:
                return anchor_tag['href']
        return None