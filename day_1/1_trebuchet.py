input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""";



def main(input):
    
    values = []
    
    for line in input.split("\n"):
        if not line:
            continue
        else:
            print(line)
        
if __name__ == "__main__":
    main(input)