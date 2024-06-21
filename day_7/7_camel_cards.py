

def read_file():
    with open("day_7/input.txt", "r") as file:
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
            
    print(input_chars)
    hands = []
    for line in input_chars:
        parsed_hand = line.split(" ");
        hand = Hand()
        hand.cards = sorted([translate_card_to_number(card) for card in parsed_hand[0]])
        hand.bid = int(parsed_hand[1])
        hands.append(hand)
        
            
    for hand in hands:
        print(hand)
        assign_points(hand)
        
    ## TODO put hands in map of results
        
    
def assign_points(hand):
    if get_five_of_a_kind_result(hand) > 0:
        hand.points = get_five_of_a_kind_result(hand);
    elif get_four_of_a_kind_result(hand) > 0:
        hand.points = get_four_of_a_kind_result(hand);
    elif get_full_house_result(hand) > 0:
        hand.points = get_full_house_result(hand);
    elif get_three_of_a_kind_result(hand) > 0:
        hand.points = get_three_of_a_kind_result(hand);
    elif get_two_pairs_result(hand) > 0:
        hand.points = get_two_pairs_result(hand);
    elif get_one_pair_result(hand) > 0:
        hand.points = get_one_pair_result(hand);
    elif get_high_card_result(hand) > 0:
        hand.points = get_high_card_result(hand);    
    else:
        return 0

def translate_card_to_number(card):
    if card == "A":
        return 14
    elif card == "K":
        return 13
    elif card == "Q":
        return 12
    elif card == "J":
        return 11
    elif card == "T":
        return 10
    else:
        return int(card)
    
    
def get_five_of_a_kind_result(hand):
    if (len(set(hand.cards)) == 1):
        return 1000 + hand.cards[0];
    else:
        return 0; 
    
def get_four_of_a_kind_result(hand):
    ## TODO implement
    return 0

def get_full_house_result(hand):
    ## TODO implement
    return 0

def get_three_of_a_kind_result(hand):
    ## TODO implement
    return 0

def get_two_pairs_result(hand):
    ## TODO implement
    return 0

def get_one_pair_result(hand):
    ## TODO implement
    return 0

def get_high_card_result(hand):
    ## TODO implement
    return 0


class Hand:
    cards = []
    bid = 0
    points = 0
    
    def __init__(self):
        self.cards = []
        self.bid = 0
        self.points = 0
        
    def __str__(self):
        return "Cards: " + str(self.cards) + " Bid: " + str(self.bid) + " Points: " + str(self.points)
    

if __name__ == "__main__":
    main()
