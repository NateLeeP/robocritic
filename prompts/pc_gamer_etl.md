# PC Gamer ETL Instructions

## Overview

You are a software engineer working on an ETL pipeline for a video game review website. Your task is to extract the relevant data from the PC Gamer website, transform it, and load it into a database.

## Instructions

1. **Extract the HTML content from the PC Gamer website:**
   - Use the provided URL to fetch the HTML content of the PC Gamer website.
   - Parse the HTML content to extract the video game review URLs.
   - Use the PCGamerReviewsParser class from 'html_parser/pcgamer.py' to parse the HTML content.

2. **Extract the review text and game title from each review page:**
   - For each review URL, fetch the HTML content.
   - Parse the HTML content to extract the review text, game title. reviewer name and reviewer bio
   - Use the PCGamerGameReviewParser class from 'html_parser/pcgamer.py' to parse the HTML content.

3. **Check if the game is already in the database:**
   - Use the RobocriticDBReader class from 'db_reader.py' to check if the game is already in the database.
   - If the game is not in the database, insert the game into the database.
   - You will need the game title, release_date, and art_url to insert the game into the database.
   - To get the release date, use the class IGDBService from 'igdb_service.py' to get the release date. 
   - Use a placeholder value for the art_url. 
   - You will also need to write to the 'platform' and 'platform_game' tables in the database.
   - Use the IDGDBService class from 'igdb_service.py' to get the platform name. Query the 'platform' table based on the platform name to get the platform id. 
   - Insert the platform id and the game id (the game id will correspond the written game) into the 'platform_game' table. 
   - The game may be on multiple platforms. You will need to account for this. 
   - If the game is in the database, move onto the next step of the ETL

4. **Insert the review into the database:**
   - Use the RobocriticDBReader class from 'db_reader.py' to check if the review is already in the database. To check if the review is in the database, query the 'review' table in the database based on game id and publisher id. The 'game id' can be found by querying the 'game' table in the database based on game title. The 'publisher id' can be found by querying the 'publisher' table in the database based on publisher name. For this etl, the publisher name is 'PC Gamer'.
   - If the review is not in the database, insert the review into the database.
   - If the review is in the database, move onto the next step of the ETL

5. **Inserting a review into the database:**
    - You will need the review_url, robo_score, critic_score, reviewer_id, game_id, and publisher_id to insert the review into the database. 
    - To get the 'robo_score', use the OpenAIService class from 'openai_service.py' to get the robo_score.
    - The review_url is the URL of the review being processed. 
    - To get the 'reviewer_id', you will need to query the 'reviewer' table in the database based on the reviewer name. If the reviewer name is not in the 'reviewer' table, insert the reviewer name into the 'reviewer' table and get the reviewer id. The reviewer table has a 'reviever_full_name' a 'publisher_id' and a 'reviewer_bio_url'. The 'reviewer_bio_url' can be null. Use the 'PCGamerReviewerParser' class from 'html_parser/pcgamer.py' to get the reviewer name and reviewer_bio_url.
    - The 'game_id' is the game id of the game being reviewed.
    - The 'publisher_id' is the publisher id of the publisher that is publishing the review. For this etl, the publisher name is 'PC Gamer'.
    - The 'critic_score' is the critic score of the review. Use the 'PCGamerGameReviewParser' class from 'html_parser/pcgamer.py' to get the critic score.

6. **Inserting pros and cons into the database:**
    - Using the OpenAIService class from 'openai_service.py', get the pros and cons of the game review. Pass into the OpenAIService class 'extract_review_pros_and_cons' method the review content. 
    - The method will return a JSON with the fields 'pros' and 'cons'. 
    - Insert the pros into the 'review_pro' table and the cons into the 'review_con' table. 
    - The review_pro table has a 'pros' VARCHAR column to store the pros. It also requires the review id. 
    - The review_con table has a 'cons' VARCHAR column to store the cons. It also requires the review id. 

Include proper error handling. Please write the ETL into the file 'etl/gamer_etl.py'