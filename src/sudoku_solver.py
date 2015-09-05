__author__ = 'andrea'
import numpy as np


class SudokuSolver(object):
    def __init__(self, input):
        self._input = np.matrix(input)

    def solution(self):
        return self._input

    def solution_for_row(self, row_number):
        """finds solution for given row"""
        pass

    def is_row_filled_in(self, row_number):
        row = self._input[row_number]
        return not (row == np.matrix('0 0 0 0 0 0 0 0 0')).any()

    def is_column_filled_in(self, column_number):
        column = self._input[:, column_number]
        return not (column == np.matrix('0; 0; 0; 0; 0; 0; 0; 0; 0')).any()

    def is_square_filled_in(self, square_number):
        return True


    def fetch_square(self, square_number):
        square_coordinates = self.coordinates_for_square(square_number)
        square = self._input[]
        pass

    def coordinates_for_square(self, square_number):
        if square_number in (0, 3, 6):
            col = (0, 1, 2)
        elif square_number in (1, 4, 7):
            col = (3, 4, 5)
        elif square_number in (2, 5, 8):
            col = (6, 7, 8)
        if square_number < 3:
            row = (0, 1, 2)
        elif square_number < 6:
            row = (3, 4, 5)
        else:
            row = (6, 7, 8)
        return {'row': row, 'col': col}






