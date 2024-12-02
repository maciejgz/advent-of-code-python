def read_file():
    with open("day_7/input.txt", "r") as file:
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

    print(input_chars)
    hands = []
    for line in input_chars:
        parsed_hand = line.split(" ")
        hand = Hand()
        hand.cards = [translate_card_to_number(card) for card in parsed_hand[0]]
        hand.bid = int(parsed_hand[1])
        
        toAdd = '';
        for x in hand.cards:
            if(x < 10):
                toAdd += '0' + str(x)
            else:
                toAdd += str(x)
        
        hand.cards_int = int(toAdd)
        hands.append(hand)

    results = {}
    for hand in hands:
        # print(hand)
        assign_points(hand, results)
            
    final_result = []
    
    for key in results:
        print(key)
        for hand in results[key]:
            print(str(hand))
            
    if "one_card" in results:
        sorted = sort_hands(results["one_card"])
        for hand in sorted:
            print("one_card: " + str(hand))
            final_result.append(hand)
    
    if "one_pair" in results: 
        sorted = sort_hands(results["one_pair"])
        for hand in sorted:
            print("pair: " + str(hand))
            final_result.append(hand)
        
    if "two_pairs" in results:
        sorted = sort_hands(results["two_pairs"])
        for hand in sorted:
            print("two_pairs: " + str(hand))
            final_result.append(hand)
        
    if "three" in results:
        sorted = sort_hands(results["three"])
        for hand in sorted:
            print("three: " + str(hand))
            final_result.append(hand)
        
    if "full" in results:
        sorted = sort_hands(results["full"])
        for hand in sorted:
            print("full: " + str(hand))
            final_result.append(hand)
    
    if "four" in results:
        sorted = sort_hands(results["four"])
        for hand in sorted:
            print("four: " + str(hand))
            final_result.append(hand)
        
    if "five" in results:
        sorted = sort_hands(results["five"])
        for hand in sorted:
            print("five: " + str(hand))
            final_result.append(hand)
        
    print("Final result: ")
    index = 1
    sum = 0
    for hand in final_result:
        hand.points = index * hand.bid
        print("Hand: " + str(hand) + " Points: " + str(hand.points))
        sum += hand.points
        index += 1
        
    print("Sum: " + str(sum))


def sort_hands(hands):
    ## sort hands by the Hand.cards.int
    hands.sort(key=lambda x: x.cards_int, reverse=False)
    
    for hand in hands:
        print("sorted: " + str(hand))
    return hands
    


def assign_points(hand, results):
    if is_five_of_a_kind_result(hand) == True:
        if "five" in results:
            results["five"].append(hand)  # Append new points to the existing list
        else:
            results["five"] = [hand]
    elif is_four_of_a_kind_result(hand) == True:
        if "four" in results:
            results["four"].append(hand)
        else:
            results["four"] = [hand]
    elif is_full_house_result(hand) == True:
        if "full" in results:
            results["full"].append(hand)
        else:
            results["full"] = [hand]
    elif is_three_of_a_kind_result(hand) == True:
        if "three" in results:
            results["three"].append(hand)
        else:
            results["three"] = [hand]
    elif is_two_pairs_result(hand) == True:
        if "two_pairs" in results:
            results["two_pairs"].append(hand)
        else:
            results["two_pairs"] = [hand]
    elif is_one_pair_result(hand) == True:
        if "one_pair" in results:
            results["one_pair"].append(hand)
        else:
            results["one_pair"] = [hand]
    else:
        if "one_card" in results:
            results["one_card"].append(hand)
        else:
            results["one_card"] = [hand]


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


def is_five_of_a_kind_result(hand):
    if len(set(hand.cards)) == 1:
        return True
    else:
        return False


def is_four_of_a_kind_result(hand):
    hand_set = set(hand.cards)
    if len(hand_set) == 2:
        for card in hand_set:
            if hand.cards.count(card) == 4:
                return True
    return False


def is_full_house_result(hand):
    hand_set = set(hand.cards)
    is_three_card = False;
    is_two_card = False;
    if len(hand_set) == 2:
        for card in hand_set:
            if hand.cards.count(card) == 3:
                is_three_card = True
            if hand.cards.count(card) == 2:
                is_two_card = True
    return is_three_card and is_two_card


def is_three_of_a_kind_result(hand):
    hand_set = set(hand.cards)
    for card in hand_set:
            if hand.cards.count(card) == 3:
                return True
    return False


def is_two_pairs_result(hand):
    hand_set = set(hand.cards)
    is_two_card = 0;
    is_one_card = False;
    if len(hand_set) == 3:
        for card in hand_set:
            if hand.cards.count(card) == 2:
                is_two_card += 1
            if hand.cards.count(card) == 1:
                is_one_card = True
    return is_two_card == 2 and is_one_card


def is_one_pair_result(hand):
    hand_set = set(hand.cards)
    is_pair = False;
    single_cards = 0;
    if len(hand_set) == 4:
        for card in hand_set:
            if hand.cards.count(card) == 2:
                is_pair = True
            if hand.cards.count(card) == 1:
                single_cards += 1
    return is_pair and single_cards == 3


class Hand:
    cards = []
    bid = 0
    points = 0
    cards_int = 0;

    def __init__(self):
        self.cards = []
        self.bid = 0
        self.points = 0
        self.cards_int = 0

    def __str__(self):
        return (
            "Cards: "
            + str(self.cards)
            + " Bid: "
            + str(self.bid)
            + " Points: "
            + str(self.points)
            + " Cards int: "
            + str(self.cards_int)
        )


if __name__ == "__main__":
    main()
