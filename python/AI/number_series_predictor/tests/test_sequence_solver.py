from unittest import TestCase

from sequence_solver import sequence_solver

class TestSequenceSolverParser(TestCase):
    def setUp(self):
        self.solver = sequence_solver()
        
    def test_parse_sequence_normal_delimiter(self):
        self.solver._parse_sequence('1,2,3')
        self.assertEqual(self.solver.sequence, [1, 2, 3])
    
    def test_parse_sequence_whitespace(self):
        self.solver._parse_sequence('1,  2,     3')
        self.assertEqual(self.solver.sequence, [1, 2, 3])
        
    def test_parse_sequence_different_delimiters(self):
        self.solver._parse_sequence('1,2;3]4[5"6')
        self.assertEqual(self.solver.sequence, [1, 2, 3, 4, 5, 6])
    
    def test_parse_sequence_negative_numbers(self):
        self.solver._parse_sequence('1,-2,3')
        self.assertEqual(self.solver.sequence, [1, -2, 3])
        
    def test_parse_sequence_negative_numbers_whitespace(self):
        self.solver._parse_sequence('1,   -2 ,-  3')
        self.assertEqual(self.solver.sequence, [1, -2, 3])
        
class TestSequenceSolver(TestCase):
    def setUp(self):
        self.solver = sequence_solver()
        
    def test_find_next_number(self):
        self.assertEqual(self.solver.find_next_number('1,2,3'), 4)