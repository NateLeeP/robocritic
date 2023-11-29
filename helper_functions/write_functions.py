# Ideally have a class. For now individual functions
# for each write.
from mysql.connector import Error


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
    except Error as e:
        print(f"The error '{e}' occurred")
