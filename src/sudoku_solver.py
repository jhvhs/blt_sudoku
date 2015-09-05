__author__ = 'andrea'
import numpy as np


class SudokuSolver(object):
    def __init__(self, input_):
        self._input = np.matrix(input_)

    def solution(self):
        return self._input

    def solution_for_row(self, row_number):
        """finds solution for given row"""
        row = self._input.tolist()[row_number]
        template = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        diff = template.difference(set(row))
        if len(diff) == 1:
            row[row.index(0)] = diff.pop()
        elif len(diff) > 1:
            while row.count(0) >= 1:
                zero_index = row.index(0)
                column = self.solution_for_column(zero_index).tolist()
                column_list = [sub_item for item in column for sub_item in item]
                row[zero_index] = column_list[row_number]
        return np.matrix(row)

    def is_row_filled_in(self, row_number):
        row = self._input[row_number]
        return not (row == np.matrix('0 0 0 0 0 0 0 0 0')).any()

    def is_column_filled_in(self, column_number):
        column = self._input[:, column_number]
        return not (column == np.matrix('0; 0; 0; 0; 0; 0; 0; 0; 0')).any()

    def is_square_filled_in(self, square_number):
        return not (self.fetch_square(square_number) == np.zeros((3, 3))).any()

    def fetch_square(self, square_number):
        square_coordinates = self.coordinates_for_square(square_number)
        return self._input[:, square_coordinates['col']][square_coordinates['row'], :]

    @staticmethod
    def coordinates_for_square(square_number):
        if square_number in (0, 3, 6):
            col = (0, 1, 2)
        elif square_number in (1, 4, 7):
            col = (3, 4, 5)
        else:
            col = (6, 7, 8)
        if square_number < 3:
            row = (0, 1, 2)
        elif square_number < 6:
            row = (3, 4, 5)
        else:
            row = (6, 7, 8)
        return {'row': row, 'col': col}

    def solution_for_column(self, column_number):
        row = self._input[:, column_number].tolist()
        row = [sub_item for item in row for sub_item in item]
        template = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        diff = template.difference(set(row))
        if len(diff):
            row[row.index(0)] = diff.pop()
        return np.matrix(';'.join([str(i) for i in row]))

    def solution_for_square(self, square_number):
        square = self.fetch_square(square_number).tolist()
        flat_square = [sub_item for item in square for sub_item in item]
        template = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        diff = template.difference(set(flat_square))
        if len(diff):
            for index, row in enumerate(square):
                try:
                    zero = row.index(0)
                    if zero >= 0:
                        square[index][zero] = diff.pop()
                except ValueError:
                    pass
                    # ignore
        return np.matrix(square)
