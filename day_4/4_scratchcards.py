## https://adventofcode.com/2023/day/3
import re
import numpy as np


def read_file():
    with open("day_4/input.txt", "r") as file:
        # Read the entire file content into a single string
        return file.read()


def main():
    result = 0

    input = read_file()
    input_chars = []
    for line in input.split("\n"):
        if not line:
            continue
        else:
            input_chars.append(line)

    for line in input_chars:
        guesses = get_guesses(line)
        resutls = get_winning_numbers(line)
        result += calculate_win(find_matches(guesses, resutls))

    print(result)


def find_matches(guesses, winning_numbers):
    matches = 0
    for guess in guesses:
        if guess in winning_numbers:
            matches += 1
    print(matches)
    return matches


def get_guesses(input_line):
    colon_index = input_line.index(":")
    pipe_index = input_line.index("|")

    # Krok 2: Wyciągnij podciąg
    numbers_substring = input_line[colon_index + 1 : pipe_index].strip()

    # Krok 3: Rozdziel podciąg na liczby
    numbers_str_list = numbers_substring.split()

    # Krok 4: Przekonwertuj na liczby całkowite
    numbers = [int(number) for number in numbers_str_list]

    return numbers


def get_winning_numbers(input_line):
    pipe_index = input_line.index("|")

    # Krok 2: Wyciągnij podciąg
    numbers_substring = input_line[pipe_index + 1 : len(input_line)].strip()

    # Krok 3: Rozdziel podciąg na liczby
    numbers_str_list = numbers_substring.split()

    # Krok 4: Przekonwertuj na liczby całkowite
    numbers = [int(number) for number in numbers_str_list]

    return numbers


def calculate_win(matches):
    if matches == 0:
        return 0
    result = 1
    for i in range(0, matches - 1):
        result *= 2
    return result


if __name__ == "__main__":
    main()
