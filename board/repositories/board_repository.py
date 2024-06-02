from drf_yasg.openapi import Response

from board.models import Board
import json

from board.serializer import BoardSerializer


class BoardRepository:
    def create_board(data):
        # Parse the JSON string into a dictionary
        data_dict = json.loads(data)

        # Extract title and content from the data dictionary
        title = data_dict.get('title')
        content = data_dict.get('content')

        # Create a new Board object
        board = Board(title=title, content=content)

        # Save the Board object to the database
        return board.save()

    @staticmethod
    def select_board_list():
        queryset = Board.objects.all()
        for i in queryset:
            print(i, id)
            print (i.title)
            print (i.content)
        return queryset
