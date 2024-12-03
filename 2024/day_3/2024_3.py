import os
import re

def main():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file, "r") as f:
        lines = f.readlines()
        
    text = ""
    for line in lines:
        text += line
    
    # Regular expression pattern
    pattern = r'mul\(\d{1,3},\d{1,3}\)'

    # Find all matches
    matches = re.findall(pattern, text)

    result = 0
    # Print matches
    for match in matches:
        result += int(match.split("(")[1].split(",")[0]) * int(match.split(",")[1].split(")")[0])
        
    print(result)
        
        
if __name__ == "__main__":
    main()
