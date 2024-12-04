import os



def count_xmas_occurrences(grid):
    def search_word(x, y, dx, dy):
        """Search for the word 'XMAS' starting from (x, y) in direction (dx, dy)."""
        word = "XMAS"
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != word[i]:
                return False
        return True

    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]

    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                if search_word(x, y, dx, dy):
                    count += 1

    return count

def main():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file, "r") as f:
        lines = f.readlines()
        
    ## remove /n
    lines = [line.replace("\n", "") for line in lines]
    
    ## create two dimensional grid of characters
    grid = create_grid(lines)
    print(count_xmas_occurrences(grid))
    
def create_grid(lines):
    grid = []
    for line in lines:
        grid.append(list(line))
    return grid
        
        
      
if __name__ == "__main__":
    main()