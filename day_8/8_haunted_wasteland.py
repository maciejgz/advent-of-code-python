import re

def read_file():
    with open("day_8/input.txt", "r") as file:
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
            
    path = input_chars[0];
    nodes  = create_nodes(input_chars)
    
    steps_number = 0
    current_node = "AAA"
    
    while True:
        for i in range(0, len(path)):
            if path[i] == "L":
                node = nodes[nodes[current_node].left_turn]
            else:
                node = nodes[nodes[current_node].right_turn]
            steps_number += 1;
            print("Step: " + str(steps_number) + " Turn: " + path[i] + " Node: " + node.node + " Left: " + node.left_turn + " Right: " + node.right_turn)
            current_node = node.node
            if node.node == "ZZZ":
                print("steps: " + str(steps_number))
                return
            
    print("steps: " + steps_number)

    
  
def create_nodes(input_chars):
    nodes = {}
    for i in range(2, len(input_chars)):
        pattern = r"\b[A-Z]{3}\b"
        matches = re.findall(pattern, input_chars[i])
        print(matches)
        nodes[matches[0]] = Node(matches[0], matches[1], matches[2])
    return nodes
        
        
            
class Node:
    node = "";
    left_turn = "";
    right_turn = "";
    
    def __init__(self, node, left_turn, right_turn):
        self.node = node
        self.left_turn = left_turn
        self.right_turn = right_turn
        
    def __str__(self):
        return f"Node: {self.node}, Left: {self.left_turn}, Right: {self.right_turn}"
    
    
if __name__ == "__main__":
    main()
