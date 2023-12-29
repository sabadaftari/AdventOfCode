import re

def extract_first_number(text):
    # Extract the first number from left to right
    match_left_to_right = re.search(r'\d+', text)
    number_left_to_right = int(match_left_to_right.group()) if match_left_to_right else None

    # Extract the first number from right to left
    match_right_to_left = re.search(r'\d+', text[::-1])
    number_right_to_left = int(match_right_to_left.group()[::-1]) if match_right_to_left else None

    return str(number_left_to_right)[0], str(number_right_to_left)[-1]

if __name__ == "__main__":
    # Example usage:
    text_sequence = open('day1-input.txt', 'r').read().split('\n')

    left_to_right, right_to_left = extract_first_number(text_sequence[0])

    result = [extract_first_number(line) for line in text_sequence]
    res = sum([int(res[0]+res[1]) for res in result])

