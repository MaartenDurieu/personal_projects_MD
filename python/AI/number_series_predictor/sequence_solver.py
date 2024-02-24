import numpy as np
import re
from sequence_type_handler import sequence_type_handler

class sequence_solver:
    def __init__(self):
        self.sequence = None
        self.sequence_handler = sequence_type_handler()
        
    def _parse_sequence(self, raw_input: str):
        # Determine the sequence by splitting the input string into groups of numbers
        # Allow potential negative numbers
        sequence = re.findall(r'-?\d+', raw_input)
        
        # Convert the list os strings to integers
        self.sequence = list(map(int, sequence))
        self.sequence_length = len(self.sequence)     
    
    def find_next_number(self, raw_input: str):
        """
        Given a sequence, finds the next number in the sequence.
        Firstly the sequence is parsed based on groups of digits in order to allow flexible delimiters for the input.
        Next the sequence type is iteratively defined, going from simpel to more complex types.
        If a match is found, the corresponding formula of that sequence is used to derived the next number in the sequence.
        
        ---Appr
        At first this problem was approached with AI. 
        However, this would require a very large dataset to train the model,
        consisting of close to all possible sequences.
        
        -> break early if easy sequence
        
        turns out AI not precise enough
        
        -> use math to solve
        
        """
        self._parse_sequence(raw_input)
        return self.sequence_handler.interpret_sequence(self.sequence)

# if __name__ == '__main__':
#     tester = sequence_solver()
# print(tester.find_next_number('2,4,16'))
        
    
    
 
    https://atozmath.com/example/NumberSeries.aspx?q=1&q1=E3