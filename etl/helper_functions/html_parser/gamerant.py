from .base import AbstractHTMLParser


class GameRantGameReviewParser(AbstractHTMLParser):
    def __init__(self, html_content: str):
        super().__init__(html_content)  
    
    def get_review_text(self):
        article_body = self.soup.find('section', class_='article-body')
        p_tags = article_body.find_all('p')
        filtered_p_text = [tag.text for tag in p_tags if tag.get('class') is None]
        review_text = ' '.join(filtered_p_text)
        review_text = review_text.replace(r"\'s", r"'s")
        return review_text if review_text else None

    def get_game_title(self):
        title_tag = self.soup.find('h1', class_='article-header-title')
        if title_tag:
            title = title_tag.text.split('Review')[0].strip()
            title = title.replace('Early Access', '')
            return title
        else:
            return None

    def get_critic_score(self):
        critic_score_tag = self.soup.find('div', class_='w-rating')
        try:
            critic_score_tag = critic_score_tag.find('div', class_='rate-number')
            critic_score = critic_score_tag.text.split('/')[0] if critic_score_tag else None
        except:
            critic_score = None
        return critic_score

    def get_reviewer_name(self):
        reviewer_name_tag = self.soup.find('a', class_='article-author')
        return reviewer_name_tag.text.strip() if reviewer_name_tag else None

    def get_reviewer_bio_url(self):
        reviewer_bio_tag = self.soup.find('a', class_='article-author')
        return "https://gamerant.com" + reviewer_bio_tag['href'] if reviewer_bio_tag else None
