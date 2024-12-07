import os

def get_next_position(current_position, direction):
    if direction == "^":
        return [current_position[0] - 1, current_position[1]]
    elif direction == ">":
        return [current_position[0], current_position[1] + 1]
    elif direction == "v":
        return [current_position[0] + 1, current_position[1]]
    elif direction == "<":
        return [current_position[0], current_position[1] - 1]
    
def turn_right(direction):
    if direction == "^":
        return ">"
    elif direction == ">":
        return "v"
    elif direction == "v":
        return "<"
    elif direction == "<":
        return "^"
    
def print_two_dimensional_array(array):
    for row in array:
        print("".join(row))

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = f.readlines()
    
    # make two dimensional array from input
    lines = [list(line.strip()) for line in lines]
    
    # find the position of the - element ^ > v <
    starting_position = [0, 0]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] in "^>v<":
                starting_position = [i, j]
                direction = lines[i][j]
                break
        if starting_position != [0, 0]:
            break
            
    # mark the initial position
    lines[starting_position[0]][starting_position[1]] = "x"
    
    # simulate movements and turn right 90 degrees when you'll find #
    current_position = starting_position
    path = [current_position]
    while True:
        next_position = get_next_position(current_position, direction)
        if next_position[0] < 0 or next_position[0] >= len(lines) or next_position[1] < 0 or next_position[1] >= len(lines[0]):
            break
        if lines[next_position[0]][next_position[1]] == "#":
            direction = turn_right(direction)
            next_position = get_next_position(current_position, direction)
            if next_position[0] < 0 or next_position[0] >= len(lines) or next_position[1] < 0 or next_position[1] >= len(lines[0]):
                break
            if lines[next_position[0]][next_position[1]] == "#":
                continue
            elif lines[next_position[0]][next_position[1]] == ".":
                lines[next_position[0]][next_position[1]] = "x"
        elif lines[next_position[0]][next_position[1]] == ".":
            lines[next_position[0]][next_position[1]] = "x"
        current_position = next_position
        path.append(current_position)
        
    print_two_dimensional_array(lines)
    # count all x
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "x":
                count += 1
                
    print(count)




