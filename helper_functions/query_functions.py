from mysql.connector import Error


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def get_publisher_by_id(connection, id):
    """
    Return the publisher with given id
    """
    cursor = connection.cursor()
    query = "SELECT * FROM publisher WHERE id = %s"
    publisher = None
    try:
        cursor.execute(query, (id,))
        publisher = cursor.fetchone()
    except Error as e:
        print(f"The error '{e}' occurred")

    return publisher


def get_game_by_title(connection, title):
    """
    Return the game with given title
    """
    cursor = connection.cursor()
    query = "SELECT * FROM game WHERE title = %s"
    game = None
    try:
        cursor.execute(query, (title,))
        game = cursor.fetchone()
    except Error as e:
        print(f"The error '{e}' occurred")

    return game


def get_review_by_game_id_and_publisher_id(connection, game_id, publisher_id):
    """
    Return the review with given game_id and publisher id
    """
    cursor = connection.cursor()
    query = "SELECT * FROM review WHERE game_id = %s AND publisher_id = %s"
    review = None
    try:
        cursor.execute(query, (game_id, publisher_id))
        review = cursor.fetchone()
    except Error as e:
        print(f"The error '{e}' occurred")

    return review
