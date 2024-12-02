def read_file():
    with open("day_9/input.txt", "r") as file:
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
    
    input_ints = []
    for line in input_chars:
        vals = []
        for char in line.split(" "):
            vals.append(int(char))
        input_ints.append(vals)
    
    print(input_ints)
    sum = 0
    for line in input_ints:
        result = extrapolate(line)
        sum += (result[len(result)-1])
    
    print("SUM: ", sum)
            
def extrapolate(line):
    extrapolated_values = []
    for i in range(len(line)-1):
        diff = line[i+1] - line[i]
        extrapolated_values.append(diff)
        
    print("EXTRAPOLATED VALUES: ", extrapolated_values)
    all_zeroes = all(elem == 0 for elem in extrapolated_values)
    if all_zeroes:
        line.append((line[len(line)-1]) + 0)
        return line
    else:
        result_values = extrapolate(extrapolated_values)
        print("result_values: ", result_values)
        line.append(line[len(line)-1] + result_values[len(result_values)-1])
        print("obliczona LINE: ", line)
        return line
        
    
if __name__ == "__main__":
    main()
