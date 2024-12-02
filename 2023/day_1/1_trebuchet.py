input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""";



def main(input):
    
    values = []
    result = 0;
    
    with open('day_1/input.txt', 'r') as file:
        # Read the entire file content into a single string
        file_content = file.read()
    
    for line in file_content.split("\n"):
        if not line:
            continue
        else:
            first = None
            last = None
            for char in line:
                if char.isdigit():
                    if first is None:
                        first = int(char)
                    last = int(char)
            
            number = last + 10 * first;
            values.append(number)
    for value in values:
        result += value  
    print(result)    
        
if __name__ == "__main__":
    main(input)