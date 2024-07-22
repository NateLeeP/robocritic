import requests
from bs4 import BeautifulSoup
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
import os
def extract_video_game_review_urls(url):
    # Send a GET request to the page
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the anchor tags with the class "article-link"
    review_links = soup.find_all('a', class_='article-link')

    # Filter out hardware reviews by checking if the "/games" path is present in the URL
    video_game_review_urls = [link['href'] for link in review_links if '/games' in link['href']]

    return video_game_review_urls

def scrape_review_text(url):
    # Send a GET request to the page
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the paragraph tags
    paragraphs = soup.find('div', id='article-body').find_all('p', recursive=False)

    # Extract the text content from each paragraph
    text_content = [paragraph.get_text() for paragraph in paragraphs]

    # Combine the text content into one string
    combined_text = ' '.join(text_content)

    return combined_text

def extract_game_title(url):
    # Send a GET request to the page
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the 'h1' tag with class 'review-title-long'
    title_tag = soup.find('h1', class_='review-title-long')

    # Extract the text content from the title tag
    game_title = title_tag.get_text()

    # Remove the word "review" from the end of the game title
    game_title = game_title.replace("review", "").strip()

    return game_title

def insert_game(title, release_date, art_url="https://shorturl.at/RKbAj"):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host='127.0.0.1',  # e.g., 'localhost'
            user='root',
            password=os.environ['MYSQL_ROOT_PASSWORD'],
            database=os.environ['MYSQL_DATABASE'],
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # SQL query to insert a new game
            sql_insert_query = """
            INSERT INTO game (title, release_date, art_url) 
            VALUES (%s, %s, %s)
            """
            # Tuple of values to be inserted
            values = (title, release_date, art_url)
            
            # Execute the SQL query
            cursor.execute(sql_insert_query, values)
            # Commit the transaction
            connection.commit()
            print("Game inserted successfully")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
