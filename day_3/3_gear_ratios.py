## https://adventofcode.com/2023/day/3
import re
import numpy as np


class NumberPosition:
    value = 0
    position = 0
    length = 0
    row = 0

    def __init__(self):
        self.value = 0
        self.position = 0
        self.length = 0
        row = 0

    def __str__(self):
        return (
            "Value: "
            + str(self.value)
            + " Position: "
            + str(self.position)
            + " Length: "
            + str(self.length)
            + " Row: "
            + str(self.row)
        )


def read_file():
    with open("day_3/input.txt", "r") as file:
        # Read the entire file content into a single string
        return file.read()


def main():
    input = read_file()
    input_chars = []
    for line in input.split("\n"):
        if not line:
            continue
        else:
            input_chars.append(line)

    # print(input_chars)
    number_positions = []
    ## find NumberPosition in input
    i = 0
    for line in input_chars:
        number_positions_found = findNumberPositionsInLine(line, i)
        for number_position in number_positions_found:
            number_positions.append(number_position)
        i += 1

    for number_position in number_positions:
        print(number_position.value)

    sum = 0
    for number_position in number_positions:
        if isCorrectNumberPosition(number_position, input_chars):
            sum += number_position.value
    print("Result: " + str(sum))


def isCorrectNumberPosition(number_position, input_chars):
    ## check if number position is sourrounded by aby non dot character
    row = number_position.row
    position = number_position.position
    ## check if the number is in the first row and char before and after is a non dot character
    if row == 0:
        if (
            input_chars[row][position - 1] != "."
            or input_chars[row][position + number_position.length] != "."
        ):
            return True
        for i in range(position - 1, position + number_position.length + 1):
            if input_chars[row + 1][i] != ".":
                return True
    ## check if the number is in the last row and char before and after is a non dot character
    elif row == len(input_chars) - 1:
        if (
            input_chars[row][position - 1] != "."
            or input_chars[row][position + number_position.length] != "."
        ):
            return True
        for i in range(position - 1, position + number_position.length + 1):
            if input_chars[row - 1][i] != ".":
                return True

    ## check if the number is in the middle row and char before and after is a non dot character. chech if charaters above and below are not dots
    else:
        print(
            "Check middle row "
            + str(row)
            + " "
            + str(position)
            + " "
            + str(number_position.value)
            + "  "
            + str(len(input_chars))
        )
        if ((position - 1) >= 0 and input_chars[row][position - 1] != ".") or (
            (position + number_position.length) < len(input_chars[row])
            and input_chars[row][position + number_position.length] != "."
        ):
            return True
        ## check previous and next row
        for i in range(position - 1, position + number_position.length + 1):
            if ((row - 1) >= 0) and  (i < len(input_chars[row-1]))  and (input_chars[row - 1][i] != "."):
                return True
            if ((row + 1) <= len(input_chars) - 1) and  (i < len(input_chars[row+1])) and (input_chars[row + 1][i] != "."):
                return True

    print("Number position is not correct" + str(number_position))

    return False


def findNumberPositionsInLine(input_line, line_number):
    number_positions = []
    i = 0
    while i < len(input_line):
        if input_line[i].isdigit():
            print("Found number at position " + str(i) + " with value " + input_line[i])
            number_position_found = buildNumberPosition(i, input_line, line_number)
            number_positions.append(number_position_found)
            i += number_position_found.length
        else:
            i += 1
    return number_positions


def buildNumberPosition(position, input_line, line_number):
    stringNumber = ""
    length = 0
    for i in range(position, len(input_line)):
        if input_line[i].isdigit():
            stringNumber += input_line[i]
            length += 1
        else:
            break
    number_position = NumberPosition()
    number_position.value = int(stringNumber)
    number_position.position = position
    number_position.length = length
    number_position.row = line_number
    print(number_position)
    return number_position


if __name__ == "__main__":
    main()
