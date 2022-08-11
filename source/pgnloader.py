import chess.pgn as pgnlib
import pathlib


class PgnFileLoader:

    def __init__(self, pgn_file_path):
        if pathlib.Path.exists(pgn_file_path):
            self.pgn_file = open(pgn_file_path)

        self.pgnDataInstance = pgnlib.read_game(self.pgn_file)

    def get_pgn_data_instance(self):
        return self.pgnDataInstance
