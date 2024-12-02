import re

limit_red = 12;
limit_green = 13;
limit_blue = 14;

def read_file():
    with open('day_2/input.txt', 'r') as file:
        # Read the entire file content into a single string
        return file.read()

def main(input):
    print("Hello World!")
    input = read_file();
    max_red = 0;
    max_green = 0;
    max_blue = 0;
    id_sum = 0;
    for line in input.split("\n"):
        if not line:
            continue
        else:
            game_number = 0;
            
            print(line)
            match = re.search(r"Game (\d+)", line)
            if match:
                game_number = match.group(1)
                print(game_number)
            else:
                print("No match found")
                
            
            pattern = r"(\d+)\s*(red|green|blue)"

            # Find all matches
            matches = re.findall(pattern, line)

            # Initialize a dictionary to hold the sum of values for each color
            color_maxes = {"red": 0, "green": 0, "blue": 0}

            # Iterate over the matches and set the max value for each color
            for value, color in matches:
                if color == "red":
                    color_maxes["red"] = max(color_maxes["red"], int(value))
                elif color == "green":
                    color_maxes["green"] = max(color_maxes["green"], int(value))
                elif color == "blue":
                    color_maxes["blue"] = max(color_maxes["blue"], int(value))

            print(color_maxes)
                
            if color_maxes["red"] <= limit_red and color_maxes["green"] <= limit_green and color_maxes["blue"] <= limit_blue:
                print("Game " + game_number + " is correct!")
                id_sum += int(game_number)
                
    print("The sum of the winning games is " + str(id_sum))
            

if __name__ == "__main__":
    main(input)