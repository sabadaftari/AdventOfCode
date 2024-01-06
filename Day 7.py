import re

def convert_to_list(input_string):

    # Using re.split() to separate characters by space or equals sign
    result = re.split(r'[ ,]', input_string)

    # Removing empty strings from the result
    result = [item for item in result if item]
    return result

def search_Full_House(hand):
    
    if not hand in {'AAAAA','KKKKK','QQQQQ','JJJJJ','TTTTT'}:
        return False
    else:
        return True

def search_Four_of_a_kind(hand):
    
    # Count occurrences of each label in the hand
    label_counts = {}
    for card in hand:
        label_counts[card] = label_counts.get(card, 0) + 1

    # Check if there is a card with a count of 4 and another with a count of 1
    for count in label_counts.values():
        if count == 4:
            return True

    return False

def search_Five_of_a_kind(hand):

    # Count the occurrences of each label in the hand
    label_counts = {}
    for card in hand:
        label_counts[card] = label_counts.get(card, 0) + 1

    # Check if there is a card with a count of 3 and another with a count of 2
    three_of_a_kind = False
    two_of_a_kind = False
    for count in label_counts.values():
        if count == 3:
            three_of_a_kind = True
        elif count == 2:
            two_of_a_kind = True

    return three_of_a_kind and two_of_a_kind

def search_Three_of_a_kind(hand):

    # Count the occurrences of each label in the hand
    label_counts = {}
    for card in hand:
        label_counts[card] = label_counts.get(card, 0) + 1

    # Check if there is a card with a count of 3
    three_of_a_kind = False
    for count in label_counts.values():
        if count == 3:
            three_of_a_kind = True

    # Check if there are only three distinct labels in the hand
    distinct_labels = len(label_counts) == 3

    return three_of_a_kind and distinct_labels

def search_Two_pair(hand):

    # Count the occurrences of each label in the hand
    label_counts = {}
    for card in hand:
        label_counts[card] = label_counts.get(card, 0) + 1

    # Check if there are two pairs (cards with a count of 2)
    pairs_count = 0
    for count in label_counts.values():
        if count == 2:
            pairs_count += 1

    # Check if there are only three distinct labels in the hand
    distinct_labels = len(label_counts) == 3

    return pairs_count == 2 and distinct_labels

def search_One_pair(hand):
    # Assuming hand is a list of card labels like ['A', '2', '3', 'A', '4']
    # Count the occurrences of each label in the hand
    label_counts = {}
    for card in hand:
        label_counts[card] = label_counts.get(card, 0) + 1

    # Check if there is a pair (cards with a count of 2)
    pairs_count = 0
    for count in label_counts.values():
        if count == 2:
            pairs_count += 1

    # Check if there are only four distinct labels in the hand
    distinct_labels = len(label_counts) == 4

    return pairs_count == 1 and distinct_labels

def search_High_card(hand):
    # Assuming hand is a list of card labels like ['2', '3', '4', '5', '6']
    return len(set(hand)) == len(hand)

def make_integer(input):
    input[1]=int(input[1])
    return input

def label_to_value(label):
    # Define a function to convert card labels to numerical values for comparison
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return values[label]

def sort_key(hand):
    return [label_to_value(card) for card in hand]

def sort_hands_by_value(hands):
    return sorted(hands, key=sort_key)

if __name__ == "__main__":

    text_sequence = list(open('day7-input.txt', 'r').read().split('\n'))
    converted_texts = [convert_to_list(text) for text in text_sequence]
    converted = [make_integer(t) for t in converted_texts]
    types = {'full': [], 'five': [], 'four': [],'three': [],'two': [], 'one': [], 'high_card': []}
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    
    for hand in converted:
        if search_Full_House(hand[0]):
            types['full'].append(hand)
        if search_Five_of_a_kind(hand[0]):
            types['five'].append(hand)
        if search_Four_of_a_kind(hand[0]):
            types['four'].append(hand)
        if search_Three_of_a_kind(hand[0]):
            types['three'].append(hand)
        if search_Two_pair(hand[0]):
            types['two'].append(hand)
        if search_One_pair(hand[0]):
            types['one'].append(hand)
        if search_High_card(hand[0]):
            types['high_card'].append(hand)

    new_list = [sorted(types[t], key=lambda x: [[card] for card in x[0]]) for t in types]
    winnings = [new_list[key]*converted[key] for key in len()]
    print(sum(winnings))
