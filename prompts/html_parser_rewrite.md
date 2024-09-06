## Instructions for re-writing HTML parser class


You are a software developer refactoring an HTML parser class. You need to make the base HTML parser class an abstract class that has abstract methods that child classes must implement. Here are the methods a child class must implement: 

get_review_text()
get_game_title()
get_critic_score()
get_reviewer_name()
get_reviewer_bio_url()

Additionally, write a function that accepts a string argument and returns an instance of the requested child class (for example, 'pcgamer' should return a PCGamerReviewsParser object).

Please review the 'helper_functions.html_parser.pcgamer.py' file to see the current implementation of the PCGamerReviewewsParser object. Re-write the class so that it inherits from an abstract base class. 


