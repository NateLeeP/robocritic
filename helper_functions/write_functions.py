# Ideally have a class. For now individual functions
# for each write.
from mysql.connector import Error


def create_game(connection, game):
    # Accepts a db connection and a game object.
    # Game is a dictionary with the following keys:
    # name, release_date. Relase date formate: YYYY-MM-DD
    create_game_query = "INSERT INTO game (title, release_date) VALUES (%s, %s)"
    cursor = connection.cursor()
    try:
        cursor.execute(
            create_game_query,
            (
                game["title"],
                game["release_date"],
            ),
        )
        connection.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"The error '{e}' occurred. Game failed to create")


def create_review(connection, review):
    # Accepts a db connection and a review object.
    # Review is a dictionary with the following keys:
    # url, game_id, publisher_id
    create_review_query = (
        "INSERT INTO review (url, game_id, publisher_id) VALUES (%s, %s, %s)"
    )
    cursor = connection.cursor()
    try:
        cursor.execute(
            create_review_query,
            (
                review["url"],
                review["game_id"],
                review["publisher_id"],
            ),
        )
        connection.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"The error '{e}' occurred. Review could not be created")


def write_review_pros_to_db(connection, list_of_pros):
    """
    Uses a db connection to write a list of pros to the database.

    list_of_pros: List of tuples with the first element being the review_id and the second element being the text.
    """
    # Accepts a db connection and a list of pros.
    # list_of_pros: List of strings
    create_pros_query = "INSERT INTO review_pro (review_id, text) VALUES (%s, %s)"
    cursor = connection.cursor()
    try:
        cursor.executemany(create_pros_query, list_of_pros)
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")


def write_review_cons_to_db(connection, list_of_cons):
    """
    Uses a db connection to write a list of cons to the database.

    list_of_cons: List of tuples with the first element being the review_id and the second element being the text.
    """
    # Accepts a db connection and a list of cons.
    # list_of_cons: List of strings
    create_cons_query = "INSERT INTO review_con (review_id, text) VALUES (%s, %s)"
    cursor = connection.cursor()
    try:
        cursor.executemany(create_cons_query, list_of_cons)
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")


def write_platform_to_db(connection, platform_name):
    """
    Uses a db connection to write a single platform to the database.

    platform: platform name to insert. Name will be Xbox One, Xbox X, PS5, etc.
    """
    platform_write_query = "INSERT INTO platform (platform_name) VALUES (%s)"
    cursor = connection.cursor()
    try:
        cursor.execute(platform_write_query, (platform_name,))
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")
