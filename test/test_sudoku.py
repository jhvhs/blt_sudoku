from unittest import TestCase, skip
import numpy

from src.sudoku_solver import SudokuSolver

SOLUTION_WITHOUT_ONE_VALUE = '0 9 5 7 4 3 8 6 1; 4 3 1 8 6 5 9 2 7; 8 7 6 1 9 2 5 4 3; ' \
                             '3 8 7 4 5 9 2 1 6; 6 1 2 3 8 7 4 9 5; 5 4 9 2 1 6 7 3 8; ' \
                             '7 6 3 5 3 4 1 8 9; 9 2 8 6 7 1 3 5 4; 1 5 4 9 3 8 6 7 2 '

SOLUTION_WITHOUT_TWO_VALUES_IN_ROW = '0 9 5 7 4 3 0 6 1; 4 3 1 8 6 5 9 2 7; 8 7 6 1 9 2 5 4 3; ' \
                                     '3 8 7 4 5 9 2 1 6; 6 1 2 3 8 7 4 9 5; 5 4 9 2 1 6 7 3 8; ' \
                                     '7 6 3 5 3 4 1 8 9; 9 2 8 6 7 1 3 5 4; 1 5 4 9 3 8 6 7 2 '

SOLUTION_WITHOUT_TWO_VALUES_IN_COLUMN = '0 9 5 7 4 3 8 6 1; 0 3 1 8 6 5 9 2 7; 8 7 6 1 9 2 5 4 3; ' \
                                        '3 8 7 4 5 9 2 1 6; 6 1 2 3 8 7 4 9 5; 5 4 9 2 1 6 7 3 8; ' \
                                        '7 6 3 5 3 4 1 8 9; 9 2 8 6 7 1 3 5 4; 1 5 4 9 3 8 6 7 2 '

SOLUTION = '2 9 5 7 4 3 8 6 1; 4 3 1 8 6 5 9 2 7; 8 7 6 1 9 2 5 4 3; ' \
           '3 8 7 4 5 9 2 1 6; 6 1 2 3 8 7 4 9 5; 5 4 9 2 1 6 7 3 8; ' \
           '7 6 3 5 3 4 1 8 9; 9 2 8 6 7 1 3 5 4; 1 5 4 9 3 8 6 7 2 '

SQUARE0 = '2 9 5; 4 3 1; 8 7 6'


class CompleteSudokuTests(TestCase):
    def setUp(self):
        self.solver = SudokuSolver(SOLUTION)

    def test_solved_solution(self):
        self.assertTrue(numpy.array_equal(self.solver.solution(), numpy.matrix(SOLUTION)))

    def test_row_complete(self):
        self.assertTrue(self.solver.is_row_filled_in(0))

    def test_column_complete(self):
        self.assertTrue(self.solver.is_column_filled_in(0))

    def test_square_fetch(self):
        self.assertTrue(numpy.array_equal(self.solver.fetch_square(0), numpy.matrix(SQUARE0)))

    def test_square_array_slice(self):
        """testing for slice of main sudoku square that gets returned. maps to the square"""
        _slice = self.solver.coordinates_for_square(0)
        self.assertEqual(_slice['row'], (0, 1, 2))
        self.assertEqual(_slice['col'], (0, 1, 2))

        _slice = self.solver.coordinates_for_square(1)
        self.assertEqual(_slice['row'], (0, 1, 2))
        self.assertEqual(_slice['col'], (3, 4, 5))

        _slice = self.solver.coordinates_for_square(2)
        self.assertEqual(_slice['row'], (0, 1, 2))
        self.assertEqual(_slice['col'], (6, 7, 8))

        _slice = self.solver.coordinates_for_square(3)
        self.assertEqual(_slice['row'], (3, 4, 5))
        self.assertEqual(_slice['col'], (0, 1, 2))

        _slice = self.solver.coordinates_for_square(4)
        self.assertEqual(_slice['row'], (3, 4, 5))
        self.assertEqual(_slice['col'], (3, 4, 5))

        _slice = self.solver.coordinates_for_square(5)
        self.assertEqual(_slice['row'], (3, 4, 5))
        self.assertEqual(_slice['col'], (6, 7, 8))

        _slice = self.solver.coordinates_for_square(6)
        self.assertEqual(_slice['row'], (6, 7, 8))
        self.assertEqual(_slice['col'], (0, 1, 2))

        _slice = self.solver.coordinates_for_square(7)
        self.assertEqual(_slice['row'], (6, 7, 8))
        self.assertEqual(_slice['col'], (3, 4, 5))

        _slice = self.solver.coordinates_for_square(8)
        self.assertEqual(_slice['row'], (6, 7, 8))
        self.assertEqual(_slice['col'], (6, 7, 8))

    def test_square_complete(self):
        self.assertTrue(self.solver.is_square_filled_in(0))

    def test_solution_for_row(self):
        self.assertTrue((self.solver.solution_for_row(0) == numpy.matrix(SOLUTION[0:17])).all())

    def test_solution_for_column(self):
        solution = numpy.matrix(SOLUTION)
        self.assertTrue((self.solver.solution_for_column(0) == solution[:, 0]).all())

    def test_solution_for_square(self):
        solution = numpy.matrix(SOLUTION)
        self.assertTrue((self.solver.solution_for_square(0) == solution[(0, 1, 2), :][:, (0, 1, 2)]).all())


class SingleMissingValueSudokuTests(TestCase):
    def setUp(self):
        self.solver = SudokuSolver(SOLUTION_WITHOUT_ONE_VALUE)

    def test_row_incomplete(self):
        self.assertFalse(self.solver.is_row_filled_in(0))

    def test_square_incomplete(self):
        self.assertFalse(self.solver.is_square_filled_in(0))

    def test_solution_for_row(self):
        self.assertTrue((self.solver.solution_for_row(0) == numpy.matrix(SOLUTION[0:17])).all())

    def test_solution_for_column(self):
        expected = numpy.matrix(SOLUTION)
        self.assertTrue((self.solver.solution_for_column(0) == expected[:, 0]).all())

    def test_column_incomplete(self):
        self.assertFalse(self.solver.is_column_filled_in(0))

    def test_solution_for_square(self):
        solution = numpy.matrix(SOLUTION)
        self.assertTrue((self.solver.solution_for_square(0) == solution[(0, 1, 2), :][:, (0, 1, 2)]).all())


class TwoMissingValuesInRowSudokuTests(SingleMissingValueSudokuTests):
    def setUp(self):
        self.solver = SudokuSolver(SOLUTION_WITHOUT_TWO_VALUES_IN_ROW)