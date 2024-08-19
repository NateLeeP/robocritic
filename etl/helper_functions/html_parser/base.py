from bs4 import BeautifulSoup


class HTMLParser():
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')
    

