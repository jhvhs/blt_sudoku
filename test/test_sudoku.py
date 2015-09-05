from unittest import TestCase, skip
import numpy

from src.sudoku_solver import SudokuSolver

INCOMPLETE_SOLUTION = '0 9 5 7 4 3 8 6 1; 4 3 1 8 6 5 9 2 7; 8 7 6 1 9 2 5 4 3; ' \
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
        slice = self.solver.coordinates_for_square(0)
        self.assertEqual(slice['row'], (0, 1, 2))
        self.assertEqual(slice['col'], (0, 1, 2))

        slice = self.solver.coordinates_for_square(1)
        self.assertEqual(slice['row'], (0, 1, 2))
        self.assertEqual(slice['col'], (3, 4, 5))

        slice = self.solver.coordinates_for_square(2)
        self.assertEqual(slice['row'], (0, 1, 2))
        self.assertEqual(slice['col'], (6, 7, 8))

        slice = self.solver.coordinates_for_square(3)
        self.assertEqual(slice['row'], (3, 4, 5))
        self.assertEqual(slice['col'], (0, 1, 2))

        slice = self.solver.coordinates_for_square(4)
        self.assertEqual(slice['row'], (3, 4, 5))
        self.assertEqual(slice['col'], (3, 4, 5))

        slice = self.solver.coordinates_for_square(5)
        self.assertEqual(slice['row'], (3, 4, 5))
        self.assertEqual(slice['col'], (6, 7, 8))

        slice = self.solver.coordinates_for_square(6)
        self.assertEqual(slice['row'], (6, 7, 8))
        self.assertEqual(slice['col'], (0, 1, 2))

        slice = self.solver.coordinates_for_square(7)
        self.assertEqual(slice['row'], (6, 7, 8))
        self.assertEqual(slice['col'], (3, 4, 5))

        slice = self.solver.coordinates_for_square(8)
        self.assertEqual(slice['row'], (6, 7, 8))
        self.assertEqual(slice['col'], (6, 7, 8))

    def test_square_complete(self):
        self.assertTrue(self.solver.is_square_filled_in(0))



class IncompleteSudokuTests(TestCase):
    def setUp(self):
        self.solver = SudokuSolver(INCOMPLETE_SOLUTION)

    def test_row_incomplete(self):
        self.assertFalse(self.solver.is_row_filled_in(0))

    @skip('need the row level solution')
    def test_solution_for_row(self):
        self.assertEqual(self.solver.solution_for_row(0), SOLUTION[0:17])

    def test_column_incomplete(self):
        self.assertFalse(self.solver.is_column_filled_in(0))

    @skip('need to fetch a square by number')
    def test_square_incomplete(self):
        self.assertFalse(self.solver.is_square_filled_in(0))



