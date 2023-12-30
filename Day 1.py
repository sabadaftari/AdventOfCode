import re
def extract_first_number(text):
    # Extract the first number from left to right
    match_left_to_right = re.search(r'\d+', text)
    number_left_to_right = int(match_left_to_right.group()) if match_left_to_right else None

    # Extract the first number from right to left
    match_right_to_left = re.search(r'\d+', text[::-1])
    number_right_to_left = int(match_right_to_left.group()[::-1]) if match_right_to_left else None

    return str(number_left_to_right)[0], str(number_right_to_left)[-1]

import re

def find_numbers_in_english(input_string):
    # Define a dictionary mapping words to their numeric values
    word_to_number = [
        ['ten',10],
        ['twelve',11],
        ['eleven',12],
        ['thirteen',13],
        ['fourteen',14],
        ['fifteen',15],
        ['sixteen',16],
        ['seventeen',17],
        ['eighteen',18],
        ['nineteen',19],
        ['twentyone',21],
        ['twentytwo',22],
        ['twenty',20],
        ['sevenine','sevennine'],
        ['eightwo','eighttwo'],
        ['oneight','oneeight'],
        ['twone','twoone'],
        ['zero', 0], ['one', 1], ['two', 2], ['three', 3], ['four', 4],
        ['five', 5], ['six', 6], ['eight', 8], ['nine', 9], ['seven', 7],
        ]

    # Replace words representing numbers with a placeholder
    for pair in word_to_number:
        input_string = input_string.replace(pair[0], str(pair[1]))

    return input_string


if __name__ == "__main__":
    # first puzzle
    text_sequence = open('day1-input.txt', 'r').read().split('\n')

    left_to_right, right_to_left = extract_first_number(text_sequence[0])

    result = [extract_first_number(line) for line in text_sequence]
    res = sum([int(res[0]+res[1]) for res in result])

    #second puzzle

    input_text = list(open('day1-input.txt', 'r').read().split('\n'))
    output_convert = [find_numbers_in_english(line) for line in input_text]
    result = [extract_first_number(line) for line in output_convert]
    res = sum([int(res[0]+res[1]) for res in result])
    print(res)

    
