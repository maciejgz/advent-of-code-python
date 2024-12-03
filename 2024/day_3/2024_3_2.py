import os
import re

def calculate_enabled_mul_sum(memory):
    # Regular expressions to match specific instructions
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Initialize state and result
    enabled = True
    total_sum = 0

    # Process the memory linearly
    index = 0
    while index < len(memory):
        # Check for `mul` instruction
        mul_match = re.match(mul_pattern, memory[index:])
        if mul_match:
            if enabled:
                x, y = int(mul_match.group(1)), int(mul_match.group(2))
                total_sum += x * y
            index += len(mul_match.group(0))
            continue

        # Check for `do()` instruction
        do_match = re.match(do_pattern, memory[index:])
        if do_match:
            enabled = True
            index += len(do_match.group(0))
            continue

        # Check for `don't()` instruction
        dont_match = re.match(dont_pattern, memory[index:])
        if dont_match:
            enabled = False
            index += len(dont_match.group(0))
            continue

        # Move to the next character if no match is found
        index += 1

    return total_sum


def main():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file, "r") as f:
        lines = f.readlines()
        
    text = ""
    for line in lines:
        text += line
    print(calculate_enabled_mul_sum(text))


if __name__ == "__main__":
    main()
