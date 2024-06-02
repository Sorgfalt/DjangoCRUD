from board.repositories.board_repository import BoardRepository


class BoardService:
    @staticmethod
    def create_board(data):
        return BoardRepository.create_board(data)

    @staticmethod
    def select_board_list():
        return BoardRepository.select_board_list()
