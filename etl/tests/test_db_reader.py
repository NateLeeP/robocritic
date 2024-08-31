import unittest
from unittest.mock import patch, MagicMock
from helper_functions.db_reader import RobocriticDBReader

class TestRobocriticDBReader(unittest.TestCase):
    def setUp(self):
        self.mock_connection = MagicMock()
        self.db_reader = RobocriticDBReader(self.mock_connection)

    def test_get_game(self):
        # Mock the cursor object and its methods
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [{'id': 1, 'name': 'Test Game'}]
        self.mock_connection.cursor.return_value = mock_cursor

        # Execute the method
        result = self.db_reader.get_game(1)

        # Assert the result is equal, the correct function was called
        self.assertEqual(result, {'id': 1, 'name': 'Test Game'})
        mock_cursor.execute.assert_called_with("SELECT * FROM game WHERE id = %s", (1,))

    def test_get_review(self):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [{'id': 1, 'content': 'Test Review'}]
        self.mock_connection.cursor.return_value = mock_cursor

        result = self.db_reader.get_review(1)
        self.assertEqual(result, {'id': 1, 'content': 'Test Review'})
        mock_cursor.execute.assert_called_with("SELECT * FROM review WHERE id = %s", (1,))

    def test_get_reviewer(self):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [{'id': 1, 'name': 'Test Reviewer'}]
        self.mock_connection.cursor.return_value = mock_cursor

        result = self.db_reader.get_reviewer(1)
        self.assertEqual(result, {'id': 1, 'name': 'Test Reviewer'})
        mock_cursor.execute.assert_called_with("SELECT * FROM reviewer WHERE id = %s", (1,))

    def test_get_all_games(self):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [{'id': 1, 'name': 'Game 1'}, {'id': 2, 'name': 'Game 2'}]
        self.mock_connection.cursor.return_value = mock_cursor

        result = self.db_reader.get_all_games()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'Game 1')
        self.assertEqual(result[1]['name'], 'Game 2')
        mock_cursor.execute.assert_called_with("SELECT * FROM game")

    def test_get_reviews_by_game(self):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [{'id': 1, 'game_id': 1, 'content': 'Review 1'}]
        self.mock_connection.cursor.return_value = mock_cursor

        result = self.db_reader.get_reviews_by_game(1)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['content'], 'Review 1')
        mock_cursor.execute.assert_called_with("SELECT * FROM review WHERE game_id = %s", (1,))

    def test_get_reviews_by_reviewer(self):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [{'id': 1, 'reviewer_id': 1, 'content': 'Review 1'}]
        self.mock_connection.cursor.return_value = mock_cursor

        result = self.db_reader.get_reviews_by_reviewer(1)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['content'], 'Review 1')
        mock_cursor.execute.assert_called_with("SELECT * FROM review WHERE reviewer_id = %s", (1,))

if __name__ == '__main__':
    unittest.main()