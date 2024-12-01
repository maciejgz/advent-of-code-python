import re
from collections import Counter

def read_file():
    """
    Read the input file and return the content as a string
    """
    with open("thread_reader/input.txt", "r") as file:
        return file.read()
    
def main():
    """
    Main function
    """
    input = read_file()
    
    # Wyrażenie regularne do znalezienia typów statusów
    pattern = re.compile(r'java\.lang\.Thread\.State:\s+(\w+)')

    # Znajdź wszystkie wystąpienia typów statusów
    statuses = pattern.findall(input)

    # Policz wystąpienia każdego typu statusu
    status_counts = Counter(statuses)

    # Wyświetl wyniki
    print(status_counts)

    
if __name__ == "__main__":
    main()