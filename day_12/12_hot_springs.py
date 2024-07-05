class Record:
    springs = []
    damaged_springs = []

    def __init__(self, springs, damaged_springs):
        self.springs = springs
        self.damaged_springs = damaged_springs

    def __str__(self):
        result = ""
        result += "springs: "
        for record in self.springs:
            result += record
            result += " "
        result += "damaged_springs: "
        for record in self.damaged_springs:
            result += str(record)
            result += " "
        return result


def read_file():
    """
    Read the input file and return the content as a string
    """
    with open("day_12/input.txt", "r") as file:
        return file.read()


def main():
    """
    Main function
    """
    input = read_file()
    space = []
    records = []
    for line in input.split("\n"):
        space.append(line)

    for line in space:
        ## split line with space
        line = line.split()
        records.append(Record(line[0], map(int, line[1].split(","))))

    result = 0
    for record in records:
        print(record)
        result += count_possibilities(record)
        
    print(f"Result: {result}")


def count_possibilities(record):
    """
    Count the possibilities of the record
    """
    if record.springs == "":
        return 1 if record.damaged_springs.size == 1 else 0
    return 0


if __name__ == "__main__":
    main()
