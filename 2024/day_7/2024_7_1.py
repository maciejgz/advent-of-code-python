import os

### support functions
def print_two_dimensional_array(array):
    for row in array:
        print("".join(row))
        
        
def evaluate_operators(values, operators):
    """Evaluate the expression given values and operators in left-to-right order."""
    result = values[0]
    for i, op in enumerate(operators):
        if op == "+":
            result += values[i + 1]
        elif op == "*":
            result *= values[i + 1]
    return result


def match_value(test_value, values, operators=[], pos=0):
    """Recursively tries all operator combinations to match the test value."""
    if pos == len(values) - 1:
        # If we've placed operators between every pair of values, evaluate the expression
        return evaluate_operators(values, operators) == test_value

    # Try adding a '+' operator and recurse
    if match_value(test_value, values, operators + ["+"], pos + 1):
        return True
    
    # Try adding a '*' operator and recurse
    if match_value(test_value, values, operators + ["*"], pos + 1):
        return True
    
    # If neither works, return False
    return False


def solve_equations(equations):
    total_calibration_result = 0

    for equation in equations:
        parts = equation.split(':')
        test_value = int(parts[0].strip())
        values = list(map(int, parts[1].strip().split()))

        # Check if the equation can be true with any combination of operators
        if match_value(test_value, values):
            total_calibration_result += test_value

    return total_calibration_result



### solution
input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = f.readlines()
    
    # make two dimensional array from input
    
print(solve_equations(lines))