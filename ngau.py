import itertools
import random

poker_hand = ['3', '4', 'A', '18', 'K']
rank = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# ♠️ Ace Spade = A, other Ace = 1
point = {
    'A' : 1,
    '1' : 1,
    '2' : 2,
    '3' : [3,6],
    '4' : 4,
    '5' : 5,
    '6' : [6,3],
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10': 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10,
}

def checkNgau(three_card_combination):
    score = 0
    numOf36 = 0 
    for i in three_card_combination:
        try:
            score += point[i]
        except TypeError:
           numOf36 += 1

    if numOf36 == 0:
        if score % 10 == 0:
            return True
        else:
            return False
    elif numOf36 == 1:
        possible_score = [3, 6]
    elif numOf36 == 2:
        possible_score = [6, 9, 12]
    else:
        return False

    for i in possible_score:
        score += i
        if score % 10 == 0:
            return True
        else:
            score -= i
    return False

def check5pictures(poker_hand):
    count_of_picture = poker_hand.count('J') + poker_hand.count('Q') + poker_hand.count('K')
    if count_of_picture == 5:
        return True
    else:
        return False

def checkTonku(poker_hand):
    poker_copy = poker_hand.copy()
    if 'A' not in poker_copy:
        return False

    poker_copy.remove('A')

    picture = ['J', 'Q', 'K']
    for i in picture:
        if i in poker_copy:
            poker_copy.remove(i)
            break
    # Check if the remaining cards have
    if len(poker_copy) == 3:
        return checkNgau(poker_copy)
    else:
        return False

def subtraction(poker_hand, card_list):
    poker_copy = poker_hand.copy()
    for card in card_list:
        poker_copy.remove(card)
    return poker_copy

def higher_rank(other_two, max_rank):
    
    poker_rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', '1']
    
    if 'A' in max_rank:
        max_rank[max_rank.index('A')] = '1'
    if 'A' in other_two:
        other_two[other_two.index('A')] = '1'

    max_double = max_rank[0] == max_rank[1] # Double flag for max_rank
    other_double = (other_two[0] == other_two[1]) # Double flag for other_double
    if max_double and other_double: # When both of them is double
        if poker_rank.index(other_two[0]) > poker_rank.index(max_rank[0]):
            return True, ("🐮 🐮 Double-Ox " + other_two[0])
        else:
            return False, ("🐮 🐮 Double-Ox " + max_rank[0])
    elif max_double ^ other_double: # XOR operator
        '''
        If one of them is double, then double one is max_rank
        '''
        if max_double:
            return False, ("🐮 🐮 Double-Ox " + max_rank[0])
        else:
            return True, ("🐮 🐮 Double-Ox " + other_two[0])
    else:
        max_point = 0
        totalOf36 = 0
        for i in max_rank:
            try:
                max_point += point[i]
            except TypeError:
                totalOf36 += 1
        if totalOf36 == 2:
            max_point = 6 + 3
        elif totalOf36 == 1:
            max_point1 = max_point + 3
            max_point2 = max_point + 6 
            if (max_point2 % 10 if max_point2 > 10 else max_point2) > (max_point1 % 10 if max_point1 > 10 else max_point1):
                max_point = max_point2
            else:
                max_point = max_point1
        
        other_point = 0
        totalOf36 = 0
        for i in other_two:
            try:
                other_point += point[i]
            except TypeError:
                totalOf36 += 1
        if totalOf36 == 2:
            other_point = 6 + 3
        elif totalOf36 == 1:
            other_point1 = other_point + 3
            other_point2 = other_point + 6 
            if (other_point2 % 10 if other_point2 > 10 else other_point2) > (other_point1 % 10 if other_point1 > 10 else other_point1):
                other_point = other_point2
            else:
                other_point = other_point1
        
        if max_point > 10:
            max_point %= 10
        if other_point > 10:
            other_point %= 10
        if  other_point > max_point:
            return True, f"🐂 Ox of {other_point}"
        else:
            return False, f"🐂 Ox of {max_point}"

def main():
    print("Note: ♠️ Ace Spade = A, other Ace = 1")
    poker_hand = input("Enter 5 cards 🃏 with space: ").split()
    
    # Generate 5 random cards
    # poker_hand = []
    # for i in range(1,6):
    #     poker_hand.append(random.choice(list(point.keys())))
    # print(poker_hand)

    if check5pictures(poker_hand):
        print("🃛 🃜 🃝 🃞 🃛 Five pictures!")
        return
    elif checkTonku(poker_hand):
        print("🂾 🂡 Tonku")
        return

    
    Ngau_list = []
    for sampled_list in itertools.combinations(poker_hand, 3):
        if checkNgau(sampled_list):
            Ngau_list.append(list(sampled_list))


    score = 0
    Ngau_list = list(set(tuple(sorted(item)) for item in Ngau_list))
    if Ngau_list:
        print("Possible combination")
    for item in Ngau_list:
        print(item)
    other_two_list = []
    if len(Ngau_list) != 0: # Check have Ngau or not 
        for combination in Ngau_list:
            other_two_list.append(subtraction(poker_hand, combination))
            
        max_rank = other_two_list[0]
        for other_two in other_two_list[0:]:
            is_higher_rank, description = higher_rank(other_two, max_rank)
            if is_higher_rank:
                max_rank = other_two
        
        print("---Highest ranking---")
        print(subtraction(poker_hand, max_rank))    
        print(max_rank)    
        print(description)
    else:
        # No Ngau
        print("😞 No Ox")


if __name__ == '__main__':
    main()