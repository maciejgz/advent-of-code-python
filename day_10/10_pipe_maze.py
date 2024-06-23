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
            


    
if __name__ == "__main__":
    main()