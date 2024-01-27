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

    def write_item(self, release_date_game_title, game_art_url):
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
                    "GameArtURL": {"S": game_art_url},
                },
                ConditionExpression="attribute_not_exists(SortByReleaseDate)",
            )
            return response
        except botocore.exceptions.ClientError as error:
            if error.response["Error"]["Code"] == "ConditionalCheckFailedException":
                print(f"Item already exists {release_date_game_title}")
            return error.response


class Reviews:
    """
    Class for querying the Reviews DynamoDB table.
    """

    def __init__(self):
        self.dynamodb_client = boto3.client("dynamodb")

    def get_review_by_game_title_and_reviewer_name(
        self, game_title, review_publisher_name
    ):
        """
        Returns a single review for a given game title and reviewer name.

        If no review exists, returns None
        """
        response = self.dynamodb_client.query(
            TableName="Reviews",
            KeyConditionExpression="GameTitle = :val1 AND ReviewPublisherName = :val2",
            ExpressionAttributeValues={
                ":val1": {"S": game_title},
                ":val2": {"S": review_publisher_name},
            },
        )
        return response["Items"][0] if len(response["Items"]) != 0 else None

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
                ConditionExpression="attribute_not_exists(GameTitle)",
            )
            return response
        except botocore.exceptions.ClientError as error:
            if error.response["Error"]["Code"] == "ConditionalCheckFailedException":
                print(
                    f"Item already exists with title {game_title} and reviewer {review_publisher_name}"
                )
            return error.response
