


import os


def main():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file, "r") as f:
        lines = f.readlines()
        
    ## remove /n
    lines = [line.replace("\n", "") for line in lines]


if __name__ == "__main__":
    main()