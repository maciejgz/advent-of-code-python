import re

def read_file():
    with open('day_2/input.txt', 'r') as file:
        # Read the entire file content into a single string
        return file.read()

def main(input):
    print("Hello World!")
    input = read_file();
    for line in input.split("\n"):
        if not line:
            continue
        else:
            print(line)
            match = re.search(r"Game (\d+)", line)
            if match:
                game_number = match.group(1)
                print(game_number)
            else:
                print("No match found")
            

if __name__ == "__main__":
    main(input)