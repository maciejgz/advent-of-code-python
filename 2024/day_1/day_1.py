import os

def main():
    ## read input
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file, 'r') as f:
        lines = f.readlines()
    left = []
    right = []
    for line in lines:
        numbers = line.strip().split('   ')
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))
        
    ## sort the numbers
    left.sort()
    right.sort()
    
    sum = 0
    ## calculate the sum of diffs between the left and right
    for i in range(len(left)):
        sum += abs(left[i] - right[i])
        
    print(sum)
    similarity_index = 0;
    ## count similarity index
    for i in range(len(left)):
        ## count how many times left[i] appears in right
        count = right.count(left[i])
        similarity_index += count * left[i]
        
    print(f'Similarity index: {similarity_index}')
        

if __name__ == '__main__':
    main()