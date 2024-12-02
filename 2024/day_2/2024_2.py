import os


def main():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file, "r") as f:
        lines = f.readlines()

    safe_levels = 0

    for line in lines:
        numbers = line.split(" ")
        numbers = [int(num.strip()) for num in numbers]  # Convert to array of int
        direction = 0
        for i in range(len(numbers) - 1):
            if (numbers[i] < numbers[i + 1]) and (direction == 0) and (abs(numbers[i] - numbers[i + 1]) >= 1) and (
                abs(numbers[i] - numbers[i + 1]) <= 3
            ):
                direction = 1
                continue
            elif (numbers[i] > numbers[i + 1]) and (direction == 0) and (abs(numbers[i] - numbers[i + 1]) >= 1) and (
                abs(numbers[i] - numbers[i + 1]) <= 3
            ):
                direction = -1
                continue
            elif (numbers[i] > numbers[i + 1]) and (direction == 1):
                direction = 2
                break
            elif (numbers[i] < numbers[i + 1]) and (direction == -1):
                direction = 2
                break
            elif (abs(numbers[i] - numbers[i + 1]) >= 1) and (
                abs(numbers[i] - numbers[i + 1]) <= 3
            ):
                continue
            else:
                direction = 2
                break
        if direction == 1 or direction == -1:
            safe_levels += 1
            print(f'{line.strip()}')

    print(safe_levels)


if __name__ == "__main__":
    main()
