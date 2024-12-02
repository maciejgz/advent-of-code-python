

def read_file():
    with open("day_6/input.txt", "r") as file:
        # Read the entire file content into a single string
        return file.read()
    
def main():
    result = 0
    input = read_file();
    input_chars = []
    for line in input.split("\n"):
        if not line:
            input_chars.append('')
        else:
            input_chars.append(line)
    times = get_times(input_chars)
    distances = get_distances(input_chars)
    print(times)
    
    
    ways_to_win = []
    i = 0;
    for race in times:
        ways_to_win_internal = 0;
        for j in range(0, times[i]+1):
            print(j)
            if (get_distance_traveled(race - j, j) > distances[i]):
                ways_to_win_internal += 1
        ways_to_win.append(ways_to_win_internal)
        i+=1
        
    result = 1;
    for ways in ways_to_win:
        result *= ways
        
    print(result)
        
    

def get_distance_traveled(time, distance):
    return distance * time
    
            
def get_times(input_line):
    input_numbers = input_line[0].replace('Time: ', '').split()
    for i in range(len(input_numbers)):
        input_numbers[i] = int(input_numbers[i])
    return input_numbers


def get_distances(input_line):
    input_numbers = input_line[1].replace('Distance: ', '').split()
    for i in range(len(input_numbers)):
        input_numbers[i] = int(input_numbers[i])
    return input_numbers
    
    
if __name__ == "__main__":
    main()
