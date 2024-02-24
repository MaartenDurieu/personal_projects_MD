def derive_formula(sequence):
    differences = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
    
    # Check if differences are all the same
    if all(diff == differences[0] for diff in differences):
        multiplier = differences[0] / sequence[0]
        if multiplier.is_integer():
            return f"Previous number multiplied by {int(multiplier)}"
        else:
            return f"Previous number multiplied by {multiplier}"
    else:
        # Check if sequence is added with constant and then multiplied
        add_constant = sequence[1] - sequence[0]
        multiply_constant = sequence[1] / sequence[0]
        if all(sequence[i] == sequence[i-1] * multiply_constant + add_constant for i in range(1, len(sequence))):
            return f"Previous number multiplied by {multiply_constant} and then added by {add_constant}"
        
        # Check if sequence is multiplied by constant and then added
        multiply_constant = sequence[1] - sequence[0]
        add_constant = sequence[1] - (sequence[0] * multiply_constant)
        if all(sequence[i] == sequence[i-1] + add_constant for i in range(1, len(sequence))):
            return f"Previous number multiplied by {multiply_constant} and then added by {add_constant}"

# Example: Sequence 2, 12, 42, 102
sequence = [2, 12, 42, 102]
formula = derive_formula(sequence)
print("Formula for the sequence:", formula)

# Example: Sequence 4, 10, 28, 82, 24
sequence = [4, 10, 28, 82, 24]
formula = derive_formula(sequence)
print("Formula for the sequence:", formula)
