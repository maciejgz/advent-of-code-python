def read_file():
    """
    Read the input file and return the content as a string
    """
    with open("day_11/input.txt", "r") as file:
        return file.read()


def main():
    """ 
    Main function
    """
    input = read_file()
    space = []
    for line in input.split("\n"):
        space.append(line)
    
    no_galaxies_rows = find_no_galaxies_rows(space)
    print(f"Rows without galaxies: {no_galaxies_rows}")
    no_galaxies_columns = find_no_galaxies_columns(space)
    print(f"Columns without galaxies: {no_galaxies_columns}")
    
    space = double_no_galaxies_rows(space, no_galaxies_rows)
    print("\n".join(space))
    space = double_no_galaxies_columns(space, no_galaxies_columns)
    print("\n".join(space))
    
        
def find_no_galaxies_rows(space):
    """
    Find the rows withour galaxies
    """
    no_galaxies = []
    for i, line in enumerate(space):
        galaxy_count = 0
        for j, char in enumerate(line):
            if char == "#":
                galaxy_count += 1
        if galaxy_count == 0:
            no_galaxies.append(i)
    return no_galaxies

def find_no_galaxies_columns(space):
    """
    Find the columns withour galaxies
    """
    no_galaxies = []
    for i in range(len(space[0])):
        galaxy_count = 0
        for j in range(len(space)):
            if space[j][i] == "#":
                galaxy_count += 1
        if galaxy_count == 0:
            no_galaxies.append(i)
    return no_galaxies

def double_no_galaxies_rows(space, no_galaxies_rows):
    """
    Double the rows without galaxies and put . in them
    """
    for i in no_galaxies_rows:
        print(len(space[i]))
        space[i] = space[i] + "\n" + "." * len(space[i])
    return space

def double_no_galaxies_columns(space, no_galaxies_columns):
    """
    Double the columns without galaxies and put . in them
    """
    ## TODO - implement this function
    return space

    
if __name__ == "__main__":
    main()
    
