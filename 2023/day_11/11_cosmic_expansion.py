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
    space = double_no_galaxies_columns(space, no_galaxies_columns)
    print("\n".join(space))
    
    galaxies_positions = find_galaxies_positions(space)
    print(f"Galaxies positions: {galaxies_positions}")
    result = calculate_all_distances(galaxies_positions)
    # sum of all distances
    print(f"Sum of all distances: {sum(result)}")


def calculate_all_distances(galaxies_positions):
    """
    Calculate the distances between all the galaxies
    """
    distances = []
    for i in range(len(galaxies_positions)):
        for j in range(i + 1, len(galaxies_positions)):
            distance = calculate_distance(galaxies_positions[i], galaxies_positions[j])
            distances.append(distance)
    return distances


def calculate_distance(galaxy1, galaxy2):
    """
    Calculate the distance between two galaxies
    """
    print(f"Calculating distance between {galaxy1} and {galaxy2} result is {abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])}")
    return (abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1]))


def find_galaxies_positions(space):
    """
    Find the positions of the galaxies in the space
    """
    galaxies = []
    for i, line in enumerate(space):
        for j, char in enumerate(line):
            if char == "#":
                galaxies.append((i, j))
    return galaxies


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
    Double the rows without galaxies. Doubled rows will have only . characters
    """
    counter = 0
    for i in no_galaxies_rows:
        space.insert(i + counter, "." * len(space[0]))
        counter += 1
    return space


def double_no_galaxies_columns(space, no_galaxies_columns):
    """
    Double the columns without galaxies and put . in them
    """
    counter = 0
    for i in no_galaxies_columns:
        for j in range(len(space)):
            space[j] = space[j][:i+counter] + "." + space[j][i+counter:]
        counter += 1
    return space


if __name__ == "__main__":
    main()
