class Direction:
    NORTH = (0, -1)
    SOUTH = (0, 1)
    EAST = (1, 0)
    WEST = (-1, 0)

PIPE_SHAPES = {
    '|': [Direction.NORTH, Direction.SOUTH],
    '-' : [Direction.EAST, Direction.WEST],
    'L': [Direction.NORTH, Direction.EAST],
    'J': [Direction.NORTH, Direction.WEST],
    '7': [Direction.SOUTH, Direction.WEST],
    'F': [Direction.SOUTH, Direction.EAST],
    'S': [Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST]
}

def read_file():
    with open("day_10/input.txt", "r") as file:
        return file.read()


def main():
    result = 0
    input = read_file()
    input_chars = []
    for line in input.split("\n"):
        if not line:
            input_chars.append("")
        else:
            input_chars.append(line)
            
            
def find_farthest_point(maze):
    find_animal_start(maze)
    return 0;


def find_animal_start(maze):
    for i, line in enumerate(maze):
        for j, char in enumerate(line):
            if char == "S":
                return (i, j)
            
            

def test_simple_maze():
    maze = '''
.....
.S-7.
.|.|.
.L-J.
.....
    '''
    farthest_point = find_farthest_point(maze)
    assert farthest_point == 4, f"Expected 4, but got {farthest_point}"
    print("Simple maze test passed")
    
    
if __name__ == "__main__":
    main()
    
