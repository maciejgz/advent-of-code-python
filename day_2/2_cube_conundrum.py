
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

if __name__ == "__main__":
    main(input)