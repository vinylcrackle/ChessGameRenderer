import chess.pgn as pgnlib
import pathlib


class PgnFileLoader:

    pgn_file = None
    pgn_data_instance = None

    def __init__(self, pgn_file_path):
        if pathlib.Path.exists(pgn_file_path):
            self.pgn_file = open(pgn_file_path)

        self.pgn_data_instance = pgnlib.read_game(self.pgn_file)

    def get_pgn_data_instance(self):
        return self.pgn_data_instance
