from django.shortcuts import get_object_or_404

from boardTest.models import BoardTest
import json


class BoardService:
    @staticmethod
    def create_board(data):
        # Parse the JSON string into a dictionary
        data_dict = json.loads(data)

        # Extract title and content from the data dictionary
        board = BoardTest.objects.create(**data_dict)

        # Save the Board object to the database
        return board.save()

    @staticmethod
    def select_board_list():
        queryset = BoardTest.objects.all()
        return queryset

    @classmethod
    def update_board(cls, board_id, data):
        # Parse the JSON string into a dictionary
        data_dict = json.loads(data)

        # Fetch the existing Board object
        board = get_object_or_404(BoardTest, pk=board_id)

        # Update the fields
        board.title = data_dict.get('title', board.title)
        board.content = data_dict.get('content', board.content)
        board.published_date = data_dict.get('published_date', board.published_date)

        # Save the Board object to the database
        return board.save()

    @classmethod
    def delete_board(cls, board_id):
        board = get_object_or_404(BoardTest, pk=board_id)

        return board.delete()


