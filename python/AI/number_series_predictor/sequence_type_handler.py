import math

class sequence_type_handler:
    def __init__(self):
        self.method_order = ['linear_handler', 'geometric_handler', 'exponential_handler']
        
    def linear_handler(self, sequence: list[int])-> int|None:
        """
        Checks if the sequence is linear and returns the next number in the sequence if it is.
        A sequence is linear if the difference between consecutive numbers is constant
        An example of a linear sequence is 1, 3, 5, 7, 9
        In this sequence, the difference between consecutive numbers is 2.
        """
        constant = sequence[1] - sequence[0]
        if all(sequence[i] - sequence[i-1] == constant for i in range(2, len(sequence))):
            return sequence[-1] + constant
            
    def geometric_handler(self, sequence: list[int])-> int|None:
        """
        Checks if the sequence is geometric and returns the next number in the sequence if it is.
        A sequence is geometric if the ratio between consecutive numbers is constant.
        An example of an geometric sequence is 2, 4, 8, 16, 32.
        In this sequence, each number is multiplied by 2 to get the next number.
        """
        
        multiplier = sequence[1] / sequence[0]
        if all(sequence[i] / sequence[i-1] == multiplier for i in range(2, len(sequence))):
            return sequence[-1] * multiplier
            
            
    def exponential_handler(self, sequence: list[int])-> int|None:
        """
        Checks if the sequence is exponential.
        An exponential sequence is obtained by raising a constant base to a power that increases with each successive term.
        An example of an exponential sequence is 2, 4, 16, 256, 65536.
        """
        power = math.log(sequence[1], sequence[0])
        if all(math.log(sequence[i], sequence[i-1]) == power for i in range(2, len(sequence))):
            return sequence[-1] ** power
    
    def interpret_sequence(self, sequence: list[int])-> int|None:
        """
        Goes over all the methods in the class and checks if the sequence is of that type.
        If the sequence is of a certain type, the next number in the sequence is returned, derived from the formula of that sequence.
        """
        for handler in self.method_order:
            method = getattr(self, handler)
            result = method(sequence)
            if result:
                return result
        raise ValueError(f"The sequence could not be solved")
    
    
    # def _is_mixed_linear_exponential(self, sequence):
    #     """
    #     Checks if the sequence is a combination of linear and exponential sequence types.
    #     An example of such a mixed sequence is 1, 12, 34, 78.
    #     The formula for this example is the the previous number multipluied with 10 and then added with 2.
    #     Another example is 4,10,28,82,24.
    #     The formula for this example is the previous number multiplied with 3 and then substracted with 2.
    #     """
    #     pass

    
        
    