from unittest import TestCase

from sequence_type_handler import sequence_type_handler

class TestSequenceTypeHandler(TestCase):
    def setUp(self):
        self.handler = sequence_type_handler()
        
    def test_linear_handler(self):
        self.assertEqual(self.handler.linear_handler([1, 2, 3]), 4)
    
    def test_geometric_handler(self):
        self.assertEqual(self.handler.geometric_handler([2, 4, 8]), 16)
        
    def test_exponential_handler(self):
        self.assertEqual(self.handler.exponential_handler([2, 4, 16]), 256)
        