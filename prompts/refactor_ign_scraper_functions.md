## Refactor IGN Scraper Functions

### Prompt  

You are a software developer working on refactoring scraper functions for the IGN website. The current functions are available in 'helper_functions/scraping_utils.py'. Your task is to extract the relevant parts of the function and place them in a new 'IGNGameReviewParser' class. The class should be in a new file 'helper_functions/html_parser/ign.py'.

For an example of how to implement the class, see the PCGamerGameReviewParser class in 'helper_functions/html_parser/pcgamer.py'. Ensure that the new ign class inherits from the AbstractHTMLParser class in 'helper_functions/html_parser/base.py'.

