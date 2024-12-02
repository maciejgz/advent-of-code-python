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
    """
    Read the input file and return the content as a string
    """
    with open("day_10/input.txt", "r") as file:
        return file.read()


def main():
    """ 
    Main function to find the farthest point in the maze
    """
    input = read_file()
    input_chars = []
    for line in input.split("\n"):
        input_chars.append(line)
    s_position = find_farthest_point(input_chars)   
    
            
def find_farthest_point(maze):
    """
    Find the farthest point from the starting position in the maze
    """
    start_position = find_animal_start(maze)
    print(f"animal start position {start_position}")
    
    loop = []
    
    loop.append
    
    return 0;



def find_animal_start(maze):
    """
    Find the starting position of the animal in the maze
    """
    for i, line in enumerate(maze):
        for j, char in enumerate(line):
            if char == "S":
                return (i, j)
            
            

def test_simple_maze():
    """
    Test the find_farthest_point function with a simple maze
    """
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
    
