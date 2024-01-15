from mysql.connector import Error
import boto3
import botocore


class GameReleaseDate:
    """
    Class for querying the GameRleaseDate DynamoDB table.
    """

    def __init__(self):
        self.dynamodb_client = boto3.client("dynamodb")

    def get_recent_games(self, limit=10):
        """Return the most recent games. Limit return with passed 'limit' argument"""
        response = self.dynamodb_client.query(
            TableName="GamesReleaseDate",
            KeyConditionExpression="SortByReleaseDate = :val",
            ExpressionAttributeValues={":val": {"N": "1"}},
            ScanIndexForward=False,
            Limit=limit,
        )
        return response["Items"]

    def write_item(self, release_date_game_title):
        """
        Writes a new item to the GameRleaseDate DynamoDB table.

        release_date_game_title: a string with format 'YYYY-MM-DD_{game_title}'
        Returns HTTP response object returned by AWS.
        """
        try:
            response = self.dynamodb_client.put_item(
                TableName="GamesReleaseDate",
                Item={
                    "SortByReleaseDate": {"N": "1"},
                    "ReleaseDate_GameTitle": {"S": release_date_game_title},
                },
                ConditionExpression="attribute_not_exists(SortByReleaseDate)",
            )
            return response
        except botocore.exceptions.ClientError as error:
            if error.response["Error"]["Code"] == "ConditionalCheckFailedException":
                print("Item already exists")
            return error.response


class Reviews:
    """
    Class for querying the Reviews DynamoDB table.
    """

    def __init__(self):
        self.dynamodb_client = boto3.client("dynamodb")

    def get_all_reviews_by_game_title(self, game_title):
        """
        Return all reviews for a given game title.
        """
        response = self.dynamodb_client.query(
            TableName="Reviews",
            KeyConditionExpression="GameTitle = :val",
            ExpressionAttributeValues={":val": {"S": game_title}},
            ScanIndexForward=False,
        )
        return response["Items"]

    def create_reviews_table_item(
        self,
        game_title,
        review_publisher_name,
        release_date,
        list_of_pros,
        list_of_cons,
        roboscore,
    ):
        """
        Create an DynamoDB table item for insertion into 'Reviews' table.
        Lists should be a list of dictionary with key value pair of
        'S' for string then the string value.
        """
        item = {
            "GameTitle": {"S": game_title},
            "ReviewPublisherName": {"S": review_publisher_name},
            "GameReleaseDate": {"S": release_date},
            "Pros": {"L": list_of_pros},
            "Cons": {"L": list_of_cons},
            "RoboScore": {"N": roboscore},
        }
        return item

    def write_item(
        self,
        game_title,
        review_publisher_name,
        game_release_date,
        list_of_pros,
        list_of_cons,
        roboscore,
    ):
        """
        Writes a new item to the Reviews DynamoDB table.
        Returns HTTP response object returned by AWS.
        """
        try:
            response = self.dynamodb_client.put_item(
                TableName="Reviews",
                Item=self.create_reviews_table_item(
                    game_title,
                    review_publisher_name,
                    game_release_date,
                    list(map(lambda x: {"S": x}, list_of_pros)),
                    list(map(lambda x: {"S": x}, list_of_cons)),
                    str(roboscore),
                ),
            )
            return response
        except botocore.exceptions.ClientError as error:
            print(f"The error '{error.response['Error']['Message']}' occurred")
            return error.response


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
